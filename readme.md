# Term animation
Very simple wrapper around ffmpeg and asciify.   
Basically this script will extract every frame from a video, it will then change each frame into ascii using asciify.  
Then you can use run_vid.py to make it play in your terminal.  
Makes for something cool to show friends.  

Asciify : https://github.com/RameshAditya/asciify  
FFMPEG: https://ffmpeg.org/  

*You need ffmpeg for this, asciify is included but not necessarily up to date.*

# Usage
```bash
./wrapper.sh video.mp4
# this will do the whole thing, it may take 1 or 2 minutes if the video is small (which it should be).
python run_vid.py
# this should launch the animation in the current terminal.
```

If you want a clearer picture, you can play with the resolution of the ascii images in wrapper.sh.  
You can also lower your font size in the target terminal so every characters looks like a pixel.  
