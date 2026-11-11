import React, { useEffect, useState } from "react";
import { Images, Shuffle, Info, AlertTriangle } from "lucide-react";

const NAMES = { V: "Victim", S: "Suspect", C: "Scene" };
const tagLine = (tags) =>
  Object.entries(tags || {})
    .map(([tag, count]) => `${tag} ×${count}`)
    .join(" · ");

function Check({ checked, disabled, onChange, label, note }) {
  const [pending, setPending] = useState(null);
  return (
    <label className="ep-checkbox">
      <input
        type="checkbox"
        aria-label={label}
        checked={pending ?? checked}
        disabled={disabled}
        onChange={(ev) => {
          setPending(ev.target.checked);
          Promise.resolve(onChange(ev.target.checked)).then(
            () => setPending(null),
            () => setPending(null),
          );
        }}
      />{" "}
      <span>
        <b>{label}</b>
        <small>{note}</small>
      </span>
    </label>
  );
}

export default function BaseImages({ project, api, plan, disabled, save }) {
  const e = project.episode || {};
  const [report, setReport] = useState(null);
  const key = [
    project.id,
    project.assets.length,
    e.base_seed || 1,
    e.base_fill,
    e.base_label,
    e.base_hold,
    plan?.timeline_digest || "",
    e.guide?.hash || "",
  ].join("|");
  useEffect(() => {
    let live = true;
    api(`/api/projects/${project.id}/episode/base-report`)
      .then((r) => live && setReport(r))
      .catch(() => live && setReport(null));
    return () => {
      live = false;
    };
  }, [key]);
  return (
    <BaseImagesView
      project={project}
      report={report}
      plan={plan}
      disabled={disabled}
      save={save}
    />
  );
}

export function BaseImagesView({ project, report, plan, disabled, save }) {
  const e = project.episode || {};
  if (!e.guide) return null;
  const pool = report?.pool || { V: 0, S: 0, C: 0 };
  const total = pool.V + pool.S + pool.C;
  const fill = plan?.base_fill;
  const setup = report?.setup;
  const locked = disabled || project.is_demo;
  const on = e.base_fill !== false;
  const findings = report?.findings || [];
  const listed = report?.guide_base_files || [];
  return (
    <section className="ep-base" aria-label="Base images">
      <div className="ep-base-head">
        <Images size={18} />
        <h3>Base images</h3>
        <span>
          Relevant archive visuals for narration that has no matching clip
        </span>
      </div>
      <div className="ep-base-counts">
        {["V", "S", "C"].map((b) => (
          <div key={b}>
            <b>{pool[b]}</b>
            <span>{NAMES[b]} images</span>
            <small>{tagLine(report?.pool_tags?.[b]) || "no tags yet"}</small>
          </div>
        ))}
      </div>
      {total === 0 ? (
        <p className="ep-small">
          <Info size={12} /> None uploaded yet. Name files{" "}
          <code>BASE-V--portrait--01.jpg</code> (V victim, S suspect, C
          scene/location; add as many as you like) and upload them with your
          footage. {listed.length > 0
            ? `The guide lists ${listed.length} to collect.`
            : "Your guide's File checklist lists the exact names."}
        </p>
      ) : (
        <p className="ep-small">
          {setup?.present
            ? `Names from the guide: victim ${setup.victims.join(", ") || "not given"} · suspect ${setup.suspects.join(", ") || "not given"}.`
            : "The guide has no Project setup block, so images are chosen from its Fill hints and the wording of each line."}
        </p>
      )}
      <div className="ep-base-controls">
        <Check
          checked={on}
          disabled={locked}
          label="Cover gaps and clip tails with base images"
          note="A clip plays once, then a relevant base image takes over instead of looping. Off restores marked gap cards and looping."
          onChange={(v) =>
            save("/episode/options", "PATCH", { base_fill: v })
          }
        />
        <Check
          checked={e.base_label !== false}
          disabled={locked || !on}
          label="Label them “Archive image, not footage of the narrated event”"
          note="Recommended: keeps the viewer from mistaking a stand-in for the real moment."
          onChange={(v) =>
            save("/episode/options", "PATCH", { base_label: v })
          }
        />
        <label className="ep-base-hold">
          <span>Longest base shot</span>
          <select
            aria-label="Longest base image shot"
            disabled={locked || !on}
            value={String(e.base_hold || 8)}
            onChange={(ev) =>
              save("/episode/options", "PATCH", {
                base_hold: Number(ev.target.value),
              })
            }
          >
            {[5, 6, 8, 10, 12].map((s) => (
              <option key={s} value={s}>
                {s} seconds
              </option>
            ))}
          </select>
        </label>
        <button
          className="btn"
          aria-label="Reshuffle base images"
          disabled={locked || !on || total === 0 || !plan}
          onClick={() =>
            save("/episode/options", "PATCH", { reshuffle: true })
          }
        >
          <Shuffle size={14} /> Reshuffle (order {e.base_seed || 1})
        </button>
      </div>
      {fill && (
        <p className="ep-small">
          {fill.fills} base shots cover {Math.round(fill.seconds)} s ·{" "}
          {fill.unfilled
            ? `${Math.round(fill.unfilled_seconds)} s still unfilled · `
            : ""}
          no image used more than {fill.max_uses_seen}× (limit{" "}
          {fill.max_uses}). Same order every time unless you reshuffle.
        </p>
      )}
      {findings.length > 0 && (
        <ul className="ep-base-findings">
          {findings.map((f, i) => (
            <li key={f.code + i}>
              <AlertTriangle size={12} /> {f.detail}
            </li>
          ))}
        </ul>
      )}
    </section>
  );
}
