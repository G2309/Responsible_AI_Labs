import argparse
import json
import urllib.error
import urllib.request

G = "\033[32m"
R = "\033[31m"
Y = "\033[33m"
C = "\033[36m"
B = "\033[1m"
X = "\033[0m"


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-host", required=True)
    parser.add_argument("-port", required=True)
    parser.add_argument("words", nargs="+")
    args = parser.parse_args()

    words = args.words
    if len(words) > 1 and words[0] == "text":
        words = words[1:]
    text = " ".join(words)

    url = f"http://{args.host}:{args.port}/moderate"
    payload = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            body = json.loads(resp.read().decode("utf-8"))
            verdict = str(body.get("verdict", "")).upper()
            color = R if verdict == "BLOCKED" else G
            print(
                f"{B}{color}Verdict: {verdict}{X}"
                f"{C} | Confidence: {body.get('confidence')} | Reason: {body.get('reason')}{X}"
            )
    except urllib.error.HTTPError as e:
        try:
            body = json.loads(e.read().decode("utf-8"))
            msg = body.get("error", str(e))
        except Exception:
            msg = str(e)
        if e.code == 400:
            print(f"{Y}Error: {msg}{X}")
        else:
            print(f"{R}Error del servidor: {msg}{X}")
    except (urllib.error.URLError, TimeoutError, OSError):
        print(f"{R}Provider no disponible (timeout){X}")


main()
