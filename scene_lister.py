# https://docs.mikeboers.com/pyav/develop/api/frame.html

import av

container = av.open("01. Xmas 1991, Annie Grad Some Xmas 2000 .mp4")

for frame in container.decode(video=0):
    if frame.time > (3 * 60):
        image = frame.to_image()
        import pdb; pdb.set_trace()
        image.save('frames/frame-%04d.jpg' % frame.index)
        break
