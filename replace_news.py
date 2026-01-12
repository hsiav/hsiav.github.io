import re

MAIN_FILE = "index.md"
NEWS_FILE = "cnn_news.md"

def replace_news_block(main_file, news_file, source_name):
    with open(main_file, "r", encoding="utf-8") as f:
        main_content = f.read()

    with open(news_file, "r", encoding="utf-8") as f:
        news_content = f.read()

    # 正確的 markdown 標題是 "# CNN 國際新聞摘要"
    pattern = fr"# {source_name.upper()} [國国]際新聞摘要.*?最近更新"

    new_block = news_content.strip() + "\n\n最近更新"

    if re.search(pattern, main_content, flags=re.DOTALL):
        new_main_content = re.sub(pattern, new_block, main_content, flags=re.DOTALL)
        with open(main_file, "w", encoding="utf-8") as f:
            f.write(new_main_content)
        print(f"✅ 已更新 {main_file} 的 {source_name.upper()} 區塊。")
    else:
        print(f"❌ 找不到標題區塊：# {source_name.upper()} 國際新聞摘要")
if __name__ == "__main__":
    replace_news_block("index.md", "cnn_news.md", "cnn")



