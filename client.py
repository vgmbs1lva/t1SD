import zmq
import threading
import time

class VideoConferenceClient:
    def __init__(self, broker_ip):
        self.context = zmq.Context()

        # Sockets PUB para enviar dados
        self.audio_pub = self.context.socket(zmq.PUB)
        self.video_pub = self.context.socket(zmq.PUB)
        self.text_pub = self.context.socket(zmq.PUB)

        self.audio_pub.connect(f"tcp://{broker_ip}:5556")
        self.video_pub.connect(f"tcp://{broker_ip}:5558")
        self.text_pub.connect(f"tcp://{broker_ip}:5560")

        # Sockets SUB para receber dados
        self.audio_sub = self.context.socket(zmq.SUB)
        self.video_sub = self.context.socket(zmq.SUB)
        self.text_sub = self.context.socket(zmq.SUB)

        self.audio_sub.connect(f"tcp://{broker_ip}:5557")
        self.video_sub.connect(f"tcp://{broker_ip}:5559")
        self.text_sub.connect(f"tcp://{broker_ip}:5561")

        self.audio_sub.setsockopt_string(zmq.SUBSCRIBE, "")
        self.video_sub.setsockopt_string(zmq.SUBSCRIBE, "")
        self.text_sub.setsockopt_string(zmq.SUBSCRIBE, "")

    def send_audio(self, audio_data):
        self.audio_pub.send(audio_data)

    def send_video(self, video_data):
        self.video_pub.send(video_data)

    def send_text(self, text_message):
        self.text_pub.send_string(text_message)

    def receive_audio(self):
        while True:
            audio_data = self.audio_sub.recv()
            print(f"Recebido áudio: {audio_data}")

    def receive_video(self):
        while True:
            video_data = self.video_sub.recv()
            print(f"Recebido vídeo: {video_data}")

    def receive_text(self):
        while True:
            text_message = self.text_sub.recv_string()
            print(f"Recebido texto: {text_message}")

    def start_receiving(self):
        threading.Thread(target=self.receive_audio).start()
        threading.Thread(target=self.receive_video).start()
        threading.Thread(target=self.receive_text).start()

if __name__ == "__main__":
    broker_ip = "189.100.68.70"  # Use o endereço IP interno para testes locais
    client = VideoConferenceClient(broker_ip=broker_ip)
    client.start_receiving()
    # Código adicional para capturar e enviar áudio/vídeo/texto
