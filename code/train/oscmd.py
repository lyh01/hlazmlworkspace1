import subprocess

def osCmdRun(cmd):
    """
       This function will run commands passed in via [(cmd, parm, parm, ...), (cmd, parm, parm, ...)]
         cmd needs to be full path, e.g., /usr/bin/id, /usr/bin/apt
       Input: cmd needs to be in tuple(s) [("cmd", "parm", "parm"), ("cmd", "parm", "parm")]
      Return: int(return code), b"stdout", b"stderr"
    """

    proc = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    stdout, stderr = proc.communicate()
    return proc.returncode, stdout, stderr
