import socket
import time

import lights
import tools

try:
    import requests
except ImportError:
    tools.notify("Kodi Hue", "ERROR: Could not import Python requests")


# called from ui.py - def discover_hue_bridge(hue)
def discover():
    bridge_ip = _discover_upnp()

    return bridge_ip

def get_lights(bridge_ip, username):
    return get_lights_by_ids(bridge_ip, username)


def get_lights_by_ids(bridge_ip, username, light_ids=None):
    req = requests.get('http://{}/api/{}/lights'.format(bridge_ip, username))
    res = req.json()

    if light_ids is None:
        light_ids = res.keys()

    if light_ids == ['']:
        return {}

    found = {}
    for light_id in light_ids:
        found[light_id] = lights.Light(bridge_ip, username, light_id,
                                       res[light_id])

    return found


def get_lights_by_group(bridge_ip, username, group_id):
    req = requests.get('http://{}/api/{}/groups/{}'.format(
        bridge_ip, username, group_id))
    res = req.json()

    light_ids = res['lights']
    return get_lights_by_ids(bridge_ip, username, light_ids)


def _discover_upnp():
    port = 1900
    ip = "239.255.255.250"
    bridge_ip = None
    address = (ip, port)
    data = '''M-SEARCH * HTTP/1.1
    HOST: {}:{}
    MAN: ssdp:discover
    MX: 3
    ST: upnp:rootdevice
    '''.format(ip, port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)

    for _ in range(10):
        try:
            sock.sendto(data, address)
            recv, addr = sock.recvfrom(2048)
            if 'IpBridge' in recv and 'description.xml' in recv:
                bridge_ip = recv.split('LOCATION: http://')[1].split(':')[0]
                break
            time.sleep(3)
        except socket.timeout:
            # if the socket times out once, its probably not going to
            # complete at all. fallback to nupnp.
            break

    return bridge_ip
