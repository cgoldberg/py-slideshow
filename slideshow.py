#!/usr/bin/env python
#
# work in progress
# Corey Goldberg 2013
#


import pyglet


def update_pan(dt):
    sprite.x += dt * 10
    sprite.y += dt * 10

def update_zoom(dt):
    sprite.scale += dt * .025


window = pyglet.window.Window(fullscreen=True, vsync=True)

@window.event
def on_draw():
    window.clear()
    sprite.draw()

img = pyglet.resource.image('images/trollface_hd.jpg')
sprite = pyglet.sprite.Sprite(img)
scale = float(window.width) / img.width
sprite.scale = scale

pyglet.clock.schedule_interval(update_pan, 1/30.0)
pyglet.clock.schedule_interval(update_zoom, 1/30.0)

pyglet.app.run()
