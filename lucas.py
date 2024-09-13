
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

# Parâmetros de gravação
FORMAT = pyaudio.paInt16  # Formato de gravação (16 bits por sample)
CHANNELS = 1  # Número de canais (1 para mono, 2 para estéreo)
RATE = 16000  # Taxa de amostragem (16kHz)
CHUNK = 1024  # Tamanho de cada bloco de áudio
RECORD_SECONDS = 10  # Duração da gravação
WAVE_OUTPUT_FILENAME = "temp_audio.wav"  # Nome do arquivo temporário

# Função para capturar áudio usando pyaudio
def capture_audio(filename):
    """
    Função para Capturar o audio
        Args:
            FORMAT = pyaudio.paInt16  # Formato de gravação (16 bits por sample)
            CHANNELS = 1  # Número de canais (1 para mono, 2 para estéreo)
            RATE = 16000  # Taxa de amostragem (16kHz)
            CHUNK = 1024  # Tamanho de cada bloco de áudio
            RECORD_SECONDS = 10  # Duração da gravação
            WAVE_OUTPUT_FILENAME = "temp_audio.wav"  # Nome do arquivo temporário

    """
    audio = pyaudio.PyAudio()

    # Configuração do stream de áudio
    stream = audio.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

    print(f"Gravando por {RECORD_SECONDS} segundos...")

    frames = []

    # Captura áudio por CHUNKS
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Gravação concluída!")

    # Fecha o stream e termina a gravação
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Salva o áudio gravado em um arquivo WAV
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

# Função principal para capturar e transcrever áudio com Whisper
def transcribe_audio():
    """
    Função de transcrição de audio

    Args:
        capture_audi - Função feita com a biblioteca Pyaudio
        whisper.load_model("base") - Carrega o modelo Whisper
        model.transcribe(temp_path, fp16=False) - Transcreve o áudio usando Whisper
        Foi preciso instalar ffmpeg no sistema
    """
    # Caminho temporário para salvar o áudio
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        temp_path = temp_file.name
    
    # Captura o áudio e salva no arquivo temporário
    capture_audio(temp_path)

    # Carrega o modelo Whisper
    model = whisper.load_model("base")
    
    # Transcreve o áudio usando Whisper
    print("Transcrevendo o áudio...")
    result = model.transcribe(temp_path, fp16=False)
    
    
    # Exibe a transcrição
    print("Transcrição: ", result['text'])
    
    # Remove o arquivo temporário
    os.remove(temp_path)




def main():
    # Executa a função de transcrição
    transcribe_audio()
    

if __name__ == "__main__":
    main()
