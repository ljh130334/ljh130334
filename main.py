import feedparser, time

URL = "https://fl0gydev.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 7

# 기존 README.md 내용 읽기
try:
    with open("README.md", "r", encoding="utf-8") as f:
        existing_content = f.read()
except FileNotFoundError:
    existing_content = ""

# 블로그 포스트 섹션 생성
blog_section = """
## Latest Blog Post
"""
for idx, feed in enumerate(RSS_FEED['entries']):
    if idx >= MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        blog_section += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

# 기존 블로그 섹션이 있는지 확인하고 교체 또는 추가
start_marker = "## Latest Blog Post"
if start_marker in existing_content:
    # 기존 블로그 섹션 찾아서 교체
    lines = existing_content.split('\n')
    new_lines = []
    skip_section = False
    
    for line in lines:
        if line.strip() == start_marker.strip():
            skip_section = True
            break
        new_lines.append(line)
    
    # 기존 내용 + 새로운 블로그 섹션
    final_content = '\n'.join(new_lines) + blog_section
else:
    # 기존 내용 아래에 블로그 섹션 추가
    final_content = existing_content + blog_section

# README.md 업데이트
with open("README.md", "w", encoding="utf-8") as f:
    f.write(final_content)
