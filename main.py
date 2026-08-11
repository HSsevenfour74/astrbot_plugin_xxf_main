import asyncio
import random
import re

from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("helloworld", "YourName", "xxf", "1.0.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""

    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("一键出来")
    async def chulai(self, event: AstrMessageEvent):
        """一键出来"""
        return event.plain_result(f"出来了")
    
    @filter.command("哈哈哈")
    async def hahaha(self, event: AstrMessageEvent):
        """哈哈哈"""
        return event.plain_result(f"CXY钢辰说哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈")

    @filter.regex(r"^出来(\d+)次$")
    async def chulai_loop(self, event: AstrMessageEvent):
        user_name = event.get_sender_name()
        raw_text = event.message_str
        match = re.match(r"^出来(\d+)次$", raw_text)
        if not match:
            yield event.plain_result("格式错误！正确示例：出来x次")
            return
        
        try:
            send_times = int(match.group(1))
        except ValueError:
            yield event.plain_result("请输入数字！如 出来10次")
            return

        # 限制刷屏
        if send_times <= 0 or send_times > 10:
            yield event.plain_result("次数范围 1~10！")
            return
        
        # 循环发送多条独立消息
        for idx in range(send_times):
            yield event.plain_result(f"出来了")
            await asyncio.sleep(0.4)


        
    @filter.command("一键小鸡吧")
    async def xiaojiba(self, event: AstrMessageEvent):
        """一键小鸡吧"""
        yield event.image_result("C:/Users/18019/Desktop/SRWJ/hi.gif")

    @filter.command("随机兑换码")
    async def redemptioncode(self, event: AstrMessageEvent):
        codes = ["IHaveSixSkin","入输来过倒要不万千","JYhWUlbC5d","BackwardsWordEnterNotDo","bem7VEcNAf"]
        i = random.randrange(0, len(codes))
        return event.plain_result(codes[i])


    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
