import time
import subprocess
import random


all_time = 0
try:
	print('程序已经启动，可按Ctrl+C停止程序')
	i = 0
	while True:
		subprocess.run('adb shell input swipe 100 500 100 100')
		sleep_time = 2
		#random.randint(9,16)
		i+=1
		print('正在观看第%s个视频,观看当前视频%s秒'%(i,sleep_time))
		all_time += sleep_time
		time.sleep(sleep_time)
except KeyboardInterrupt as e:
	print('程序已经手动停止！当前运行%s秒'%(all_time))

print('总共用时%s秒'%(all_time))
