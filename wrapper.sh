#!/bin/bash
rm -rf ./frames
rm -rf ./ascii_frames
mkdir ./frames
mkdir ./ascii_frames

ffmpeg -i $1 frames/frame_%06d.png
find frames -name "*.png" -exec asciify/asciify.py {} 150 ./ascii_frames/ \;
