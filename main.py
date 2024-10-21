import cv2

class Webcam:
    def __init__(self, ip):
        self.ip = ip
        self.cam = cv2.VideoCapture(ip)
        if (self.cam.isOpened() == False):
            print("Error reading video file")
        self.mode = 'webcam'
        self.fourcc = int(cv2.VideoWriter_fourcc(*'MJPG'))
        self.cam_width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cam_height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.fps = self.cam.get(cv2.CAP_PROP_FPS)



    def switch_mode(self):
        if self.mode == 'webcam':
            self.mode = 'video'
        else:
            self.mode = 'webcam'

    def save_video(self, save_path):
        vid = cv2.VideoWriter(save_path, self.fourcc, 20.0, (640, 480))


if __name__ == '__main__':
    # Load camera Cheonan traffic
    ip = 'rtsp://210.99.70.120:1935/live/cctv001.stream'
    webcam = Webcam(ip)
    vid = cv2.VideoWriter('traffic.avi', webcam.fourcc, 10.0, (int(webcam.cam_width), int(webcam.cam_height)), isColor=True)


    while webcam.cam.isOpened():
        _, frame = webcam.cam.read()
        frame = cv2.resize(frame, (640, 480))
        cv2.imshow("Webcam", frame)
        vid.write(frame)
        if cv2.waitKey(1) & 0xFF == 27: # press ESC
            break
        elif cv2.waitKey(1) & 0xFF == 32: # press Space
            pass

    webcam.cam.release()
    vid.release()
    cv2.destroyAllWindows()