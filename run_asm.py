'置入带参数的汇编代码执行'
import os
import sys
import time
import ctypes
import struct
import subprocess
import threading
import multiprocessing








def run_asm(asm_code):
    '运行汇编代码'
    # 生成汇编代码
    with open('run_asm.s', 'w') as f:
        f.write(asm_code)
    # 编译汇编代码
    subprocess.call(['nasm', '-f', 'elf64', 'run_asm.s'])
    # 链接汇编代码
    subprocess.call(['ld', '-o', 'run_asm', 'run_asm.o'])
    # 运行汇编代码
    subprocess.call(['./run_asm'])


'''获取返回值'''
def get_ret(asm_code):
    '获取返回值'
    # 生成汇编代码
    with open('get_ret.s', 'w') as f:
        f.write(asm_code)
    # 编译汇编代码
    subprocess.call(['nasm', '-f', 'elf64', 'get_ret.s'])
    # 链接汇编代码
    subprocess.call(['ld', '-o', 'get_ret', 'get_ret.o'])
    # 运行汇编代码
    ret = subprocess.check_output(['./get_ret'])
    return ret