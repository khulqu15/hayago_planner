import asyncio
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer

async def run(pc, offer_sdp):
    
    player = MediaPlayer('video=USB Camera', format='dshow', options={
        'video_size': '640x480'
    })
    @pc.on("datachannel")
    def on_datachannel(channel):
        print("Data channel is available")
    
    pc.addTrack(player.video)
    offer = RTCSessionDescription(sdp=offer_sdp, type="offer")
    await pc.setRemoteDescription(offer)
    answer = await pc.createAnswer()
    await pc.setLocalDescription(answer)
    return pc.localDescription.sdp

async def main():
    pc = RTCPeerConnection()
    
    offer_sdp = """v=0
    o=- 4611731065146434605 2 IN IP4 127.0.0.1
    s=- 
    t=0 0
    a=group:BUNDLE 0
    a=msid-semantic: WMS
    m=video 9 UDP/TLS/RTP/SAVPF 96
    c=IN IP4 0.0.0.0
    a=rtcp:9 IN IP4 0.0.0.0
    a=ice-ufrag:F7gI
    a=ice-pwd:x9cml/YzichV2+XlhiMu8g
    a=ice-options:trickle
    a=fingerprint:sha-256 3A:59:0D:2C:F8:34:D7:6A:A2:67:9B:94:79:BA:DE:D9:57:DB:12:AF:50:1D:A9:F3:5D:D7:E7:1B:73:5D:91
    a=setup:actpass
    a=mid:0
    a=sendrecv
    a=rtcp-mux
    a=rtpmap:96 VP8/90000
    a=ssrc:2126108489 cname:9vp5tsmnIbsn
    """
    
    answer_sdp = await run(pc, offer_sdp)
    print("Answer SDP:\n", answer_sdp)
    
asyncio.run(main())