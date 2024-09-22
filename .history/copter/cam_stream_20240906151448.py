import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer

async def run(pc, offer_sdp):
    player = MediaPlayer("video=Integrated Camera")
    @pc.on("datachannel")
    def on_datachannel(channel):
        print("Data channel is available")
    
    pc.addTrack(player.video)
    offer = RTCSessionDescription(sdp=offer_sdp, type="offer")
    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)