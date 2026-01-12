import os
from PIL import Image, ImageDraw, ImageFont
import datetime



# 定义输入和输出文件夹
# 從外部輸出
input_folder = r"C:\Users\eric\Desktop\aff_folder\speed_test"
output_folder = r"C:\Users\eric\Desktop\aff_folder\hsiav.github.io\image\speed_test"


new_date = datetime.datetime.now()
new_date = new_date +  datetime.timedelta(hours=13)
new_date = new_date.strftime('%Y%m%d')

# 确保输出文件夹存在
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 水印文本
watermark_text = f"Powered by VPN universe on {new_date}"

# 支持的图片格式
valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

# 遍历输入文件夹中的所有文件
for filename in os.listdir(input_folder):
    # 检查文件扩展名
    try:
        if any(filename.lower().endswith(ext) for ext in valid_extensions):
            # 打开图片
            with Image.open(os.path.join(input_folder, filename)) as img:
                # 如果图像不是RGBA模式，转换为RGBA
                    if img.mode != 'RGBA':
                        img = img.convert('RGBA')
                    
                    # 创建一个新的透明图层用于水印
                    watermark = Image.new('RGBA', img.size, (0,0,0,0))
                    
                    # 创建绘图对象
                    draw = ImageDraw.Draw(watermark)
                    
                    # 获取图片尺寸
                    width, height = img.size
                    
                    # 设置字体（请确保此字体文件存在，或使用系统默认字体）
                    font = ImageFont.truetype("arial.ttf", 50)
                    
                    # 获取文本尺寸
                    text_width, text_height = draw.textsize(watermark_text, font)
                    
                    # 计算文本位置（右下角）
                    x = width - text_width - 10
                    y = height - text_height - 10
                    
                    # 添加水印
                    draw.text((x, y), watermark_text, font=font, fill=(128, 128, 128, 128))
                    
                    # 将水印图层与原图合并
                    out = Image.alpha_composite(img, watermark)
                    
                    # 如果原图不是RGBA，转换回原来的模式
                    if img.mode != 'RGBA':
                        out = out.convert(img.mode)
                    
                    # 保存新图片
                    output_path = os.path.join(output_folder, f"{filename}")
                    out.save(output_path)
                    
                    print(f"Processed: {filename}")
    except:
        continue

print("All images have been processed and saved with watermarks.")