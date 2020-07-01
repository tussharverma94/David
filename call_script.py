import subprocess


class callpy:
    def __init__(self):
        self.path = "C:\\Users\\tussh\\PycharmProjects\\spaceinvader\\main.py"

    def call_python_file(self):
        subprocess.call(["python", "{}".format(self.path)])

    def call_python_shell(self, command):
        return subprocess.check_output(command, shell=True)

    def return_ip(self):
        output = self.call_python_shell('ipconfig')
        # print(output.decode('utf-8'))
        str_dup = b'Wireless LAN adapter Wi-Fi:'
        str_dup2 = b'Wireless LAN adapter Local Area Connection'
        str_ip4 = b'IPv4 Address'
        output = output[output.find(str_dup):]
        output = output[:output.find(str_dup2)]
        output = output[output.find(str_ip4):]
        output = output[36:47]
        ip_adress = output.decode('utf-8')
        return ip_adress

"""
c= callpy()
output = c.call_python_shell('ipconfig')
print(output.decode('utf-8'))
str_dup = b'Wireless LAN adapter Wi-Fi:'
str_dup2 = b'Wireless LAN adapter Local Area Connection'
str_ip4 = b'IPv4 Address'
# len_ = len(output)
# print(len_)
# lower_ind = output.find(str_dup)
# print(lower_ind)
# print(type(output.find(str_dup, 0, len(output))))
output = output[output.find(str_dup):]
output = output[:output.find(str_dup2)]
output = output[output.find(str_ip4):]
output = output[36:47]
ip_adress = output.decode('utf-8')
print(ip_adress)
"""