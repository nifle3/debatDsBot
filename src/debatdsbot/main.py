from discord import Intents

from config import ds_config
from ds import MyClient 


def main() -> None:
    """
        Entrypoint func
    """

    intents = Intents.default()
    intents.message_content = True

    client = MyClient(intents=intents)
    client.run(ds_config.token)


if __name__ == "__main__":
    main()