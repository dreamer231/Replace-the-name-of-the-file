import pandas as pd

def read_excel_column(file_path, sheet_name, column_name=None, column_index=None):
    """
    读取Excel文件中指定列的数据并返回为列表
    
    参数:
    file_path (str): Excel文件路径
    sheet_name (str): 工作表名称
    column_name (str, 可选): 列名（如'A'或'列标题'）
    column_index (int, 可选): 列索引（从0开始）
    
    返回:
    list: 包含指定列数据的列表
    """
    try:
        # 读取Excel文件
        df = pd.read_excel(file_path, sheet_name=sheet_name)
        
        # 根据列名或列索引选择列
        if column_name:
            # 如果column_name是字母（如'A'），则转换为列索引
            if isinstance(column_name, str) and column_name.isalpha():
                column_index = ord(column_name.upper()) - ord('A')
                column_data = df.iloc[:, column_index]
            else:
                # 否则视为列标题
                column_data = df[column_name]
        elif column_index is not None:
            column_data = df.iloc[:, column_index]
        else:
            raise ValueError("必须提供column_name或column_index参数")
        
        # 转换为列表并返回
        return column_data.tolist()
    
    except Exception as e:
        print(f"读取Excel文件时出错: {str(e)}")
        return []

# 使用示例
if __name__ == "__main__":
    # 示例1: 通过列名（字母）读取
    data_a = read_excel_column("智网2301班名单.xlsx", "Sheet1", column_name="B")
    print(f"A列数据: {data_a}")
    
    # 示例2: 通过列标题读取
    data_name = read_excel_column("智网2301班名单.xlsx", "Sheet1", column_name="姓名")
    print(f"姓名列数据: {data_name}")
    
    # 示例3: 通过列索引读取
    data_index = read_excel_column("智网2301班名单.xlsx", "Sheet1", column_index=1)
    print(f"第3列数据: {data_index}")