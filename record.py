import pyaudio
import wave
import datetime

time_now = datetime.datetime.now().strftime("%H_%M_%S")

print(time_now)
filename = f"Recorded at {time_now}.wav"

chunk = 1024

FORMAT = pyaudio.paInt16

channels = 1

sample_rate = 44100

record_seconds = 5

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = channels, 
                rate = sample_rate,
                input= True,
                output = True,
                frames_per_buffer=chunk
)

frames =[]

print('recording...')

for i in range(int(44100 / chunk * record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

print('Finished recording.')

stream.stop_stream()

stream.close()

p.terminate()

wf = wave.open(filename, "wb")

wf.setnchannels(channels)

wf.setsampwidth(p.get_sample_size(FORMAT))

wf.setframerate(sample_rate)

wf.writeframes(b"".join(frames))

wf.close()
