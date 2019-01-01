# Home Video Processing

My scripts for organizing home videos.

## For Users

Open `index.html` in your web browser. This contains descriptions of each scene
and allows you to jump directly to any scene in the videos.

The videos themselves are stored in `data/originals`.

## For Developers

1. Extract scene start and end times from original videos and generate data
  template.
2. Generate thumbnails.
3. Generate `index.html` from `index.json`.

### Requirements
- Python 3
- Numpy
- PyAV
- Pillow
- Mako
- ffmpeg

### Notes

Use [media fragment](https://www.w3.org/TR/media-frags/) to specify video
segments: `#t=start,end`.
