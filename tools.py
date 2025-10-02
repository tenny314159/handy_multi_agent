
from camel.agents import ChatAgent
from camel.models import ModelFactory
from camel.types import ModelPlatformType

import os
from dotenv import load_dotenv
import math

load_dotenv()

# 定义系统消息
sys_msg = "你是一个数学大师，擅长各种数学问题。"

# 初始化agent
api_key = os.getenv('QWEN_API_KEY')

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/Qwen2.5-72B-Instruct",
    url='https://api-inference.modelscope.cn/v1/',
    api_key=api_key
)

# 创建agent并添加工具
agent = ChatAgent(
    system_message=sys_msg,
    model=model,
    output_language='中文',
    tools=[]
)

# 定义用户消息
usr_msg = "2的平方根是多少？"

# 发送消息给agent
response = agent.step(usr_msg)
print(response.msgs[0].content)


# 2的平方根是 \(\sqrt{2}\)，大约等于 1.414。

