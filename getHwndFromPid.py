import win32gui, win32process


def get_hwnds(pid):
    """return a list of window handlers based on it process id"""

    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
                print(win32gui.GetWindowText(hwnd))
        return True

    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return hwnds


result = get_hwnds(15304)

print(result[0])
