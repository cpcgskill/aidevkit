# -*-coding:utf-8 -*-
"""
:创建时间: 2023/8/27 22:53
:作者: 苍之幻灵
:我的主页: https://cpcgskill.com
:Github: https://github.com/cpcgskill
:QQ: 2921251087
:aboutcg: https://www.aboutcg.org/teacher/54335
:bilibili: https://space.bilibili.com/351598127
:爱发电: https://afdian.net/@Phantom_of_the_Cang

"""
from __future__ import unicode_literals, print_function, division

if False:
    pass
import torch
from aidevkit.aos import object_exists, Saver


class MyModule(torch.nn.Module):
    def __init__(self):
        super(MyModule, self).__init__()
        self.linear = torch.nn.Linear(100, 100)
        self.s = 1

    def forward(self, x):
        return self.linear(x)


print('object_exists', object_exists('a_dose_not_exist.pt'))
print('object_exists', object_exists('test.pt'))
saver = Saver(lambda: MyModule(), 'test.pt', 3)
for i in range(100):
    saver.step()
