import pyaudio
import wave


def beep1():
    # define stream chunk
    chunk = 1024
    # open a wav format music
    f = wave.open(r"/home/patryk/workspace/testApp/res/beep-04.wav","rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    # read data
    data = f.readframes(chunk)
    # paly stream
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)
    # stop stream
    stream.stop_stream()
    stream.close()
    # close PyAudio
    p.terminate()


def beep2():
    # define stream chunk
    chunk = 1024
    # open a wav format music
    f = wave.open(r"/home/patryk/workspace/testApp/res/beep-07.wav","rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    # read data
    data = f.readframes(chunk)
    # paly stream
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)
    # stop stream
    stream.stop_stream()
    stream.close()
    # close PyAudio
    p.terminate()


def beep3():
    # define stream chunk
    chunk = 1024
    # open a wav format music
    f = wave.open(r"/home/patryk/workspace/testApp/res/beep-06.wav","rb")
    # instantiate PyAudio
    p = pyaudio.PyAudio()
    # open stream
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)
    # read data
    data = f.readframes(chunk)
    # paly stream
    while data != '':
        stream.write(data)
        data = f.readframes(chunk)
    # stop stream
    stream.stop_stream()
    stream.close()
    # close PyAudio
    p.terminate()