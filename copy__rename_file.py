import shutil

def copy_and_rename_file(src_path, dst_path):
    """
    复制文件并重命名
    
    参数:
    src_path (str): 源文件路径
    dst_path (str): 目标文件路径（包含新文件名）
    """
    try:
        shutil.copy2(src_path, dst_path)
        print(f"文件已成功复制并重命名为: {dst_path}")      # the file has been copied and renamed successfully
    except Exception as e:
        print(f"操作失败: {str(e)}")        # operation failed

# 使用示例
if __name__ == "__main__":
    source_file = "original.txt"  # 原始文件名
    destination_file = "copy_renamed.txt"  # 新文件名

    copy_and_rename_file(source_file, destination_file)