from transformers import pipeline

# 使用 BART 模型
rewriter = pipeline("text2text-generation", model="facebook/bart-large-cnn", device=-1)

def rewrite_paragraph(paragraph):
    """
    使用 BART 模型对段落进行改写，生成自然流畅的段落。
    """
    prompt = f"Rewrite the following text in fluent English:\n\n{paragraph}"
    
    # 调整生成参数
    result = rewriter(
        prompt,
        max_length=150,
        num_return_sequences=1,
        do_sample=True,  # 启用采样以生成多样化的文本
        temperature=0.7,
        top_k=50,
        top_p=0.9
    )
    
    # 提取生成文本
    rewritten_text = result[0]["generated_text"].strip()
    return rewritten_text if rewritten_text else "No valid output generated."

# 测试段落
paragraph_to_rewrite = (
    "The internet has revolutionized the way people communicate and access information. "
    "With just a few clicks, users can connect with others across the globe, share ideas, "
    "and gather knowledge on any topic imaginable. This rapid technological advancement has "
    "opened up countless opportunities but also introduced challenges such as misinformation and privacy concerns."
)

# 改写段落
rewritten_paragraph = rewrite_paragraph(paragraph_to_rewrite)
print("Rewritten paragraph:", rewritten_paragraph)

print(len(rewritten_paragraph) - len(paragraph_to_rewrite))