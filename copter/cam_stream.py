import cv2
import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.mediastreams import VideoStreamTrack
from av.video.frame import VideoFrame

class StreamTrack(VideoStreamTrack):
    def __init__(self, video_source=0):
        super().__init__()