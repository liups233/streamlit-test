import requests


def run(model, inputs, account_id, api_key):
    API_BASE_URL = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/"
    headers = {"Authorization": f"Bearer {api_key}"}
    input = { "messages": inputs }
    response = requests.post(f"{API_BASE_URL}{model}", headers=headers, json=input)
    return response.json()

def judge_offense(content, account_id, api_key):
    inputs = [
        { "role": "system", "content": "### 定位：语义歧视分析专家\n ### 任务：请对用户输入的句子进行歧视性分析，并用 1 到 5 之间的数字表示其歧视程度。1 表示没有歧视，5 表示极为歧视。\n ###输出 ：只输出数字，不需要额外解释。" },
        { "role": "user", "content": content}
    ]
    output = run("@cf/meta/llama-3.2-3b-instruct", inputs, account_id, api_key)
    return output["result"]["response"]

def improve_sentence(content, account_id, api_key):
    inputs = [
        { "role": "system", "content": "### 定位：语言表述专家\n ### 任务：将输入的歧视性语句换一种方法表述，使表述中不包含歧视语义。" },
        { "role": "user", "content": content}
    ]
    output = run("@cf/meta/llama-3.2-3b-instruct", inputs, account_id, api_key)
    return output["result"]["response"]
