# -*- coding: utf-8 -*-

class bcolors:
    header = '\033[95m'
    bold = "\033[1m"
    okblue  = '\033[94m'
    okgreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'

def warning(str): 
    print bcolors.bold + bcolors.warning + 'warning: ' + bcolors.end + bcolors.warning + str + bcolors.end 

def error(str): 
    print bcolors.bold + bcolors.fail + 'error: ' + bcolors.end + bcolors.fail + str + bcolors.end 
