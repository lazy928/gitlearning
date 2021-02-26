# -*- coding: utf-8 -*-

# timer

# from datetime import datetime
# from threading import Timer
# import time
#
# # 定时任务
# def task():
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#
# def timedTask():
#     '''
#     第一个参数：延迟多长时间执行任务（秒）
#     第二个参数：要执行的函数
#     第三个参数：调用函数的参数（tuple）
#     '''
#     Timer(5, task, ()).start()
#
# while True:
#     timedTask()
#     time.sleep(5)

# sched 模块 之执行一次，可在main 下添加while True 或者添加调度任务在timeTask 中即可

# from datetime import datetime
# import sched
# import time
#
# def timeTask():
#     # 初始化sched 模块的scheduler 类，传入（time.time, time.sleep）这两个参数
#     scheduler = sched.scheduler(time.time, time.sleep)
#     # 增加调度任务，enter(睡眠时间，执行级别，执行函数)
#     scheduler.enter(5, 1, task)
#     # 执行任务
#     scheduler.run()
#
# # 定时任务
# def task():
#     print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#
# if __name__ == '__main__':
#     timeTask()

# 根据上面的另一种写法
import schedule
import time

def hello():
    print('hello')

def Timer():
    schedule.every().day.at("09:00").do(hello)
    schedule.every().day.at("18:00").do(hello)

    while True:
        schedule.run_pending()
        time.sleep('60')

Timer()