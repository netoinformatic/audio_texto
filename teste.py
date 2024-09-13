
# $ pip install pyaudio numpy
# pip install --upgrade openai-whisper

import streamlit as st
#from contrato import Vendas
from datetime import datetime, time
from pydantic import ValidationError
#from database import salvar_no_postgres
import pyaudio
import wave
import numpy as np
import whisper
import tempfile
import os

# # Parâmetros de gravação
# FORMAT = pyaudio.paInt16  # Formato de gravação (16 bits por sample)
# CHANNELS = 1  # Número de canais (1 para mono, 2 para estéreo)
# RATE = 16000  # Taxa de amostragem (16kHz)
# CHUNK = 1024  # Tamanho de cada bloco de áudio
# RECORD_SECONDS = 10  # Duração da gravação
# WAVE_OUTPUT_FILENAME = "temp_audio.wav"  # Nome do arquivo temporário

# # Função para capturar áudio usando pyaudio

# audio = pyaudio.PyAudio()

# # Configuração do stream de áudio
# stream = audio.open(format=FORMAT,
#                     channels=CHANNELS,
#                     rate=RATE,
#                     input=True,
#                     frames_per_buffer=CHUNK)

# print(f"Gravando por {RECORD_SECONDS} segundos...")

# frames = []

# # Captura áudio por CHUNKS
# for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#     data = stream.read(CHUNK)
#     frames.append(data)

# print("Gravação concluída!")

# # Fecha o stream e termina a gravação
# stream.stop_stream()
# stream.close()
# audio.terminate()

# with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
#      filename = temp_file.name
# print(filename)
# #filename = "C:\Games\audio.wav"

# # Salva o áudio gravado em um ar
# # quivo WAV
# with wave.open(filename, 'wb') as wf:
#     wf.setnchannels(CHANNELS)
#     wf.setsampwidth(audio.get_sample_size(FORMAT))
#     wf.setframerate(RATE)
#     wf.writeframes(b''.join(frames))

def main():
    
    # Carrega o modelo Whisper
    model = whisper.load_model("base")
    temp_path = "C:/Users/netop/AppData/Local/Temp/tmpc5g26sw6.wav"

    # Transcreve o áudio usando Whisper
    print("Transcrevendo o áudio...")
    result = model.transcribe(temp_path, fp16=False)


    # Exibe a transcrição
    print("Transcrição: ", result['text'])

# Remove o arquivo temporário
#os.remove(temp_path)

if __name__ == "__main__":
    main()