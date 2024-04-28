from app_v1.modification_audio import save_audio_new
from app_v1.modification_audio import change_speed, change_volume
from app_v1.transcription_audio import transcription_audio
from app_v1.transcription_audio import save_text_to_json

from utils.config import settings
import os
import whisper


def check_existence(audio_name: str, audio_path: str) -> tuple[str, str]:
    while os.path.isfile(audio_path) is False:
        print("\nФайла с таким именем не существует в папке data")
        audio_name = input(
            "Введите название вашего аудиофайла (пример: speech_3.wav): "
        )
        audio_path = settings.get_audio_path(audio_name)

    return (audio_name, audio_path)


def main():
    print("Добро пожаловать в приложение для работы с аудио в формате .WAV!")
    print("Пожалуйста, положите ваш аудиофайл в папку data.")
    audio_name = input(
        "Введите название вашего аудиофайла (пример: speech_3.wav): "
    )
    audio_path = settings.get_audio_path(audio_name)
    audio_name, audio_path = check_existence(audio_name, audio_path)

    while True:
        print(f'\nИмя вашего файла "{audio_name}"')
        print(
            "Выберите один из следующих вариантов (введите номер без точки):"
        )
        print("1. Модификация аудиофайла")
        print("2. Расшифровка аудиофайла в текст")
        print("3. Ввести название другого аудиофайла")
        print("4. Закрыть программу")
        choice = input("Ваш выбор: ")

        match choice:
            case "1":
                print("\nВыберите один из следующих вариантов:")
                print("1. Изменить громкость аудиофайла")
                print("2. Изменить скорость аудиофайла")
                modification_choice = input("Ваш выбор: ")
                match modification_choice:
                    case "1":
                        factor = int(
                            input(
                                "\nВведите число от -50 (тише)"
                                " до 50 (громче): "
                            )
                        )
                        audio_new = change_volume(audio_path, factor)
                        save_audio_new(audio_path, audio_new)
                    case "2":
                        factor = float(
                            input(
                                "\nВведите число от 0 до 1 (медленнее)"
                                " или от 1 до 2 (быстрее): "
                            )
                        )
                        audio_new = change_speed(audio_path, factor)
                        save_audio_new(audio_path, audio_new)
                    case _:
                        print("\nНеверный выбор. Попробуйте еще раз.")
            case "2":
                audio = whisper.load_audio(audio_path)
                text = transcription_audio(audio)
                print(text)
                save_text_to_json(audio_path, text)
            case "3":
                audio_name = input("\nВведите название другого аудиофайла: ")
                audio_path = os.path.join("data", audio_name)
                audio_name, audio_path = check_existence(audio_name,
                                                         audio_path)
            case "4":
                print("\nЗавершение программы.")
                break
            case _:
                print("\nНеверный выбор. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
