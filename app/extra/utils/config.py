from os import environ


class ConfigUtils:

    @staticmethod
    def env(key: str, env_type: type):
        if key not in environ:
            raise TypeError(f"Environ variable is absent {key}")

        val = environ.get(key)

        if env_type == str:
            return val
        elif env_type == bool:
            if val.lower() in ['1', 'true', 'yes', 'y', 'ok', 'on']:
                return True
            if val.lower() in ['0', 'false', 'no', 'n', 'nok', 'off']:
                return False
            raise TypeError("Invalid environment variable '%s' (expected a boolean): '%s'" % (key, val))
        elif env_type == int:
            try:
                return int(val)
            except ValueError:
                raise TypeError("Invalid environment variable '%s' (expected an integer): '%s'" % (key, val))
        else:
            raise TypeError("unknown type")