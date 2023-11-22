class ConfigManagerSingleton:
    _instance = None
    config_data = {}

    def __new__(cls):
        if not cls._instance:
            cls._instance = super(ConfigManagerSingleton, cls).__new__(cls)
        return cls._instance

    def set_config(self, key, value):
        self.config_data[key] = value

    def get_config(self, key):
        return self.config_data.get(key, None)

config_manager1 = ConfigManagerSingleton()
config_manager2 = ConfigManagerSingleton()

print(config_manager1 is config_manager2)

config_manager1.set_config("language", "Python")
config_manager2.set_config("theme", "Dark")

print(config_manager1.get_config("language"))
print(config_manager2.get_config("theme"))
print(config_manager1.get_config("theme"))
