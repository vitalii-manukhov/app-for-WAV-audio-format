from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    AUDIO_PATH: str = ''
    WHISPER_DOWNLOAD_PATH: str = ''

    model_config = SettingsConfigDict(env_file=".env",
                                      env_file_encoding="utf-8",
                                      extra="allow")

    def get_audio_path(self, audio_name: str):
        return self.AUDIO_PATH + audio_name


settings = Settings()
