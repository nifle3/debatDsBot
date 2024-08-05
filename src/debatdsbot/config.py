from pydantic_settings import BaseSettings, SettingsConfigDict


class DSConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix='DS_',
        env_file='.env',
        case_sensitive=False,
    )

    hello_message: str
    token: str


ds_config = DSConfig()
