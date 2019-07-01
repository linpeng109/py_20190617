import win32gui, win32process


class GetHwndFromPid:
    hwnds = []
    pid = ''

    def getHwnds(self):
        print("pid=%s" % self.pid)

        def callback(hwnd, hwnds):
            if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
                _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                if found_pid == self.pid:
                    hwnds.append(hwnd)
                self.hwnds = hwnds
            return True

        win32gui.EnumWindows(callback, self.hwnds)
        return self.hwnds
