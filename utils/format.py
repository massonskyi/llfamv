import functions as f
import config


class Format:
    @classmethod
    def host(cls, func):  # Add the cls parameter
        return cls.callback(func, {"regex":config.HOST_PATTERN, "is_port": False})

    @classmethod
    def port(cls, func):  # Add the cls parameter
        return cls.callback(func, {"regex":config.PORT_PATTERN, "is_port": True})

    @classmethod
    def callback(cls, func, pattern):
        return f.__format__(func, pattern)
