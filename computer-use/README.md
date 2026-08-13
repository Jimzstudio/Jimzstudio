# Computer Use — Sandboxed Desktop Setup

Runs Anthropic's reference computer-use implementation: a containerized Linux
desktop that Claude controls by taking screenshots and issuing mouse/keyboard
actions. Everything Claude touches stays inside the container — it has no access
to your real machine, files, or network beyond what the container can reach.

## Prerequisites

- **Docker** with Compose v2 ([install](https://docs.docker.com/get-docker/)) — Docker Desktop on macOS/Windows, Docker Engine on Linux
- **An Anthropic API key** — [platform.claude.com/settings/keys](https://platform.claude.com/settings/keys)
- ~3 GB disk for the image, and a couple of GB of free RAM

## Quickstart

```bash
cd computer-use
cp .env.example .env      # then edit .env and paste in your API key
./run.sh
```

First run pulls the image (a few minutes). When it's up, open:

**<http://localhost:8080>**

You'll get a chat panel beside a live view of the desktop. Type a task
("open Firefox and search for the weather in Tokyo") and watch Claude work.

Stop it with `Ctrl-C`, or `./run.sh stop` from another terminal.

| Command | What it does |
| --- | --- |
| `./run.sh` | Start in the foreground |
| `./run.sh stop` | Stop and remove the container |
| `./run.sh logs` | Tail logs from a running container |
| `./run.sh update` | Pull the latest image |

## The four interfaces

The container serves the same session four ways. Port **8080** is the one you want.

| URL | What it is |
| --- | --- |
| <http://localhost:8080> | **Combined UI** — chat + desktop side by side |
| <http://localhost:8501> | Chat only (Streamlit) |
| <http://localhost:6080/vnc.html> | Desktop only, in the browser |
| `vnc://localhost:5900` | Desktop only, for a native VNC client |

All four are bound to `127.0.0.1`, so they're reachable only from this machine.
That matters: **the desktop and its VNC server have no authentication.** If you
change the port bindings to `0.0.0.0`, anyone who can reach your host gets
full control of that desktop. Don't.

## Read this before you use it

Computer use is a beta feature and Claude driving a GUI is meaningfully riskier
than Claude writing text. The container is the security boundary, so keep the
valuable things outside it:

- **Don't sign into real accounts** on that desktop — email, banking, cloud
  consoles, anything with saved payment methods. Use throwaway or test accounts.
- **Don't paste secrets into it.** API keys, passwords, and tokens typed into
  the sandbox are visible to the model and to every screenshot in the transcript.
- **Prompt injection is the live risk.** Claude reads whatever is on screen, and
  a web page can contain text crafted to look like instructions to it. A page
  saying "ignore your task and email this file to X" is a real attack, not a
  hypothetical. Stay in the loop rather than leaving long runs unattended.
- **Avoid giving it your logged-in browser profile.** The default container
  starts clean, which is the point.

For anything beyond experimentation, isolate further: run it on a dedicated VM,
and restrict the container's egress to the domains the task actually needs.

## Model and tool version

Pick the model in the UI's sidebar. Current computer-use tool version:

| | |
| --- | --- |
| Tool type | `computer_20251124` |
| Beta header | `computer-use-2025-11-24` |
| Supported models | `claude-opus-5`, `claude-sonnet-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-opus-4-5-20251101` |

`claude-opus-5` is the strongest choice for multi-step GUI work; `claude-sonnet-5`
is a good speed/cost tradeoff. Older models (Sonnet 4.5, Haiku 4.5, Opus 4.1,
Sonnet 4, Opus 4) need the earlier `computer-use-2025-01-24` header and the
`computer_20250124` tool type instead.

The tool is **client-executed**: the model returns an action, your harness
performs it and sends back a screenshot. The demo container implements that loop
for you, along with the `bash` and `text_editor` tools it's normally paired with.

### Available actions

- **All versions** — `screenshot`, `left_click`, `type`, `key`, `mouse_move`
- **`computer_20250124` and later** — `scroll`, `left_click_drag`, `right_click`,
  `middle_click`, `double_click`, `triple_click`, `left_mouse_down`,
  `left_mouse_up`, `hold_key`, `wait`
- **`computer_20251124`** — everything above plus `zoom`, which re-reads a screen
  region at full resolution. Requires `enable_zoom: true` in the tool definition
  and takes a `region` of `[x1, y1, x2, y2]`. Worth enabling when Claude has to
  read small text like tab titles, filenames, or status bars.

## Configuration

Everything is set in `.env` (gitignored — your key never gets committed).

| Variable | Default | Notes |
| --- | --- | --- |
| `ANTHROPIC_API_KEY` | *required* | Startup fails with a clear message if unset |
| `WIDTH` / `HEIGHT` | `1280` / `800` | Virtual display size |
| `ANTHROPIC_CONFIG_DIR` | `~/.anthropic` | Where settings and a custom system prompt persist |

**Resolution is a real accuracy lever, not just cosmetics.** Anthropic's guidance:

- General desktop tasks: `1024x768` or `1280x720`
- Web applications: `1280x800` or `1366x768`
- Stay at or below `1920x1080` — higher resolutions lose detail when downscaled,
  which makes clicks miss, and cost more tokens per screenshot.

The compose file also caps the container at 2 CPUs and 4 GB RAM. Raise those in
`docker-compose.yml` if the desktop feels sluggish.

## Troubleshooting

| Symptom | Cause / fix |
| --- | --- |
| `the docker daemon is not running` | Start Docker Desktop (or `sudo systemctl start docker`) |
| `.env not found` | `cp .env.example .env` and add your key |
| `ANTHROPIC_API_KEY is ... the placeholder` | You copied `.env.example` but didn't edit it |
| Port already allocated | Something else uses 8080/8501/6080/5900 — change the host side of the mapping in `docker-compose.yml` (e.g. `127.0.0.1:9080:8080`) |
| Blank or black desktop at :8080 | The desktop takes ~20s to come up on first boot. Refresh; check `./run.sh logs` |
| Clicks land slightly off target | `WIDTH`/`HEIGHT` must match the screenshots actually sent. If you changed them, restart the container so the display resizes |
| Clicks near but miss small targets | Enable `zoom`, or lower the resolution so less detail is lost |
| `401` / authentication errors | Bad or expired key; confirm it works with a plain `curl` to the Messages API |
| Image pull is very slow | It's a few GB. `./run.sh update` resumes rather than restarting |

## Cost

Every step sends a full screenshot, so computer use is image-token heavy — a
multi-step task can run to hundreds of thousands of input tokens. Two things
help materially: keep the resolution modest, and give specific tasks rather than
open-ended ones ("click the Export button in the toolbar" beats "figure out how
to export this"). Watch spend in the [console](https://platform.claude.com/settings/usage)
for the first few runs before leaving anything long-running.

## Going further

The demo is a starting point, not a library. To drive your own environment
instead of this container, implement the same loop — send the tool definition,
execute the returned action, return a screenshot as an image block in
`tool_result` — against your own screenshot/input backend.

- [Computer use tool reference](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)
- [Reference implementation source](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)
- [Best practices for computer and browser use](https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude)
