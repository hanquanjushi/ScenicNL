import openai

# 设置 OpenAI API 密钥
openai.api_key = "sk-M6BqN0a1wBtUc5FvLsvX4nKmpuxSpoKYFyHYDke3Rw3hHvpA"  # 替换为你的 API 密钥

# 设置 OpenAI API 基础 URL（可选）
openai.api_base = "https://api.qhaigc.net/v1"  # 替换为你的 API Base

def generate_json_response(prompt):
    """
    调用 OpenAI GPT-3.5 API，生成指定格式的 JSON 响应。
    
    参数:
        prompt (str): 用户的输入提示，描述想要生成的内容。
    
    返回:
        dict: GPT-3.5 返回的 JSON 格式响应。
    """
    try:
        # 调用 OpenAI ChatCompletion 接口
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "你是一个只输出 JSON 格式的助手。所有的回答必须是有效的 JSON 格式，不包含多余文字。"},
                {"role": "user", "content": prompt}
            ],
            temperature=0  # 设置为 0 确保生成的输出更具确定性
        )

        # 获取模型返回的内容
        model_output = response['choices'][0]['message']['content']

        # 转换为 Python 字典（如果 JSON 无效会抛出异常）
        json_output = eval(model_output)  # 或使用 json.loads(model_output) 更安全
        return json_output

    except Exception as e:
        print(f"发生错误: {e}")
        return None


# 示例调用
if __name__ == "__main__":
    # 用户需求描述
    user_prompt = "请生成一个包含姓名(name)、年龄(age)、职业(profession)的 JSON 对象。"

    # 调用函数生成 JSON 响应
    result = generate_json_response(user_prompt)

    # 打印结果
    if result:
        print("生成的 JSON 响应:")
        print(result)
    else:
        print("无法生成有效的 JSON 格式输出。")