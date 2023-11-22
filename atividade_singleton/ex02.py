class SingletonServer:
    _instance = None
    server_list = []

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(SingletonServer, cls).__new__(cls)
        return cls._instance

    @staticmethod
    def add_server(server_name):
        if server_name.startswith("http://") or server_name.startswith("https://"):
            if server_name not in SingletonServer.server_list:
                SingletonServer.server_list.append(server_name)
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def download_http_servers():
        return [server for server in SingletonServer.server_list if server.startswith("http://")]

    @staticmethod
    def download_https_servers():
        return [server for server in SingletonServer.server_list if server.startswith("https://")]


singleton_instance = SingletonServer()

print(singleton_instance.add_server("https://mail.google.com/"))
print(singleton_instance.add_server("https://classroom.google.com/"))

http_servers = singleton_instance.download_http_servers()
https_servers = singleton_instance.download_https_servers()

print("Servidores HTTP:", http_servers)
print("Servidores HTTPS:", https_servers)
