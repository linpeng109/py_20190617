import subprocess


def getPortFromPid(pid):
    _result = subprocess.Popen("netstat -nao|findstr " + pid, shell=True, stdout=subprocess.PIPE)
    _lines = _result.stdout.readlines()
    ports = []
    for port in _lines:
        _port = str(port).replace(' ', '') \
            .replace('.', '') \
            .replace(':', '') \
            .replace("b'", '') \
            .replace("\\r\\n'", '') \
            .replace('TCP0000', '') \
            .replace(str(pid), '') \
            .replace('00000LISTENING', '')
        if len(_port) <= 10:
            ports.append(_port)
    return ports


# begin = str(port).index('LISTENING') + 8
# print(str(port)[begin:10])
# end = str(port).index('LISTENING')
# ports.append(str(port)[begin:end].strip())


#     if 'LISTENING' in str(_port):
#         ports.append(_port)
# print(ports)
#  return ports

if __name__ == '__main__':
    result = getPortFromPid('13280')
    print(result)
