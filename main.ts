let tryk = 0
let tid = 0
let mode = 0
let ab_tryk = 0
let ab_tid = 0
let ab_mode = 0
function tøm_vand () {
    wuKong.setMotorSpeed(wuKong.MotorList.M2, 100)
    basic.pause(18000)
    wuKong.stopMotor(wuKong.MotorList.M2)
}
function vask_3 () {
    for (let index = 0; index < 3; index++) {
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.4)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, -16.2)
        basic.pause(18000)
    }
    wuKong.stopMotor(wuKong.MotorList.M1)
    wuKong.setLightMode(wuKong.LightMode.OFF)
}
function spin_1 () {
    wuKong.setAllMotor(20, 100)
    basic.pause(9000)
    wuKong.setAllMotor(32, 100)
    basic.pause(9000)
    wuKong.setAllMotor(44, 100)
    basic.pause(9000)
    wuKong.setAllMotor(60, 100)
    basic.pause(140000)
    wuKong.setAllMotor(40, 100)
    basic.pause(5000)
    wuKong.setAllMotor(32, 100)
    basic.pause(3000)
    wuKong.setAllMotor(20, 100)
    basic.pause(3000)
    wuKong.setAllMotor(15.2, 100)
    basic.pause(3000)
    wuKong.stopMotor(wuKong.MotorList.M1)
}
function spin_5 () {
    wuKong.setAllMotor(20, 100)
    basic.pause(9000)
    wuKong.setAllMotor(32, 100)
    basic.pause(120000)
    wuKong.setAllMotor(20, 100)
    basic.pause(5000)
    wuKong.setAllMotor(15.2, 100)
    basic.pause(3000)
    wuKong.stopMotor(wuKong.MotorList.M1)
}
function vask_5 () {
    for (let index = 0; index < 2; index++) {
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.4)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, -16.2)
        basic.pause(18000)
    }
    wuKong.stopMotor(wuKong.MotorList.M1)
    wuKong.setLightMode(wuKong.LightMode.OFF)
}
input.onButtonPressed(Button.A, function () {
    if (tryk == 0) {
        tryk = 1
        tid = 0
    }
    if (mode == 1) {
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        basic.showString("Miele")
        basic.showString("Bomuld rpm 1600")
        basic.pause(100)
    } else if (mode == 2) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Kort rpm 1200")
        basic.pause(100)
    } else if (mode == 3) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Forvask rpm 1600")
        basic.pause(100)
    } else if (mode == 4) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Finvask rpm 800")
        basic.pause(100)
    } else if (mode == 5) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Mørkt rpm 1200")
        basic.pause(100)
    } else if (mode == 6) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Skjorter rpm 600")
        basic.pause(100)
    } else if (mode == 7) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Spin rpm 1600")
        basic.pause(100)
    } else if (mode == 8) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Bomuld kort rpm 1600")
        basic.pause(100)
    } else if (mode == 9) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Forvask kort rpm 1600")
        basic.pause(100)
    } else if (mode == 10) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Finvask kort 800rpm")
        basic.pause(100)
    } else if (mode == 11) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Mørkt kort rpm 1200")
        basic.pause(100)
    } else if (mode == 12) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Skjorter kort rpm 600")
        basic.pause(100)
    } else if (mode == 13) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Bomuld rpm 1200")
        basic.pause(100)
    } else if (mode == 14) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Kort rpm 800")
        basic.pause(100)
    } else if (mode == 15) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Forvask rpm 1200")
        basic.pause(100)
    } else if (mode == 16) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Finvask rpm 600")
        basic.pause(100)
    } else if (mode == 17) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Mørkt rpm 800")
        basic.pause(100)
    } else if (mode == 18) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Spin rpm 1200")
        basic.pause(100)
    } else if (mode == 19) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Bomuld rpm 800")
        basic.pause(100)
    } else if (mode == 20) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Kort rpm 600")
        basic.pause(100)
    } else if (mode == 21) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Forvask rpm 800")
        basic.pause(100)
    } else if (mode == 22) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Mørkt rpm 600")
        basic.pause(100)
    } else if (mode == 23) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Spin rpm 800")
        basic.pause(100)
    } else if (mode == 24) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Bomuld rpm 600")
        basic.pause(100)
    } else if (mode == 25) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Forvask rpm 600")
        basic.pause(100)
    } else if (mode == 26) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        basic.showString("Spin rpm 600")
        basic.pause(100)
    }
    if (mode > 26) {
        mode = 0
        basic.clearScreen()
    }
})
function spin_4 () {
    wuKong.setAllMotor(20, 100)
    basic.pause(9000)
    wuKong.setAllMotor(32, 100)
    basic.pause(9000)
    wuKong.setAllMotor(44, 100)
    basic.pause(9000)
    wuKong.setAllMotor(80, 100)
    basic.pause(120000)
    wuKong.setAllMotor(44, 100)
    basic.pause(5000)
    wuKong.setAllMotor(32, 100)
    basic.pause(3000)
    wuKong.setAllMotor(20, 100)
    basic.pause(3000)
    wuKong.setAllMotor(15.2, 100)
    basic.pause(3000)
    wuKong.stopMotor(wuKong.MotorList.M1)
}
function vask_2 () {
    for (let index = 0; index < 3; index++) {
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.4)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, -16.2)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.4)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, -16.2)
        basic.pause(18000)
    }
    wuKong.stopMotor(wuKong.MotorList.M1)
    wuKong.setLightMode(wuKong.LightMode.OFF)
}
function vask_4 () {
    for (let index = 0; index < 2; index++) {
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.4)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, -16.2)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.4)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, -16.2)
        basic.pause(18000)
    }
    wuKong.stopMotor(wuKong.MotorList.M1)
    wuKong.setLightMode(wuKong.LightMode.OFF)
}
function vask_1 () {
    for (let index = 0; index < 4; index++) {
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.4)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, -16.2)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.4)
        basic.pause(18000)
        wuKong.stopMotor(wuKong.MotorList.M1)
        basic.pause(3000)
        wuKong.setMotorSpeed(wuKong.MotorList.M1, -16.2)
        basic.pause(18000)
    }
    wuKong.stopMotor(wuKong.MotorList.M1)
    wuKong.setLightMode(wuKong.LightMode.OFF)
}
input.onButtonPressed(Button.AB, function () {
    serial.writeLine("knap a+b trykkes")
    serial.writeLine("ab_tryk: " + ("" + ab_tryk))
    serial.writeLine("ab_tid: " + ("" + ab_tid))
    ab_tryk = 1
    ab_tid = 0
    serial.writeLine("ab_tryk efter +1: " + ("" + ab_tryk))
})
function spin_2 () {
    wuKong.setAllMotor(20, 100)
    basic.pause(9000)
    wuKong.setAllMotor(32, 100)
    basic.pause(9000)
    wuKong.setAllMotor(44, 100)
    basic.pause(9000)
    wuKong.setAllMotor(80, 100)
    basic.pause(160000)
    wuKong.setAllMotor(44, 100)
    basic.pause(5000)
    wuKong.setAllMotor(32, 100)
    basic.pause(3000)
    wuKong.setAllMotor(20, 100)
    basic.pause(3000)
    wuKong.setAllMotor(15.2, 100)
    basic.pause(3000)
    wuKong.stopMotor(wuKong.MotorList.M1)
}
input.onButtonPressed(Button.B, function () {
    serial.writeLine("der trykkes på b")
    music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
    if (mode == 1) {
        serial.writeLine("b: mode = 1")
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # #
            `)
        vask_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_3()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 2) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_4()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_4()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 3) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 4) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_4()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 5) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_4()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 6) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 7) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 8) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_3()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 9) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_3()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_3()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 10) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_3()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 11) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 12) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_5()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 13) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . . # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            . # # # #
            `)
        vask_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_3()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 14) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_4()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 15) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 16) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_4()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 17) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_4()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 18) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        spin_2()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 19) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_3()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 20) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_3()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 21) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_3()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 22) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 23) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        spin_1()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 24) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_2()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 25) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.showLeds(`
            . . . . .
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(5000)
        mænteautomatik_1()
        basic.pause(1000)
        basic.showLeds(`
            . . . . .
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        vask_3()
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    } else if (mode == 26) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 45)
        basic.pause(1000)
        basic.showLeds(`
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            # # # # #
            `)
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        spin_5()
        basic.pause(1000)
        tøm_vand()
        basic.pause(1000)
        for (let index = 0; index < 4; index++) {
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, 15.2)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            basic.pause(2000)
            wuKong.setMotorSpeed(wuKong.MotorList.M1, -16)
            basic.pause(5000)
            wuKong.stopMotor(wuKong.MotorList.M1)
            wuKong.stopMotor(wuKong.MotorList.M1)
            music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
            music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
            basic.showString("færdig")
            basic.pause(20000)
        }
    }
})
function spin_3 () {
    wuKong.setAllMotor(20, 100)
    basic.pause(9000)
    wuKong.setAllMotor(32, 100)
    basic.pause(9000)
    wuKong.setAllMotor(40, 100)
    basic.pause(9000)
    wuKong.setAllMotor(80, 100)
    basic.pause(9000)
    wuKong.setAllMotor(100, 100)
    basic.pause(180000)
    wuKong.setAllMotor(80, 100)
    basic.pause(5000)
    wuKong.setAllMotor(44, 100)
    basic.pause(5000)
    wuKong.setAllMotor(32, 100)
    basic.pause(3000)
    wuKong.setAllMotor(20, 100)
    basic.pause(3000)
    wuKong.setAllMotor(15.2, 100)
    basic.pause(3000)
    wuKong.stopMotor(wuKong.MotorList.M1)
}
function mænteautomatik_1 () {
    wuKong.setAllMotor(15.4, 100)
    basic.pause(18000)
    wuKong.stopAllMotor()
}
basic.forever(function () {
    // Denne function skal aktiveres når man
    // trykker på A knappen.
    // Ved kort tryk ...
    // Ved langt tryk ...
    if (input.buttonIsPressed(Button.A)) {
        tid += 1
        basic.pause(100)
    }
    if (tid >= 8) {
        mode += 6
        tryk = 0
        tid = 0
    }
    if (tryk == 1 && (tid > 0 && tid < 8)) {
        mode += 1
        tryk = 0
        tid = 0
    }
})
basic.forever(function () {
    // get button value here in if statement as in a
    if (input.buttonIsPressed(Button.AB)) {
        ab_tid += 1
        basic.pause(100)
    }
    if (ab_tid >= 8) {
        serial.writeLine("ab: tid er større end 8")
        ab_mode = 2
        ab_tryk = 0
        ab_tid = 0
    }
    if (ab_tryk == 1 && (ab_tid > 0 && ab_tid < 8)) {
        serial.writeLine("ab: tid er mindre end 8")
        ab_mode += 1
        ab_tryk = 0
        ab_tid = 0
    }
    if (ab_mode == 2) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Half)), music.PlaybackMode.UntilDone)
        music.play(music.tonePlayable(784, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        control.reset()
        ab_mode = 0
        basic.pause(300)
    } else if (ab_mode == 1) {
        music.play(music.tonePlayable(988, music.beat(BeatFraction.Eighth)), music.PlaybackMode.UntilDone)
        wuKong.setServoAngle(wuKong.ServoTypeList._180, wuKong.ServoList.S0, 0)
        wuKong.setLightMode(wuKong.LightMode.OFF)
        wuKong.stopAllMotor()
        ab_mode = 0
        basic.pause(300)
    }
})
