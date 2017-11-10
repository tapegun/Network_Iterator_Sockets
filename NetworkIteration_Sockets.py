import subprocess, socket, urllib2, sys
class pymap:
    def __init__(self, host):
        self.host = host
        socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock = socket1



################################################################################
################################################################################
    # def getYourIp(self):
    #     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     s.connect(("8.8.8.8", 80))
    #     thing = s.getsockname()[0]
    #     s.close()
    #     return(s.getsockname()[0])

################################################################################
################################################################################



################################################################################
################################################################################

    def getip(self):
        if self.host == None:
            print ("Specify a host first.")
        else:
            return socket.gethostbyname(self.host)

################################################################################
################################################################################

    def scanport(self, port1):
        self.sock.settimeout(.0001)
        try:
            self.sock.connect((self.host, port1))
            return 1
        except:
            return 0

################################################################################
################################################################################

    def scanports(self, start, end):
        ports = []
        for i in range(start, end + 1):  # 49151
            try:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if (self.scanport(i) == 1):
                    ports.append(i)
                    self.sock.close()
            except:
                pass
        return ports

################################################################################
################################################################################

    def traceroute(self):
        if self.host == None:
            print ("Specify a host first.")

        else:
            proc=subprocess.Popen(('tracert', self.host), shell=True, stdout=subprocess.PIPE)
            output=proc.communicate()[0]
            return output

################################################################################
################################################################################

    def getsource(self, url):
        page = urllib2.urlopen(url)
        return page.read()

################################################################################
################################################################################

x = pymap("10.103.171.115")
print (x.scanports(0, 65535))
# print (x.scanport(5000))