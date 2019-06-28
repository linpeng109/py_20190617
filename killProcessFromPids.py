import os, signal

def kill(pids):
    for pid in pids:
        try:
            os.kill(pid, signal.SIGTERM)
            print('Process(pid=%s) has be killed' % pid)
        except OSError:
            print('no such process(pid=%s)' % pid)
