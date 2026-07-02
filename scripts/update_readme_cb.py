import re
import time
import os

def main():
    # Locate the README.md relative to the script location (one directory up from scripts/)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    readme_path = os.path.abspath(os.path.join(script_dir, "..", "README.md"))
    
    if not os.path.exists(readme_path):
        print(f"Error: README.md not found at {readme_path}")
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    timestamp = str(int(time.time()))
    
    # Matches URLs belonging to github-readme-stats, streak-stats, github-readme-activity-graph, or komarev containing a cache_bust query parameter
    pattern = r'((?:github-readme-stats\.shion\.dev|streak-stats\.demolab\.com|github-readme-activity-graph\.vercel\.app|komarev\.com)[^"\']*?cache_bust=)\d+'
    
    new_content, count = re.subn(pattern, r'\g<1>' + timestamp, content)
    
    if count > 0:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Successfully updated cache_bust to {timestamp} in {count} locations in README.md")
    else:
        print("No cache_bust parameters found or updated in README.md")

if __name__ == "__main__":
    main()
