#!/usr/bin/env bash
# Launch the sandboxed computer-use desktop.
#
#   ./run.sh          start (foreground, Ctrl-C to stop)
#   ./run.sh stop     stop and remove the container
#   ./run.sh logs     tail logs of a running container
#   ./run.sh update   pull the latest image

set -euo pipefail
cd "$(dirname "$0")"

die() { printf '\033[31merror:\033[0m %s\n' "$1" >&2; exit 1; }

case "${1:-start}" in
  stop)   exec docker compose down ;;
  logs)   exec docker compose logs -f ;;
  update) exec docker compose pull ;;
  start)  ;;
  *)      die "unknown command '${1}' (expected: start, stop, logs, update)" ;;
esac

if [ ! -f .env ]; then
  die ".env not found. Run:  cp .env.example .env  then add your ANTHROPIC_API_KEY"
fi

# shellcheck disable=SC1091
set -a; . ./.env; set +a

case "${ANTHROPIC_API_KEY:-}" in
  ""|"sk-ant-...") die "ANTHROPIC_API_KEY is unset or still the placeholder - edit .env" ;;
esac

command -v docker >/dev/null 2>&1 || die "docker is not installed - see https://docs.docker.com/get-docker/"
docker info >/dev/null 2>&1 || die "the docker daemon is not running - start Docker Desktop (or dockerd) and retry"

cat <<'BANNER'

  Claude will have full mouse and keyboard control of the desktop inside this
  container. Treat that desktop as untrusted:

    - Do not log into accounts you would mind losing.
    - Do not paste credentials, tokens, or payment details into it.
    - Content Claude reads from a web page can influence what it does next
      (prompt injection). Watch the session rather than leaving it unattended.

  Everything is bound to 127.0.0.1 - the desktop is not exposed to your network.

BANNER

echo "Starting... the UI will be at http://localhost:8080"
echo

exec docker compose up
