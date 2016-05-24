import netifaces as ni


def get_ip():
    ni.ifaddresses('utun0')
    ip = ni.ifaddresses('utun0')[2][0]['addr']
    return ip

print(get_ip()) ##если надо получить все интерфейсы ni.interfaces()