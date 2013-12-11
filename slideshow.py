#!/usr/bin/env python
#
#  Copyright (c) 2013 Corey Goldberg http://goldb.org/
#  dev: https://github.com/cgoldberg/py-slideshow
#
#  License: GPLv3
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation.


import random
import os

import pyglet


def update_pan(dt):
    sprite.x += dt * 10
    sprite.y += dt * 10


def update_zoom(dt):
    sprite.scale += dt * .025


def update_image(dt):
    img = random.choice(images)
    sprite.image = img
    sprite.scale = get_scale(window, img)
    sprite.x = 0
    sprite.y = 0
    window.clear()


def get_images(input_dir='.'):
    images = []
    for root, dirs, files in os.walk(input_dir, topdown=True):
        for file in sorted(files):
            if file.endswith(('jpg', 'png', 'gif')):
                path = os.path.abspath(os.path.join(root, file))
                img = pyglet.image.load(path)
                images.append(img)
    return images


def get_scale(window, image):
    if image.width > image.height:
        scale = float(window.width) / image.width
    else:
        scale = float(window.height) / image.height
    return scale


window = pyglet.window.Window(fullscreen=True)


@window.event
def on_draw():
    sprite.draw()


if __name__ == '__main__':
    images = get_images('.')
    img = random.choice(images)
    sprite = pyglet.sprite.Sprite(img)
    sprite.scale = get_scale(window, img) 

    pyglet.clock.schedule_interval(update_image, 5.0)
    pyglet.clock.schedule_interval(update_pan, 1/60.0)
    pyglet.clock.schedule_interval(update_zoom, 1/60.0)

    pyglet.app.run()
