from typing import List

from dotenv import load_dotenv
load_dotenv()
import os

import instructor
from pydantic import BaseModel
from openai import OpenAI

prompt = '''你是金融领域文本审查助手，理解长文本中的矛盾和漏洞，擅长识别出文档中的问题句子，或者存在矛盾的问题句子对。
错误类型包括常识错误、数值单位错误、逻辑矛盾、时间矛盾、数值前后矛盾、数据不完整、计算错误、语句重复。
请仔细分析下面的文本，如果存在上述错误之一，则指出出错的句子，如果没有，则不用返回。

＃示例
合同签订日期：2023-07-32
合同公告日期：2023-07-06 00:00:00

分析：上述文本存在常识错误，日期超过了31。

返回：合同签订日期：2023-07-32
---
#待判断文本

'''


class Result(BaseModel):
    sent: str


client = OpenAI()

def validate(context):
    completion = client.chat.completions.create(
        model=os.environ['MODEL'],
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": context},
        ],
    )
    
    return completion.choices[0].message.content
