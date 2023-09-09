# aikit

一些ai开发过程中使用到的工具模块

- [aikit](#aikit)
    - [安装](#安装)
    - [使用](#使用)
        - [aos](#aos)

## 安装

```commandline
git clone git@github.com:cpcgskill/aikit.git
```

## 使用

### aos

```python
import os

# 设置以下环境变量为腾讯云cos的配置

os.environ['COS_Region'] = 'ap-hongkong'
os.environ['COS_SecretId'] = ''
os.environ['COS_SecretKey'] = ' '
os.environ['COS_Bucket'] = ' '

import torch
from aidevkit.aos import Saver


class MyModule(torch.nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.linear = torch.nn.Linear(10, 10)
        self.s = 1

    def forward(self, x):
        return self.linear(x)


saver = Saver(lambda: MyModule(), 'test.pt', 3)
for i in range(10):
    saver.step()
```

