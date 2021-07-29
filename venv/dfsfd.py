


ip = "10.10.20.538"

print(ip.count('.'))

ip_chk = (ip.split('.'))
print(ip_chk)

def ip_scan(np):
    if 0 <= int(np) <= 255:
        return np

try:
    print(len(list(filter(ip_scan, ip_chk))))
    print("In correct format")

except:
    print("Not in correct format")

else:
    print("No errors detected")

finally:
    print("IP scan completed")

