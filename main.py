tryk = 0
tid = 0
mode = 0
ab_tryk = 0
ab_tid = 0
ab_mode = 0
def tøm_vand():
    wuKong.set_motor_speed(wuKong.MotorList.M2, 100)
    basic.pause(18000)
    wuKong.stop_motor(wuKong.MotorList.M2)
def vask_3():
    for index in range(3):
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
        basic.pause(18000)
    wuKong.stop_motor(wuKong.MotorList.M1)
    wuKong.set_light_mode(wuKong.LightMode.OFF)
def spin_1():
    wuKong.set_all_motor(20, 100)
    basic.pause(9000)
    wuKong.set_all_motor(32, 100)
    basic.pause(9000)
    wuKong.set_all_motor(44, 100)
    basic.pause(9000)
    wuKong.set_all_motor(60, 100)
    basic.pause(140000)
    wuKong.set_all_motor(40, 100)
    basic.pause(5000)
    wuKong.set_all_motor(32, 100)
    basic.pause(3000)
    wuKong.set_all_motor(20, 100)
    basic.pause(3000)
    wuKong.set_all_motor(15.2, 100)
    basic.pause(3000)
    wuKong.stop_motor(wuKong.MotorList.M1)
def spin_5():
    wuKong.set_all_motor(20, 100)
    basic.pause(9000)
    wuKong.set_all_motor(32, 100)
    basic.pause(120000)
    wuKong.set_all_motor(20, 100)
    basic.pause(5000)
    wuKong.set_all_motor(15.2, 100)
    basic.pause(3000)
    wuKong.stop_motor(wuKong.MotorList.M1)
def vask_5():
    for index2 in range(2):
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
        basic.pause(18000)
    wuKong.stop_motor(wuKong.MotorList.M1)
    wuKong.set_light_mode(wuKong.LightMode.OFF)

def on_button_pressed_a():
    global tryk, tid, mode
    if tryk == 0:
        tryk = 1
        tid = 0
    if mode == 1:
        music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Miele")
        basic.show_string("Bomuld rpm 1600")
        basic.pause(100)
    elif mode == 2:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Kort rpm 1200")
        basic.pause(100)
    elif mode == 3:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Forvask rpm 1600")
        basic.pause(100)
    elif mode == 4:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Finvask rpm 800")
        basic.pause(100)
    elif mode == 5:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Mørkt rpm 1200")
        basic.pause(100)
    elif mode == 6:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Skjorter rpm 600")
        basic.pause(100)
    elif mode == 7:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Spin rpm 1600")
        basic.pause(100)
    elif mode == 8:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Bomuld kort rpm 1600")
        basic.pause(100)
    elif mode == 9:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Forvask kort rpm 1600")
        basic.pause(100)
    elif mode == 10:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Finvask kort 800rpm")
        basic.pause(100)
    elif mode == 11:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Mørkt kort rpm 1200")
        basic.pause(100)
    elif mode == 12:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Skjorter kort rpm 600")
        basic.pause(100)
    elif mode == 13:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Bomuld rpm 1200")
        basic.pause(100)
    elif mode == 14:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Kort rpm 800")
        basic.pause(100)
    elif mode == 15:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Forvask rpm 1200")
        basic.pause(100)
    elif mode == 16:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Finvask rpm 600")
        basic.pause(100)
    elif mode == 17:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Mørkt rpm 800")
        basic.pause(100)
    elif mode == 18:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Spin rpm 1200")
        basic.pause(100)
    elif mode == 19:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Bomuld rpm 800")
        basic.pause(100)
    elif mode == 20:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Kort rpm 600")
        basic.pause(100)
    elif mode == 21:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Forvask rpm 800")
        basic.pause(100)
    elif mode == 22:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Mørkt rpm 600")
        basic.pause(100)
    elif mode == 23:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Spin rpm 800")
        basic.pause(100)
    elif mode == 24:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Bomuld rpm 600")
        basic.pause(100)
    elif mode == 25:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Forvask rpm 600")
        basic.pause(100)
    elif mode == 26:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        basic.show_string("Spin rpm 600")
        basic.pause(100)
    if mode > 26:
        mode = 0
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

def spin_4():
    wuKong.set_all_motor(20, 100)
    basic.pause(9000)
    wuKong.set_all_motor(32, 100)
    basic.pause(9000)
    wuKong.set_all_motor(44, 100)
    basic.pause(9000)
    wuKong.set_all_motor(80, 100)
    basic.pause(120000)
    wuKong.set_all_motor(44, 100)
    basic.pause(5000)
    wuKong.set_all_motor(32, 100)
    basic.pause(3000)
    wuKong.set_all_motor(20, 100)
    basic.pause(3000)
    wuKong.set_all_motor(15.2, 100)
    basic.pause(3000)
    wuKong.stop_motor(wuKong.MotorList.M1)
def vask_2():
    for index3 in range(3):
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
        basic.pause(18000)
    wuKong.stop_motor(wuKong.MotorList.M1)
    wuKong.set_light_mode(wuKong.LightMode.OFF)
def vask_4():
    for index4 in range(2):
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
        basic.pause(18000)
    wuKong.stop_motor(wuKong.MotorList.M1)
    wuKong.set_light_mode(wuKong.LightMode.OFF)
def vask_1():
    wuKong.set_light_mode(wuKong.LightMode.BREATH)
    for index5 in range(4):
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
        basic.pause(18000)
        wuKong.stop_motor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
        basic.pause(18000)
    wuKong.stop_motor(wuKong.MotorList.M1)
    wuKong.set_light_mode(wuKong.LightMode.OFF)

