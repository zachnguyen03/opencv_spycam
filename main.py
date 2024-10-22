import cv2
import argparse

class Webcam:
    def __init__(self, ip, codec):
        self.ip = ip
        self.cam = cv2.VideoCapture(ip)
        if (self.cam.isOpened() == False):
            print("Error reading video file")
        self.mode = 'webcam'
        self.fourcc = int(cv2.VideoWriter_fourcc(*codec))
        self.cam_width = self.cam.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.cam_height = self.cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.fps = self.cam.get(cv2.CAP_PROP_FPS)



    def switch_mode(self):
        if self.mode == 'webcam':
            self.mode = 'record'
        else:
            self.mode = 'webcam'

    def save_video(self, save_path):
        vid = cv2.VideoWriter(save_path, self.fourcc, 20.0, (640, 480))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str, default='rtsp://210.99.70.120:1935/live/cctv001.stream', help='specify IP or RTSP address for VideoCapture')
    parser.add_argument('--fps', type=float, default=20.0, help='specify FPS of output video')
    parser.add_argument('--save_path', type=str, default='out.avi', help='specify destination to save video')
    parser.add_argument('--mode', type=str, default='webcam', help='specify starting mode of SpyCAM')
    parser.add_argument('--fourcc', type=str, default='MJPG', help='specify codec for output video')
    
    args = parser.parse_args()
    
    # Load camera Cheonan traffic
    webcam = Webcam(args.ip, args.fourcc)
    vid = cv2.VideoWriter(args.save_path, webcam.fourcc, args.fps, (int(webcam.cam_width), int(webcam.cam_height)), isColor=True)


    while webcam.cam.isOpened():
        _, frame = webcam.cam.read()
        # frame = cv2.resize(frame, (640, 480))
        cv2.imshow("Webcam", frame)
        if webcam.mode == 'record':
            vid.write(frame)
        if cv2.waitKey(1) & 0xFF == 32:
            webcam.switch_mode()
            print(f"Switched to mode: {webcam.mode}")
        elif cv2.waitKey(1) & 0xFF == 27: # press ESC
            break

    webcam.cam.release()
    vid.release()
    cv2.destroyAllWindows()