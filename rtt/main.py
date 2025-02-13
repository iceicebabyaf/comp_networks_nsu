import subprocess
import csv


def ping(server, count=1, wait_sec=1):

    cmd = "ping -c {} -W {} {}".format(count, wait_sec, server).split(' ')

    try:
        output = subprocess.check_output(cmd).decode().strip()
        lines = output.split("\n")
        timing = lines[-1].split()[3].split('/')
        arr = [server, timing[1]]
        return arr

    except Exception as e:
        print(e)
        return None


file = open("/Users/xd/Documents/GitHub/comp_networks_nsu/rtt/output.csv", "w")

writer = csv.writer(file)
writer.writerow(['webSite', 'rtt'])

data = ["google.com", "mail.google.com", "yandex.com", "youtube.com", "mail.com", "apple.com", "logitech.com", "habr.com", "github.com", "stackoverflow.com"]
dataAndRtt = []

for server in data:
    name = ping(server)[0]
    rtt = ping(server)[1]
    writer.writerow([name, float(rtt)])
