# Sea-Picro pinout
import board

# KMK specific files
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.RGB import RGB, AnimationModes
from kmk.keys import KC
from kmk.extensions.media_keys import MediaKeys

# Init keyboard
keyboard = KMKKeyboard()

# Mapping IO pin to position in matrix
# Comment lines in / out depending if you are using diodes or not
keyboard.matrix = KeysScanner([board.D21, board.D23, board.D20, board.D22,]) # Without diodes
# keyboard.matrix = KeysScanner([board.D29, board.D28, board.D27, board.D26,]) # With diodes

# Add encoders, RGB, and media key support to keyboard
encoder_handler = EncoderHandler()
rgb_ext = RGB(pixel_pin=board.D7, num_pixels=3, val_limit=255, val_default=64, animation_mode=AnimationModes.RAINBOW,)
media_keys = MediaKeys()
keyboard.modules = [encoder_handler, media_keys, rgb_ext]

# Configure encoder pins
# As the encoder can be placed in multiple spots we don't define which IO the push button
# is mapped to, and instead leave that for the switch matrix definition
encoder_handler.pins = ((board.D9, board.D8, None, False),)

# This is where we control what keys are sent when a switch is pressed
keyboard.keymap = [
    [
        KC.MUTE, KC.MPRV, KC.MPLY, KC.MNXT
    ]
]

# Below configures what happens when the encoder is turned
encoder_handler.map = (((KC.VOLD, KC.VOLU, None),),)

# With everything configured, time to become a keyboard!
if __name__ == '__main__':
    keyboard.go()