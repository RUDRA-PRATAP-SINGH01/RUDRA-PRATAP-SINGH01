import re
import time
import os
import urllib.request

STREAK_URL = (
    "https://github-readme-streak-stats-eight.vercel.app/"
    "?user=RUDRA-PRATAP-SINGH01"
    "&background=0d1117"
    "&ring=3b82f6"
    "&fire=10b981"
    "&currStreakNum=10b981"
    "&currStreakLabel=3b82f6"
    "&sideNums=10b981"
    "&sideLabels=3b82f6"
    "&dates=8b949e"
    "&hide_border=true"
    "&disable_animations=true"
)

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; ReadmeBot/1.0)"}


def refresh_streak_svg(script_dir: str) -> bool:
    """Download the latest streak SVG and save it to assets/streak_card.svg."""
    assets_dir = os.path.abspath(os.path.join(script_dir, "..", "assets"))
    os.makedirs(assets_dir, exist_ok=True)
    out_path = os.path.join(assets_dir, "streak_card.svg")

    try:
        req = urllib.request.Request(STREAK_URL, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp:
            data = resp.read()
        with open(out_path, "wb") as f:
            f.write(data)
        print(f"Updated streak card SVG ({len(data)} bytes) -> {out_path}")
        return True
    except Exception as e:
        print(f"Warning: Could not refresh streak SVG: {e}")
        return False


def update_cache_bust(script_dir: str) -> None:
    """Update cache_bust timestamps in README.md."""
    readme_path = os.path.abspath(os.path.join(script_dir, "..", "README.md"))

    if not os.path.exists(readme_path):
        print(f"Error: README.md not found at {readme_path}")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    timestamp = str(int(time.time()))
    pattern = r"([?&]cache_bust=)\d+"
    new_content, count = re.subn(pattern, r"\g<1>" + timestamp, content)

    if count > 0:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated cache_bust to {timestamp} in {count} locations in README.md")
    else:
        print("No cache_bust parameters found in README.md")


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    refresh_streak_svg(script_dir)
    update_cache_bust(script_dir)


if __name__ == "__main__":
    main()
