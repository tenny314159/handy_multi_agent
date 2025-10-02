
from camel.toolkits import FunctionTool
import math
from camel.agents import ChatAgent
import os
from camel.models import ModelFactory
from camel.types import ModelPlatformType


def calculate_sqrt(x: float) -> float:
    r"""计算一个实数的平方根。

    Args:
        x (float): 需要计算平方根的数字。

    Returns:
        float: 输入数字的平方根。
    """
    return math.sqrt(x)

# 用 FunctionTool 包装该函数
sqrt_tool = FunctionTool(calculate_sqrt)

print(sqrt_tool.get_function_name())

# >>> calculate_sqrt

print(sqrt_tool.get_function_description())

# 计算一个实数的平方根。

# 定义系统消息
sys_msg = "你是一个数学大师，擅长各种数学问题。当你遇到数学问题的时候，你要调用工具，将工具计算的结果作为答案"

api_key = os.getenv('QWEN_API_KEY')

model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI_COMPATIBLE_MODEL,
    model_type="Qwen/Qwen2.5-72B-Instruct",
    url='https://api-inference.modelscope.cn/v1/',
    api_key=api_key
)

tool_agent = ChatAgent(
    tools=[sqrt_tool],
    system_message=sys_msg,
    model=model,
    output_language="中文")

# 定义用户消息
usr_msg = "2的平方根是多少？"

# 重新发送消息给toolagent
response = tool_agent.step(usr_msg)
print(response.msgs[0].content)

# Traceback (most recent call last):
#   File "D:\pythoncode\learn\a\handy_multi_agent\tools2.py", line 37, in <module>
#     model = ModelFactory.create(
#   File "D:\anaconda3\envs\portfolio\lib\site-packages\camel\models\model_factory.py", line 157, in create
#     return model_class(
#   File "D:\anaconda3\envs\portfolio\lib\site-packages\camel\models\openai_compatible_model.py", line 70, in __init__
#     self._client = OpenAI(
#   File "D:\anaconda3\envs\portfolio\lib\site-packages\openai\_client.py", line 130, in __init__
#     raise OpenAIError(
# openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable

# >> >
# 2
# 的平方根是1
# .4142135623730951。