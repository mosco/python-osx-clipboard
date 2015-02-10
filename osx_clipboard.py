import subprocess

def copy(s):
    subp = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    subp.communicate(s)

def paste():
    subp = subprocess.Popen(['pbpaste'], stdout=subprocess.PIPE)
    return subp.communicate()[0]
