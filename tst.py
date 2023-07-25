import ffmpy

ff = ffmpy.FFmpeg(
    inputs={'508.ogg': None},
    outputs={'508.wav': None}
)
ff.run()