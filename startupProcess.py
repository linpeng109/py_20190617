import subprocess


class StartupProcess:
    def start(self):
        # cmd = "C:/Program Files (x86)/GEOVIA/Surpac/681/nt_i386/bin/surpac2.exe"
        cmd = "C:/Program Files (x86)/GEOVIA/Surpac/69/nt_i386/bin/surpac2.exe"
        subprocess.Popen(cmd)
        self.cmd = cmd


