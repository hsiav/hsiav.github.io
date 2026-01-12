import feedparser
from deep_translator import GoogleTranslator

# 設定新聞來源
SOURCES = {
    "cnn": {
        "rss_url": "http://rss.cnn.com/rss/edition_world.rss",
        "output_file": "cnn_news.md"
    },
    "nhk": {
        "rss_url": "https://www3.nhk.or.jp/rss/news/cat0.xml",
        "output_file": "nhk_news.md"
    },
    "dw": {
        "rss_url": "https://rss.dw.com/rdf/rss-en-all",
        "output_file": "dw_news.md"
    }
}

def fetch_news(rss_url, max_items=5):
    feed = feedparser.parse(rss_url)
    if not feed.entries:
        print(f"❌ 無法從 {rss_url} 抓資料。")
        return []
    
    news_list = []
    for entry in feed.entries[:max_items]:
        title = entry.get("title", "無標題")
        summary = entry.get("summary", entry.get("description", "無摘要"))
        link = entry.get("link", "")
        news_list.append({"title": title, "summary": summary, "link": link})
    return news_list

def translate(text, target_lang="zh-CN"):
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except Exception as e:
        print(f"⚠️ 翻譯失敗：{e}")
        return text

def save_to_markdown(news_list, filename, source_name):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# {source_name.upper()} 國際新聞摘要\n\n")
        for idx, item in enumerate(news_list, 1):
            title_cn = translate(item["title"])
            summary_cn = translate(item["summary"])
            f.write(f"### {idx}. {title_cn}\n\n")
            f.write(f"{summary_cn}\n\n")
            f.write(f"[🔗 原文連結]({item['link']})\n\n")
    print(f"✅ {source_name.upper()} 儲存完成：{filename}")

if __name__ == "__main__":
    for source_name, info in SOURCES.items():
        print(f"\n📡 抓取 {source_name.upper()}...")
        news = fetch_news(info["rss_url"])
        if news:
            save_to_markdown(news, info["output_file"], source_name)
        else:
            print(f"⚠️ {source_name.upper()} 沒抓到新聞。")
