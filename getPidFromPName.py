import subprocess

def getPids(pname):
    _result = subprocess.Popen("tasklist|findstr " + pname, shell=True, stdout=subprocess.PIPE)
    _lines = _result.stdout.readlines()
    pidList = set()
    for pid in _lines:
        begin = str(pid).index('surpac2.exe') + 11
        end = str(pid).index('Console')
        pidList.add(str(pid)[begin:end].strip())
    return pidList

# print(getPids("surpac2"))
