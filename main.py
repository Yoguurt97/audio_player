import os
import pyglet

#song = pyglet.media.load('test2.wav')
#song.play()
#pyglet.app.run()

def wav_to_ogg(filename):
    os.system('ffmpeg -i {0}.wav {0}_final.ogg'.format(filename))
    print('Файл {0}_final.ogg сохранен.'.format(filename))
def wav_to_mp3(filename):
    os.system('ffmpeg -i {0}.wav -vn -ar 44100 -ac 2 -ab 192 -f mp3 {0}_final.mp3'.format(filename))
    print('Файл {0}_final.mp3 сохранен.'.format(filename))
def mp3_to_ogg(filename):
    os.system('ffmpeg -i {0}.mp3 -ab 64k {0}_final.ogg'.format(filename))
    print('Файл {0}_final.ogg сохранен.'.format(filename))
def mp3_to_wav(filename):
    os.system('ffmpeg -i {0}.mp3 {0}_final.wav'.format(filename))
    print('Файл {0}_final.wav сохранен.'.format(filename))
def ogg_to_mp3(filename):
    os.system('ffmpeg -i {0}.ogg {0}_final.mp3'.format(filename))
    print('Файл {0}_final.mp3 сохранен.'.format(filename))
def ogg_to_wav(filename):
    os.system('ffmpeg -i {0}.ogg {0}_final.wav'.format(filename))
    print('Файл {0}_final.wav сохранен.'.format(filename))

def main():
    while True:
        otvet = input('Проигрыватель/Конвертер: ')
        otvet = otvet.lower()
        if otvet == 'проигрыватель' or otvet == '1':
            print(1)
        elif otvet == 'конвертер' or otvet == '2':
            while True:
                filename = input('Укажите название файла(без формата): ')
                format = input('Укажите формат файла(mp3, wav, ogg): ')
                try:
                    with open('{0}.{1}'.format(filename, format), 'r') as f:
                        pass
                except FileNotFoundError:
                    print('Данный файл не найден, или указан не верный формат')
                    continue
                final = input('В какой формат конвертировать(mp3, wav, ogg): ')
                # Из вав в мп3
                if final == 'mp3' and format == 'wav':
                    wav_to_mp3(filename)
                # Из мп3 в огг
                elif final == 'mp3' and format == 'ogg':
                    ogg_to_mp3(filename)
                # Из огг в мп3
                elif final == 'ogg' and format == 'mp3':
                    mp3_to_ogg(filename)
                # Из ogg B wav
                elif final == 'wav' and format == 'ogg':
                    ogg_to_wav(filename)
                # Из wav B ogg
                elif final == 'ogg' and format == 'wav':
                    wav_to_ogg(filename)
                elif final == 'wav' and format == 'mp3':
                    mp3_to_wav(filename)
                else:
                    print('Указан не верный формат')
        else:
            print('Не правильная команда')

if __name__ == "__main__":
    main()