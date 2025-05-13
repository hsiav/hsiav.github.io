from transformers import pipeline
import random
import os

# 使用 Hugging Face 的改寫管道
rewriter = pipeline("text2text-generation", model="t5-small")

# 文件路徑
FILE_PATH = "index.md"

def load_paragraphs(file_path):
    """從文件中讀取所有段落，忽略空行。"""
    with open(file_path, "r", encoding="utf-8") as file:
        paragraphs = [line.strip() for line in file.readlines() if line.strip()]
    return paragraphs

def save_paragraphs(file_path, paragraphs):
    """將更新後的段落寫回文件。"""
    with open(file_path, "w", encoding="utf-8") as file:
        file.write("\n\n".join(paragraphs))

def rewrite_paragraph(paragraph):
    """使用 T5 模型進行改寫。"""
    prompt = f"Paraphrase the following sentence:\n\n{paragraph}"
    result = rewriter(prompt, max_length=200, num_return_sequences=1)
    return result[0]["generated_text"].strip()

def main():
    if not os.path.exists(FILE_PATH):
        print(f"檔案 {FILE_PATH} 不存在，請確認路徑正確。")
        return

    # 讀取段落
    paragraphs = load_paragraphs(FILE_PATH)

    # 隨機選擇一段
    paragraph_to_rewrite = random.choice(paragraphs)

    # 改寫段落
    rewritten_paragraph = rewrite_paragraph(paragraph_to_rewrite)

    # 更新段落清單
    updated_paragraphs = [
        rewritten_paragraph if para == paragraph_to_rewrite else para
        for para in paragraphs
    ]

    # 將更新內容存回文件
    save_paragraphs(FILE_PATH, updated_paragraphs)

    print("段落已隨機改寫並更新到檔案中！")
    print(f"原始段落：\n{paragraph_to_rewrite}\n")
    print(f"改寫後段落：\n{rewritten_paragraph}")

if __name__ == "__main__":
    main()