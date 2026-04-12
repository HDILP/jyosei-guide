import os

def clean_md_properly(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                new_lines = []
                for line in lines:
                    # 精确匹配“原文：”所在行
                    if line.strip() == "原文：":
                        break
                    new_lines.append(line)
                
                # 核心防错逻辑：
                # 1. "".join(new_lines) 将前面的内容拼回去
                # 2. .rstrip() 删掉末尾【所有】多余的空行和空格
                # 3. + "\n" 确保文件以【且仅以】一个换行符结尾（符合 MD047，解决 MD012）
                final_content = "".join(new_lines).rstrip() + "\n"

                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(final_content)
                print(f"Successfully cleaned: {file_path}")

if __name__ == "__main__":
    # 在 content/ 目录下运行
    clean_md_properly('.')