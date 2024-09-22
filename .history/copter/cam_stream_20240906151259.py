import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer

async def run(pc, offer_sdp):
    player = MediaPlayer("video=Integrated Camera")