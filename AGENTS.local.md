# Shared-policy repository instructions

- The canonical distributable baseline is [`agent-policy/AGENTS.shared.md`](agent-policy/AGENTS.shared.md).
- The root `AGENTS.md` is generated from that file and this repository's local instructions. Edit the source files, then run `python3 scripts/render-agent-instructions.py --shared agent-policy/AGENTS.shared.md --local AGENTS.local.md --output AGENTS.md --source-label 'KGBos/.github canonical baseline'`.
- Keep the canonical baseline concise and portable. Put extended rationale and workflow detail in `docs/` and link to it only when the agent is explicitly told to read it for applicable work.
- Downstream repositories should vendor the baseline and renderer from one exact commit, record its SHA and file digests, compose their local instructions, and run the renderer in CI without network access.
