#!/usr/bin/env python
#-*- coding:utf-8 -*-


# %(levelno)s: 打印日志级别的数值
# %(levelname)s: 打印日志级别名称
# %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
# %(filename)s: 打印当前执行程序名
# %(funcName)s: 打印日志的当前函数
# %(lineno)d: 打印日志的当前行号
# %(asctime)s: 打印日志的时间
# %(thread)d: 打印线程ID
# %(threadName)s: 打印线程名称
# %(process)d: 打印进程ID
# %(message)s: 打印日志信息

import logging

logging.basicConfig(level=logging.DEBUG, #日志level
					format = '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s,%(lineno)d] %(message)s', #log格式
					datefmt = '%Y-%h-%m %H:%M:%S', #日期格式
					filename = 'log.txt', #文件名
					filemode = 'a'  #追加模式
					)

if __name__ == '__main__':
	logging.info("hello")