def on_button_pressed_ab():
    global ab_tryk, ab_tid
    serial.write_line("knap a+b trykkes")
    serial.write_line("ab_tryk: " + ("" + str(ab_tryk)))
    serial.write_line("ab_tid: " + ("" + str(ab_tid)))
    ab_tryk = 1
    ab_tid = 0
    serial.write_line("ab_tryk efter +1: " + ("" + str(ab_tryk)))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def spin_2():
    wuKong.set_all_motor(20, 100)
    basic.pause(9000)
    wuKong.set_all_motor(32, 100)
    basic.pause(9000)
    wuKong.set_all_motor(44, 100)
    basic.pause(9000)
    wuKong.set_all_motor(80, 100)
    basic.pause(160000)
    wuKong.set_all_motor(44, 100)
    basic.pause(5000)
    wuKong.set_all_motor(32, 100)
    basic.pause(3000)
    wuKong.set_all_motor(20, 100)
    basic.pause(3000)
    wuKong.set_all_motor(15.2, 100)
    basic.pause(3000)
    wuKong.stop_motor(wuKong.MotorList.M1)

def on_button_pressed_b():
    serial.write_line("der trykkes på b")
    music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.UNTIL_DONE)
    if mode == 1:
        serial.write_line("b: mode = 1")
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # #
            """)
        vask_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_3()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index6 in range(4):
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 2:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_4()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_4()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index7 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 3:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index8 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 4:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_4()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index9 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 5:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_4()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index10 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 6:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index11 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 7:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index12 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 8:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_3()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index13 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 9:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_3()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index14 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 10:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_3()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index15 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 11:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index16 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 12:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_5()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index17 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 13:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # #
            """)
        vask_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_3()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index18 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 14:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_4()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index19 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 15:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index20 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 16:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_4()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index21 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 17:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_4()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index22 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 18:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index23 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 19:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_3()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index24 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 20:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_3()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index25 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 21:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_3()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index26 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 22:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index27 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 23:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index28 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 24:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_2()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index29 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 25:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.show_leds("""
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.show_leds("""
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        vask_3()
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        for index30 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
    elif mode == 26:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.pause(1000)
        basic.show_leds("""
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            """)
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for index31 in range(4):
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.set_motor_speed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stop_motor(wuKong.MotorList.M1)
            wuKong.stop_motor(wuKong.MotorList.M1)
            music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
                music.PlaybackMode.UNTIL_DONE)
            music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
                music.PlaybackMode.UNTIL_DONE)
            basic.show_string("færdig")
            basic.pause(20000)
input.on_button_pressed(Button.B, on_button_pressed_b)

def spin_3():
    wuKong.set_all_motor(20, 100)
    basic.pause(9000)
    wuKong.set_all_motor(32, 100)
    basic.pause(9000)
    wuKong.set_all_motor(40, 100)
    basic.pause(9000)
    wuKong.set_all_motor(80, 100)
    basic.pause(9000)
    wuKong.set_all_motor(100, 100)
    basic.pause(180000)
    wuKong.set_all_motor(80, 100)
    basic.pause(5000)
    wuKong.set_all_motor(44, 100)
    basic.pause(5000)
    wuKong.set_all_motor(32, 100)
    basic.pause(3000)
    wuKong.set_all_motor(20, 100)
    basic.pause(3000)
    wuKong.set_all_motor(15.2, 100)
    basic.pause(3000)
    wuKong.stop_motor(wuKong.MotorList.M1)
def mænteautomatik_1():
    wuKong.set_all_motor(15.2, 100)
    basic.pause(18000)
    wuKong.stop_all_motor()

def on_forever():
    global tid, mode, tryk
    # Denne function skal aktiveres når man
    # trykker på A knappen.
    # Ved kort tryk ...
    # Ved langt tryk ...
    if input.button_is_pressed(Button.A):
        tid += 1
        basic.pause(100)
    if tid >= 8:
        mode += 6
        tryk = 0
        tid = 0
    if tryk == 1 and (tid > 0 and tid < 8):
        mode += 1
        tryk = 0
        tid = 0
basic.forever(on_forever)

def on_forever2():
    global ab_tid, ab_mode, ab_tryk
    # get button value here in if statement as in a
    if input.button_is_pressed(Button.AB):
        ab_tid += 1
        basic.pause(100)
    if ab_tid >= 8:
        serial.write_line("ab: tid er større end 8")
        ab_mode = 2
        ab_tryk = 0
        ab_tid = 0
    if ab_tryk == 1 and (ab_tid > 0 and ab_tid < 8):
        serial.write_line("ab: tid er mindre end 8")
        ab_mode += 1
        ab_tryk = 0
        ab_tid = 0
    if ab_mode == 2:
        music.play(music.tone_playable(988, music.beat(BeatFraction.HALF)),
            music.PlaybackMode.UNTIL_DONE)
        music.play(music.tone_playable(784, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        control.reset()
        ab_mode = 0
        basic.pause(300)
    elif ab_mode == 1:
        music.play(music.tone_playable(988, music.beat(BeatFraction.EIGHTH)),
            music.PlaybackMode.UNTIL_DONE)
        wuKong.set_servo_angle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
        wuKong.set_light_mode(wuKong.LightMode.OFF)
        wuKong.stop_all_motor()
        ab_mode = 0
        basic.pause(300)
basic.forever(on_forever2)
