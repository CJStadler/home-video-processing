# https://docs.mikeboers.com/pyav/develop/api/frame.html

import av

container = av.open("data/test.mp4")

for frame in container.decode(video=0):
    image = frame.to_image()
    import pdb; pdb.set_trace()
    image.save('frames/frame-%04d.jpg' % frame.index)
    break
