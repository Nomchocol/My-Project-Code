# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define L = Character("เลย์(ตัวเรา)", color="#ff7700")
define P = Character("ศาสตราจารย์ปูไทย", color="#0400ff")
define whatP = Character("???", color="#0400ff")
define T = Character("เทสโต้", color="#00ff1a")
define whatT = Character("???", color="#00ff1a")
define R = Character("โรลเลอร์โคสเตอร์", color="#ffc400")
define whatR = Character("???", color="#ffcc00")
define C = Character("CapybaraBOSS", color="#ff0000")
define what = Character("???", color="#ff0000")
define s = Character("สัตว์ประหลาด B", color="#ff0000")
define everyone = Character("everyone", color="#a4004dff")

define score = 0
image Beyond the Ruins = "Beyond the Ruins.png"
# The game starts here.

transform open:
    xalign 0.1
    yalign -1.0       # เริ่มนอกจอด้านบน
    linear 0.1 yalign 1.0   # สไลด์ลงมาใช้เวลา 1 วินาที

transform out:
    yalign 1.0       # เริ่มนอกจอด้านด้านล่าง
    linear 0.1 yalign -10.0   # สไลด์ออกบนใช้เวลา 1 วินาที


transform fade_away:
    alpha 0.5

transform fade_back:
    alpha 1.0

transform shake:
    linear 0.10 xoffset -20
    linear 0.10 xoffset 20
    linear 0.10 xoffset -20
    linear 0.10 xoffset 20
    linear 0.10 xoffset -20
    linear 0.10 xoffset 20
    linear 0.10 xoffset -20
    linear 0.10 xoffset 20
    linear 0.10 xoffset 0

transform shake_open:
    linear 0.05 xoffset -20
    linear 0.05 xoffset 20
    linear 0.05 xoffset -20
    linear 0.05 xoffset 20
    linear 0.05 xoffset 0

label start:
    scene Beyond the Ruins
    with fade # ภาพค่อยๆปรากฏ
    pause 60  # หน่วงไว้เวลา
    jump Hopital


label Hopital:
    play music "Loop Hero.mp3" volume 0.3 fadein 2.0
    scene black with fade
    play audio "goku-teleport-sound.mp3"   volume 0.3 
    $ renpy.pause(1.0, hard=True)
    scene hospital at shake_open

    show character0ashadow at open
    L "*อึ้ก...*"
    show character0a at Position(xalign=0.1, yalign=1.0)

    L "{cps=60}อีหยังวะ!..เกิดอะไรขึ้น?{/cps}"
    L "{cps=60}ที่นี่ที่ไหน..?{/cps}"
    what "{cps=20}*กรอบ... กึก... แคร่ก...*{/cps}"
    L "{cps=60}เสียงไรวะ?!{/cps}"
    show monster at right
    what "{cps=20}กกก...กววววรร์...{/cps}"
    L "{cps=60}ตะ..ตัวเชี้ยยย...ไรวะน่ะะะะะะะะะะะะะะะะะะ!!??{/cps}"
    menu:
        "หนีโว้ยยย":
            L "{cps=60}ใครจะอยู่ก็อยู่!{/cps}"
            hide character0ashadow
            show character0a at out
            play audio "teleport.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)
            jump city

        "จะหมัดจะมวยจะไรก็มาดิวะ":
            stop music fadeout 2.0
            jump hospital1

label hospital1:
    scene expression Solid("#bcbcbc") with dissolve
    $ renpy.pause(0.5, hard=True)
    play music "Battle.mp3" volume 0.25 
    scene background
    with dissolve 
    show character0 at Position(xalign=0.2, yalign=1.0)  # ตัวละครผู้เล่น
    show monster battle at Position(xalign=0.8, yalign=0.2) # ศัตรูอยู่บน
    with dissolve 
    menu:
        "ล้มเสือด้วยมือเปล่า(มือเปล่า)":
            L "{cps=60}ตายซ่ะะ! เจ้าเสือ!!{/cps}"
            show monster battle at Position(xalign=0.8, yalign=0.2), shake
            play audio "strongpunch.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)
            show character0 at Position(xalign=0.2, yalign=1.0), shake
            play audio "strongpunch.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)

            what "{cps=60}กววววรร์!!!!!...{/cps}"

            play audio "death-bong.mp3" volume 0.3
            hide monster battle with dissolve
            
            L "{cps=60}*เอื้อ..!!*{/cps}"
            stop music fadeout 2.0
            jump hospital0

        "สู้แบบฉลาดๆ(มือเปล่า)":
            L "{cps=60}วัน ทรู หลบ! วัน ทรู ต่อย!{/cps}"
            show monster battle at Position(xalign=0.8, yalign=0.2), shake
            play audio "strongpunch.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)

            what "{cps=60}กววววรร์!!!!!...{/cps}"

            play audio "death-bong.mp3" volume 0.3
            hide monster battle with dissolve
            L "{cps=60}เยี่ยม!!{/cps}"
            stop music fadeout 2.0
            jump hospital2

label hospital0:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    play music "Loop Hero.mp3" volume 0.3 fadein 2.0
    scene hospital
    show character0a
    with dissolve
    L "{cps=60}ให้ตายสิ..บาดเจ็บเพราะมันเนี่ยนะ!{/cps}"
    L "{cps=60}ตรูคงไม่กลายร่างเป็นแบบนั้นใช่ไหม?{/cps}"
    whatR "{cps=60}เฮ้! นายที่อยู่ตรงนั้นน่ะ{/cps}"
    L "{cps=60}หือ?..อีหยังวะ?..{/cps}"

    hide character0a
    show character2b
    with dissolve

    whatR "{cps=60}นาย..เก่งดีหนิที่รอดมาได้{/cps}"

    hide character2b
    show character0a at Position(xalign=0.1, yalign=1.0)
    show character2 at Position(xalign=0.85, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)
    show character2 at Position(xalign=0.85, yalign=1.0), fade_away

    L "{cps=60}เธอเป็นใคร?{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character2 at Position(xalign=0.85, yalign=1.0), fade_back
    R "{cps=60}ฉันโรลเลอร์โคสเตอร์{/cps}"
    R "{cps=60}เป็นผู้รอดชีวิตของที่นี่{/cps}"
    R "{cps=60}ช่างเรื่องนั้นก่อน แผลนาย..ฉันช่วยรักษาให้ได้{/cps}"
    menu:
        "จัดมาเลยเจ๊คนสวย":
            show character2 at Position(xalign=0.85, yalign=1.0), fade_away
            show character0a at Position(xalign=0.1, yalign=1.0), fade_back
            L "{cps=60}ช่วยทีสิ! ขอเน้นๆ{/cps}"
            show character0a at Position(xalign=0.1, yalign=1.0), fade_away
            show character2 at Position(xalign=0.85, yalign=1.0), fade_back
            R "{cps=60}*........*{/cps}"
            R "{cps=60}ให้ฉันจัดการเอง เรื่องนี้ฉันถนัด{/cps}"

            scene expression Solid("#FFFFFF")
            with fade
            window hide
            show text "{color=#000000}จากฝีมือการรักษาของโรลเลอร์โคสเตอร์ ทำให้แผลหายดีได้ในระยะเวลาอันสั๊น..{/color}" with dissolve
            pause 60         
            jump R

        "บ่เอา":
            show character2 at Position(xalign=0.85, yalign=1.0), fade_away
            show character0a at Position(xalign=0.1, yalign=1.0), fade_back
            L "{cps=60}สบม. สบายมาก! ฉันไม่ต้องการ{/cps}"
            show character0a at Position(xalign=0.1, yalign=1.0), fade_away
            show character2 at Position(xalign=0.85, yalign=1.0), fade_back
            R "{cps=60}หือ..ก็แล้วแต่นาย{/cps}"

            scene expression Solid("#FFFFFF")
            with fade
            window hide
            show text "{color=#000000}ถึงจะใช้เวลานานในการรักษาด้วยตนเองไปหน่อย แต่สุดท้ายแผลก็ถูกรักษาจนหายดี..{/color}" with dissolve
            pause 60
            jump R

label R:
    scene hospital
    show character0a at Position(xalign=0.1, yalign=1.0)
    with dissolve

    L "{cps=60}โอเคร หายดีเรียบร้อย{/cps}"

    show character2 at Position(xalign=0.85, yalign=1.0)
    with dissolve
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    R "{cps=60}การรักษาเป็นไปได้ด้วยดีสินะ{/cps}"
    R "{cps=60}มาเข้าเรื่อง..ฉันอยากให้นายมาร่วมทีมจับคู่กับฉัน{/cps}"
    R "{cps=60}สนใจไหม{/cps}"
    menu:
        "แน่นอนคนเยอะย่อมดีกว่า":
            show character2 at Position(xalign=0.85, yalign=1.0), fade_away
            show character0a at Position(xalign=0.1, yalign=1.0), fade_back
            L "{cps=60}จัดมาอย่าให้เสีย{/cps}"
            show character2 at Position(xalign=0.85, yalign=1.0), fade_back
            show character0a at Position(xalign=0.1, yalign=1.0), fade_away
            R "{cps=60}ดี! เราจะหาทางออกไปจากที่นี่{/cps}"
            jump city1

        "ไม่เอา ฉันจะเป็นหมาป่าเดียวดาย":
            show character2 at Position(xalign=0.85, yalign=1.0), fade_away
            show character0a at Position(xalign=0.1, yalign=1.0), fade_back          
            L "{cps=60}โทษที ฉันอยากไปคนเดียวมากกว่า{/cps}"
            show character2 at Position(xalign=0.85, yalign=1.0), fade_back
            show character0a at Position(xalign=0.1, yalign=1.0), fade_away            
            R "{cps=60}โอเคร ตามใจละกัน{/cps}"

            hide character2
            show character0a at center, fade_back
            with dissolve
            L "{cps=60}...ต้องหาทางออกจากที่นี่ให้เจอ{/cps}"
            L "{cps=60}อืม..เดินไปทางนี้ละกัน{/cps}"
            jump city3

label hospital2:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    play music "Loop Hero.mp3" volume 0.3 fadein 2.0
    scene hospital
    show character0a
    with dissolve
    L "{cps=60}ง่ายกว่าที่คิด{/cps}"
    whatR "{cps=60}เฮ้! นายที่อยู่ตรงนั้นน่ะ{/cps}"
    L "{cps=60}หือ?!..{/cps}"

    hide character0a
    show character2b
    with dissolve
    whatR "{cps=60}ฉันเห็นหมดแล้ว..นายสู้ได้ฉลาดมาก{/cps}"
    
    hide character2b
    show character0a at Position(xalign=0.1, yalign=1.0)
    show character2 at Position(xalign=0.85, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)
    show character2 at Position(xalign=0.85, yalign=1.0), fade_away

    L "{cps=60}เธอเป็นใคร?{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character2 at Position(xalign=0.85, yalign=1.0), fade_back
    R "{cps=60}ฮ่าๆ ฉันโรลเลอร์โคสเตอร์ ยินดีที่ได้รู้จัก{/cps}"
    R "{cps=60}ฉันเป็นผู้รอดชีวิตของที่นี่{/cps}"
    R "{cps=60}แล้วนาย ชื่ออะไร?{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character2 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}ฉันชื่อเลย์ ไม่รู้มาโผล่ที่นี่ได้ยังไง?{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character2 at Position(xalign=0.85, yalign=1.0), fade_back
    R "{cps=60}นายรู้ไว้แค่ว่าที่นี่มีแต่สัตว์ประหลาดอยู่เยอะก็พอ{/cps}"
    R "{cps=60}มาเข้าเรื่อง ฉันอยากให้นายมาร่วมทีมจับคู่กับฉัน{/cps}"
    R "{cps=60}สนใจไหม{/cps}"
    menu:
        "แน่นอนคนเยอะย่อมดีกว่า":
            show character0a at Position(xalign=0.1, yalign=1.0), fade_back
            show character2 at Position(xalign=0.85, yalign=1.0), fade_away
            L "{cps=60}จัดมาอย่าให้เสีย{/cps}"
            show character0a at Position(xalign=0.1, yalign=1.0), fade_away
            show character2 at Position(xalign=0.85, yalign=1.0), fade_back
            R "{cps=60}ดี! เราจะหาทางออกไปจากที่นี่{/cps}"
            jump city1

        "ไม่เอา ฉันจะเป็นหมาป่าเดียวดาย":
            show character0a at Position(xalign=0.1, yalign=1.0), fade_back
            show character2 at Position(xalign=0.85, yalign=1.0), fade_away
            L "{cps=60}โทษที ฉันอยากไปคนเดียวมากกว่า{/cps}"
            R "{cps=60}โอเคร ตามใจละกัน{/cps}"
            hide character2
            show character0a at center, fade_back
            with dissolve
            L "{cps=60}...ต้องหาทางออกจากที่นี่ให้เจอ{/cps}"
            L "{cps=60}อืม..เดินไปทางนี้ละกัน{/cps}"
            jump city3

label city3:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene city
    show character0a
    with dissolve
    L "{cps=60}ที่นี่มัน กลางเมืองสินะ{/cps}"
    what "{cps=20}กกก...กววววรร์...{/cps}"
    L "{cps=60}อีหยังน่ะ!?{/cps}"
    L "{cps=60}*บางอย่างกำลังมาทางนี้!?..*{/cps}"

    menu:
        "หลบซ่อน":
            stop music fadeout 2.0
            $ renpy.pause(1.0, hard=True)
            play music "m3.mp3" volume 0.3 fadein 2.0
            hide character0a with dissolve
            $ renpy.pause(1.0, hard=True)
            what "{cps=20}ตึก..ตึก..{/cps}"
            show monster at right ,with dissolve
            what "{cps=20}กกก...กววววรร์...{/cps}"
            show monster at center ,with dissolve
            what "{cps=20}ตึก...ตึก.ตึก.{/cps}"
            what "{cps=20}กววววรร์...{/cps}"
            show monster at left ,with dissolve
            what "{cps=20}ตึก..ตึก..{/cps}"
            hide monster with dissolve
            what "{cps=20}..ตึก...{/cps}"
            what "{cps=20}.................{/cps}"
            L "{cps=60}ไปแล้ว..สินะ{/cps}"
            stop music fadeout 1.0
            show character0a with dissolve
            $ renpy.pause(1.0, hard=True)
            play music "Loop Hero.mp3" volume 0.3 fadein 2.0
            L "{cps=60}สัตว์ประหลาดอีกตัวเหรอ{/cps}"
            L "{cps=60}มันคือตัวอะไรกันแน่{/cps}"
            L "{cps=60}สงสัยไปก็เสียเวลาเปล่า{/cps}"

        "จะหมัดจะมวยจะไรก็มาดิวะ":
            show character0a at Position(xalign=0.01, yalign=1.0)
            show monster at right
            with dissolve
            $ renpy.pause(1.0, hard=True)
            show monster at right
            L "{cps=60}นั่นมัน..สัตว์ประหลาดอีกตัว!{/cps}"
            L "{cps=60}มันคือตัวอะไรกันแน่นะ{/cps}"
            L "{cps=60}สงสัยไปก็เปล่าประโยชน์{/cps}"

            show monster at right , shake
            what "{cps=20}กกก...กววววรร์...{/cps}"
            stop music fadeout 2.0

            scene expression Solid("#bcbcbc") with dissolve
            $ renpy.pause(0.5, hard=True)
            play music "Battle.mp3" volume 0.25
            scene background
            with dissolve
            show character0 at Position(xalign=0.2, yalign=1.0)  # ตัวละครผู้เล่น
            show monster battle at Position(xalign=0.8, yalign=0.2) # ศัตรูอยู่บน
            with dissolve 
            menu:
                "ล้มเสือด้วยมือเปล่าฉบับสมบูรณ์(มือเปล่า)":
                    L "{cps=60}วัน ทรู หลบ! วัน ทรู ต่อย!{/cps}"
                    show monster battle at Position(xalign=0.8, yalign=0.2), shake
                    play audio "strongpunch.mp3" volume 0.3
                    $ renpy.pause(1.0, hard=True)

                    what "{cps=60}กววววรร์!!!!!...{/cps}"

                    play audio "death-bong.mp3" volume 0.3
                    hide monster battle with dissolve
                    L "{cps=60}เยี่ยม!!{/cps}"
                    stop music fadeout 2.0
                    scene black with fade
                    $ renpy.pause(1.0, hard=True)
                    play music "Loop Hero.mp3" volume 0.3 fadein 2.0
                    scene city
                    show character0a with dissolve
                    L "{cps=60}อีซี่มาก{/cps}"
                
    "{cps=60}*โครม!..ครามม!!*{/cps}"
    L "{cps=60}หือ! เสียงอะไรวะ?{/cps}"
    hide character0a 
    stop music fadeout 2.0

    play audio "01-opening.mp3" volume 0.6
    hide character0a 
    show character1bshadow
    with dissolve
    $ renpy.pause(6.0, hard=True)

    show character1b
    with dissolve
    $ renpy.pause(2.0, hard=True)

    play music "Loop Hero.mp3" volume 0.3 fadein 2.0

    L "{cps=50}ตาลุงแก่เหงือกหงำ?{/cps}"

    hide character1bshadow
    hide character1b
    show character0a at Position(xalign=0.1, yalign=1.0)
    show character1 at Position(xalign=0.85, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)

    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    whatP "{cps=60}หืม? ผุใด๋ยุม่องหั่น!!{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}คุณเป็นใครน่ะ{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1 at Position(xalign=0.85, yalign=1.0), fade_back
    whatP "{cps=60}ถ้าจะถามชื่อคนอื่นก็ต้องแนะนำตัวเองก่อนสิ{/cps}"
    whatP "{cps=60}มันเป็นมารยาทนะ{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}เอ่อก็ได้..ผมชื่อเล-{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1 at Position(xalign=0.85, yalign=1.0), fade_back
    P "{cps=60}ฉันชื่อปูไทยหรือศาสตราจารย์ปูไทย{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}....{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1 at Position(xalign=0.85, yalign=1.0), fade_back
    P "{cps=60}เลย์สินะ ตามมาสิ นายคงอยากรู้ว่าเกิดอะไรขึ้น{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}..ก็ได้วะ{/cps}"
    jump subway

label city1:
    scene black with fade
    $ renpy.pause(1.0, hard=True)  
    scene city
    show character2 at Position(xalign=0.75, yalign=1.0) zorder 1
    show character0a at Position(xalign=0.20, yalign=1.0) zorder 2
    with dissolve
    $ renpy.pause(1.0, hard=True)

    show character2 at Position(xalign=0.75, yalign=1.0), fade_away
    L "{cps=60}แล้วเธอมาอยู่ที่นี่นานรึยัง{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character2 at Position(xalign=0.75, yalign=1.0), fade_back
    R "{cps=60}ไม่นานแค่ปีสองปี{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    show character2 at Position(xalign=0.75, yalign=1.0), fade_away
    L "{cps=60}ใช่เหรอ..{/cps}"
    L "{cps=60}นั่นไม่นานหรอวะ?{/cps}"
    what "{cps=20}กกก...กววววรร์...{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    show character2 at Position(xalign=0.75, yalign=1.0), fade_back
    "{cps=60}..!?{/cps}"

    hide character2
    show character2b at Position(xalign=0.01, yalign=1.0) zorder 1
    show monster at right
    with dissolve
    $ renpy.pause(1.0, hard=True)

    show character2b at Position(xalign=0.01, yalign=1.0), fade_away
    L "{cps=60}อีหยังอีกกันวะ!!{/cps}"
    L "{cps=60}มันคือตัวอะไรเนี่ย{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character2b at Position(xalign=0.01, yalign=1.0), fade_back
    R "{cps=60}ฉันก็ไม่รู้เหมือน{/cps}"
    R "{cps=60}นายเจอไปแล้วตัวนึง งั้นเรียกสัตว์ประหลาดBก็ได้{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    show character2b at Position(xalign=0.01, yalign=1.0), fade_away
    L "{cps=60}หะ..แบบนี้ก็ได้เหรอ{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    show character2b at Position(xalign=0.01, yalign=1.0), fade_back
    s "{cps=20}...กกววววรร์!!{/cps}"
    stop music fadeout 2.0

    scene expression Solid("#bcbcbc") with dissolve
    $ renpy.pause(0.5, hard=True)
    play music "Battle.mp3" volume 0.25
    scene background
    with dissolve
    show character0 at Position(xalign=0.1, yalign=1.0)  # ตัวละครผู้เล่น
    show character2a at Position(xalign=0.3, yalign=1.0)
    show monster battle at Position(xalign=0.8, yalign=0.2) # ศัตรูอยู่บน
    with dissolve 

    menu:
        "ล้มเสือด้วยมือเปล่า(มือเปล่า)":
            L "{cps=60}ตายซ่ะะ! เจ้าเสือ!!{/cps}"
            show monster battle at Position(xalign=0.8, yalign=0.2), shake
            play audio "strongpunch.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)
            show character0 at Position(xalign=0.1, yalign=1.0), shake
            play audio "strongpunch.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)

            s "{cps=60}กววววรร์!!!!!...{/cps}"
            L "{cps=60}*อึ้ก..!! * มันยังไม่ตาย{/cps}"
            R "{cps=60}หลบไป ย่าา!! สตรีคิ๊ก!!{/cps}"

            show monster battle at Position(xalign=0.8, yalign=0.2), shake
            play audio "strongpunch.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)

            s "{cps=60}กวววววววววรร์!!!!!!!!...{/cps}"

            play audio "death-bong.mp3" volume 0.3
            hide monster battle with dissolve
            L "{cps=60}ล้มได้แล้วสินะ {/cps}"
            stop music fadeout 2.0

            scene black with fade
            $ renpy.pause(1.0, hard=True)  
            play music "Loop Hero.mp3" volume 0.3 fadein 2.0
            scene city
            show character2 at Position(xalign=0.75, yalign=1.0)
            show character0a at Position(xalign=0.20, yalign=1.0)
            with dissolve
            $ renpy.pause(1.0, hard=True)
            show character2 at Position(xalign=0.75, yalign=1.0), fade_away
            show character0a at Position(xalign=0.20, yalign=1.0), fade_back
            L "{cps=60}สู้อะไรหนิ โคตรกระจอก{/cps}"
            show character2 at Position(xalign=0.75, yalign=1.0), fade_back
            show character0a at Position(xalign=0.20, yalign=1.0), fade_away
            R "{cps=60}โทษที ฉันนึกว่ามันจะตายในทีเดียว{/cps}"
            R "{cps=60}ช่างมัน รีบไปกันต่อเถอะ{/cps}"
            show character2 at Position(xalign=0.75, yalign=1.0), fade_away
            show character0a at Position(xalign=0.20, yalign=1.0), fade_back
            L "{cps=60}ได้{/cps}"
            jump lab1

        "สู้แบบฉลาดๆ(มือเปล่า)":
            L "{cps=60}วัน ทรู หลบ! วัน ทรู ต่อย!{/cps}"
            show monster battle at Position(xalign=0.8, yalign=0.2), shake
            play audio "strongpunch.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)

            s "{cps=60}กววววรร์!!!!!...{/cps}"
            L "{cps=60}?! ยังไม่ตายเหรอ{/cps}"
            R "{cps=60}ย่าา!! สตรีคิ๊ก!!{/cps}"

            show monster battle at Position(xalign=0.8, yalign=0.2), shake
            play audio "strongpunch.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)

            s "{cps=60}กวววววววววรร์!!!!!!!!...{/cps}"

            play audio "death-bong.mp3" volume 0.3
            hide monster battle with dissolve
            L "{cps=60}ไนซ์ช็อจ!! {/cps}"
            stop music fadeout 2.0

            scene black with fade
            $ renpy.pause(1.0, hard=True)
            play music "Loop Hero.mp3" volume 0.3 fadein 2.0
            scene city
            show character2 at Position(xalign=0.75, yalign=1.0)
            show character0a at Position(xalign=0.20, yalign=1.0)
            with dissolve
            $ renpy.pause(1.0, hard=True)  
            show character2 at Position(xalign=0.75, yalign=1.0), fade_away
            show character0a at Position(xalign=0.20, yalign=1.0), fade_back
            L "{cps=60}เข้าได้สวยเลยนี่ โรลเลอร์โคสเตอร์!{/cps}"
            show character2 at Position(xalign=0.75, yalign=1.0), fade_back
            show character0a at Position(xalign=0.20, yalign=1.0), fade_away
            R "{cps=60}นายก็เจ๋งไม่เบา{/cps}"
            R "{cps=60}เสียเวลาไปพอสมควร ไปกันต่อเถอะ{/cps}"
            show character2 at Position(xalign=0.75, yalign=1.0), fade_away
            show character0a at Position(xalign=0.20, yalign=1.0), fade_back
            L "{cps=60}ได้{/cps}"
            jump lab1

label lab1:
    scene black with fade
    $ renpy.pause(1.0, hard=True)  
    scene lap
    show character2 at Position(xalign=0.75, yalign=1.0)
    show character0a at Position(xalign=0.20, yalign=1.0)
    with dissolve    
    $ renpy.pause(1.0, hard=True)  
    show character2 at Position(xalign=0.75, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    L "{cps=60}ที่นี่มันที่ไหนน่ะ{/cps}"
    show character2 at Position(xalign=0.75, yalign=1.0), fade_back
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    R "{cps=60}ดูไงก็เป็นห้องแลป{/cps}"
    R "{cps=60}นั่น! เหมือนจะเป็นผู้รอดชีวิต{/cps}"

    hide character2
    hide character0a
    show character1b at Position(xalign=0.40, yalign=1.0)
    show character3c at Position(xalign=0.60, yalign=1.0)
    with dissolve
    

    R "{cps=60}หนุ่มติดอาวุธ กับ ตาแก่ศาตราจารย์เองเหรอ{/cps}"
    L "{cps=60}รู้จักด้วยเหรอ{/cps}"
    R "{cps=60}เป็นผู้รอดชีวิตที่มีไม่กี่คน ถ้าไม่นับนาย{/cps}"

    hide character1b
    hide character3c
    show character2 at Position(xalign=0.01, yalign=1.0)
    show character0a at Position(xalign=0.20, yalign=1.0)
    show character1 at Position(xalign=0.80, yalign=1.0)
    show character3 at Position(xalign=0.99, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)  

    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    P "{cps=60}อะแห่ม! ฉันคือศาสตราจารย์ปูไทย{/cps}"
    P "{cps=60}ส่วนเด็กคนนี้ชื่อ เทสโต้{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_away
    show character3 at Position(xalign=0.99, yalign=1.0), fade_back
    T "{cps=60}......{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_back
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    P "{cps=60}ไหนๆกลุ่มผู้รอดชีวิตก็มารวมตัวกัน..{/cps}"
    P "{cps=60}ฉันจำเป็นจะต้องบอกอะไรพวกนายด้วย{/cps}"

    show character2 at Position(xalign=0.01, yalign=1.0), fade_back
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_away
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    R "{cps=60}ว่ามาเลยตาแก่{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_back
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    P "{cps=60}มีสัตว์ประหลาดอยู่ตนนึง..{/cps}"
    P "{cps=60}ถ้าเราจัดการมันได้ มันจะพาเราออกจากที่นี่{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_back
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_away
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    R "{cps=60}ข่าวดีเลยหนิ ตาแก่หัวล้าน!{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_back
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    P "{cps=60}ล้านแล้วมันไปหนักหัวเธอเรอะ{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    show character1 at Position(xalign=0.80, yalign=1.0), fade_away
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    L "{cps=60}แล้วสัตว์ประหลาดตนนั้นตอนนี้อยู่ไหนล่ะ{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_away
    show character3 at Position(xalign=0.99, yalign=1.0), fade_back
    T "{cps=60}นั่นน่ะฉันจะใช้อุปกรณ์ของฉันตามหามันเอง{/cps}"
    T "{cps=60}ส่วนพวกนายที่ถนัดการต่อสู้ฉันจะให้ยืมอาวุธ แล้วไปสยบมันซะ{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_back
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    P "{cps=60}ก็ตามนั้นล่ะ พวกเราต้องพึ่งพวกเธอนะ{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    show character1 at Position(xalign=0.80, yalign=1.0), fade_away
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    L "{cps=60}(*ยังไงก็ไม่มีทางออกอื่นอยู่แล้ว แถมนี่ยังง่ายกว่าทำคนเดียวอีกหลายเท่า*){/cps}"
    L "{cps=60}ผมเอาด้วย!{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_back
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_away
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    R "{cps=60}ยังไงก็เกี่ยวเนื่องกับการออกจากที่นี่อยู่แล้ว ฉันเอาด้วย!{/cps}"
    show character2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.80, yalign=1.0), fade_back
    show character3 at Position(xalign=0.99, yalign=1.0), fade_away
    P "{cps=60}ดี! งั้นพวกเราจะออกตามหามันพรุ่งนี้เช้า{/cps}"
    jump bossfight


label bossfight:
    scene expression Solid("#FFFFFF")
    with fade
    window hide
    show text "{color=#000000}เช้าวันต่อมาาาา..ก๊าาาาาาาาาาาาาาาาาาาา!! {/color}" with dissolve 
    pause 60

    scene lap
    show character0a
    with dissolve 

    L "{cps=60}เช้าแล้ว..{/cps}"
    L "{cps=60}คงได้เวลาตามหาเจ้าต้นตอแล้วสินะ{/cps}"

    scene black with fade
    $ renpy.pause(1.0, hard=True)  
    scene city

    show character3a2 at Position(xalign=0.65, yalign=1.0)
    show character1 at Position(xalign=0.45, yalign=1.0)
    show character2 at Position(xalign=0.22, yalign=1.0)
    show character0a2 at Position(xalign=0.80, yalign=1.0)
    
    show monster at Position(xalign=1.2, yalign=1.0)
    show monster2 at Position(xalign=-0.2, yalign=1.0)

    with dissolve


    L "{cps=60}ล้มเสือมือเปล่าขั้นสมบูรณ์!{/cps}"
    R "{cps=60}สตรีคิ๊ก!!{/cps}"

    show monster at Position(xalign=1.2, yalign=1.0), shake
    play audio "strongpunch.mp3" volume 0.3
    $ renpy.pause(2.0, hard=True)
    hide monster with dissolve
    

    show monster2 at Position(xalign=-0.2, yalign=1.0), shake
    play audio "strongpunch.mp3" volume 0.3
    $ renpy.pause(2.0, hard=True)
    hide monster2 with dissolve
    
    show character3a2 at Position(xalign=0.65, yalign=1.0), fade_away
    show character1 at Position(xalign=0.45, yalign=1.0), fade_away
    show character2 at Position(xalign=0.22, yalign=1.0), fade_back
    show character0a2 at Position(xalign=0.80, yalign=1.0), fade_away
    R "{cps=60}เยอะแบบนี้คงได้หมดแรงก่อนแน่{/cps}"
    show character3a2 at Position(xalign=0.65, yalign=1.0), fade_back
    show character1 at Position(xalign=0.45, yalign=1.0), fade_away
    show character2 at Position(xalign=0.22, yalign=1.0), fade_away
    show character0a2 at Position(xalign=0.80, yalign=1.0), fade_away
    T "{cps=60}ไม่หรอก มันอยู่ใกล้ๆแถวนี้แหละ{/cps}"
    show character3a2 at Position(xalign=0.65, yalign=1.0), fade_away
    show character1 at Position(xalign=0.45, yalign=1.0), fade_away
    show character2 at Position(xalign=0.22, yalign=1.0), fade_away
    show character0a2 at Position(xalign=0.80, yalign=1.0), fade_back
    L "{cps=60}ใกล้มาจะ10รอบแล้วนะ!{/cps}"
    show character3a2 at Position(xalign=0.65, yalign=1.0), fade_back
    show character1 at Position(xalign=0.45, yalign=1.0), fade_away
    show character2 at Position(xalign=0.22, yalign=1.0), fade_away
    show character0a2 at Position(xalign=0.80, yalign=1.0), fade_away
    T "{cps=60}ฉันมั่นใจเลย คราวนี้แหละ!{/cps}"
    show character3a2 at Position(xalign=0.65, yalign=1.0), fade_away
    show character1 at Position(xalign=0.45, yalign=1.0), fade_away
    show character2 at Position(xalign=0.22, yalign=1.0), fade_away
    show character0a2 at Position(xalign=0.80, yalign=1.0), fade_back
    L "{cps=60}โถ่เว้ย!{/cps}"

    scene black with fade
    $ renpy.pause(1.0, hard=True)   
    scene hospital

    show character3a2 at Position(xalign=0.65, yalign=1.0)
    show character1 at Position(xalign=0.45, yalign=1.0)
    show character2 at Position(xalign=0.22, yalign=1.0)
    show character0a2 at Position(xalign=0.80, yalign=1.0)

    with dissolve
    L "{cps=60}แถวนี้มัน....{/cps}"
    what "{cps=20}*กรอบ... งั่ม!..งั่ม!* แซบบบๆ{/cps}"
    T "{cps=60}!?{/cps}"
    T "{cps=60}นั่น!!{/cps}"

    hide character3a2
    hide character1
    hide character2
    hide character0a2
    show capiparabossshadow at center
    with dissolve

    T "{cps=60}มันอยู่นั่น! เราเจอมันแล-{/cps}"
    L "{cps=60}ชู่วว..ขมิบปากเงียบๆ{/cps}"
    P "{cps=60}เหมือนมันจะ..กำลังกินบางอย่างอยู่{/cps}"
    R "{cps=60}เอาไงดี ลุยไปทั้งๆแบบนี้เลยไหม{/cps}"

    menu:
        "สุภาพบุรุษรอให้กินเสร็จ":
            L "{cps=60}เดี๋ยวก่อน!{/cps}"
            hide capiparabossshadow
            show character3a at Position(xalign=0.65, yalign=1.0)
            show character12 at Position(xalign=0.35, yalign=1.0)
            show character2b at Position(xalign=0.22, yalign=1.0)
            show character0a at Position(xalign=0.80, yalign=1.0)
            with dissolve

            show character3a at Position(xalign=0.65, yalign=1.0), fade_away
            show character12 at Position(xalign=0.35, yalign=1.0), fade_away
            show character2b at Position(xalign=0.22, yalign=1.0), fade_away
            show character0a at Position(xalign=0.80, yalign=1.0)
            L "{cps=60}มันกำลังกินอยู่นะ เราไม่ควรไปรบกวนมันนะเว้ย!{/cps}"
            show character3a at Position(xalign=0.65, yalign=1.0), fade_away
            show character12 at Position(xalign=0.35, yalign=1.0), fade_away
            show character2b at Position(xalign=0.22, yalign=1.0), fade_back
            show character0a at Position(xalign=0.80, yalign=1.0), fade_away
            R "{cps=60}นี่เราตามหามันทั้งวันเพื่อมาดูมันกินเนี่ยนะ!{/cps}"
            show character3a at Position(xalign=0.65, yalign=1.0), fade_away
            show character12 at Position(xalign=0.35, yalign=1.0), fade_away
            show character2b at Position(xalign=0.22, yalign=1.0), fade_away
            show character0a at Position(xalign=0.80, yalign=1.0), fade_back
            L "{cps=60}ก็เหมือนกับการเวลาเรากินไรแล้วคนมาก่อกวนอะ!{/cps}"
            L "{cps=60}ไม่ช๊อบบบบไม่ชอบ!{/cps}"
            show character3a at Position(xalign=0.65, yalign=1.0), fade_away
            show character12 at Position(xalign=0.35, yalign=1.0), fade_back
            show character2b at Position(xalign=0.22, yalign=1.0), fade_away
            show character0a at Position(xalign=0.80, yalign=1.0), fade_away
            P "{cps=60}ทั้งสองคนคุยกันเสียงดังไปแล้วนะ{/cps}"
            show character3a at Position(xalign=0.65, yalign=1.0), fade_back
            show character12 at Position(xalign=0.35, yalign=1.0), fade_away
            show character2b at Position(xalign=0.22, yalign=1.0), fade_away
            show character0a at Position(xalign=0.80, yalign=1.0), fade_away
            T "{cps=60}นั่นไง!! มันมาแล้ว!!..ทุกคนระวัง!!!{/cps}"
            show character3a at Position(xalign=0.65, yalign=1.0), fade_back
            show character12 at Position(xalign=0.35, yalign=1.0), fade_back
            show character2b at Position(xalign=0.22, yalign=1.0), fade_back
            show character0a at Position(xalign=0.80, yalign=1.0), fade_back
            everyone "{cps=60}..?!{/cps}"

            hide character3a
            hide character12
            hide character2b
            hide character0a
            show capiparaboss at Position(xalign=0.5, yalign=1.0)
            with dissolve
            $ renpy.pause(1.0, hard=True)
            show capiparaboss at Position(xalign=0.5, yalign=1.0), shake

            C "{cps=40}แง่ววววววววววววว!!!!!!!!!!!!!{/cps}"
            L "{cps=60}โถ่เอ้ย! มันหงุดหงิดเลยเห็นไหม!{/cps}"
            stop music fadeout 2.0

            scene expression Solid("#bcbcbc") with dissolve
            $ renpy.pause(0.5, hard=True)
            play music "final boss.mp3" volume 0.3
            scene background
            with dissolve 
            show character1a at Position(xalign=0.1, yalign=1.0)zorder 1  # ตัวละครผู้เล่น
            show character0 at Position(xalign=0.2, yalign=1.0)zorder 3  # ตัวละครผู้เล่น
            show character2a at Position(xalign=0.3, yalign=1.0)zorder 5  # ตัวละครผู้เล่น
            show character3d at Position(xalign=0.4, yalign=1.0)zorder 7  # ตัวละครผู้เล่น
            show capiparaboss battle at Position(xalign=0.8, yalign=0.4) # ศัตรูอยู่บน
            with dissolve 

            C "{cps=40}แง่ววววว!!!!!!!!{/cps}"
            show character0 at Position(xalign=0.2, yalign=1.0), shake
            play audio "strongpunch.mp3" volume 0.3
            L "{cps=60}*ฮะเอื้อออ!..*{/cps}"
            show character1a at Position(xalign=0.1, yalign=1.0), shake
            play audio "strongpunch.mp3" volume 0.3
            P "{cps=60}*อึ้กก!..*{/cps}"
            show character2a at Position(xalign=0.3, yalign=1.0), shake
            play audio "strongpunch.mp3" volume 0.3
            R "{cps=60}*อ่าา!..*{/cps}"
            show character3d at Position(xalign=0.4, yalign=1.0), shake
            play audio "strongpunch.mp3" volume 0.3
            T "{cps=60}*พวกมึงทำเชี้ยไรเนี่ยย..แอ้กกก!!!..*{/cps}"

            L "{cps=50}*อึ้ก..* ยังไหวไหมทุกคน!{/cps}"
            P "{cps=40}ก็พอไหว..{/cps}"
            R "{cps=40}มีแผนสำรองไหม!{/cps}"
            T "{cps=60}*(ไม่น่าขอให้พวกมันช่วยเลยย..)*{/cps}"
            L "{cps=50}ทำยังไงดี?{/cps}"
            menu:
                "พลังมิตรภาพที่ไม่พร้อมใช้งาน?":
                    jump end1

                "ยั่วโมโหสุดขีด!":
                    L "{cps=50}ไอ้สัตว์ประหลาดอ้วน!{/cps}"
                    L "{cps=50}ใหญ่แต่ตัวสมองดันเท่าเม็ดถั่ว!{/cps}"
                    T "{cps=60}ทำอะไรเนี่ย!{/cps}"
                    L "{cps=50}เออน่า......หือ?!{/cps}"

                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
                    C "{cps=40}แง่ววววว!!!!!!!!{/cps}"

                    R "{cps=50}มันโมโหแล้ว!{/cps}"
                    L "{cps=50}จังหวะนี้แหละทุกคนหลบ!{/cps}"

                    play audio "goku-teleport-sound.mp3" volume 0.3
                    $ renpy.pause(1.0, hard=True)
                    show character1a at Position(xalign=0.1, yalign=1.0), out  # ตัวละครผู้เล่น
                    show character0 at Position(xalign=0.2, yalign=1.0), out  # ตัวละครผู้เล่น
                    show character2a at Position(xalign=0.3, yalign=1.0), out   # ตัวละครผู้เล่น
                    show character3d at Position(xalign=0.4, yalign=1.0), out # ตัวละครผู้เล่น
                    $ renpy.pause(0.5, hard=True)
                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake # ศัตรูอยู่บน
                    C "{cps=40}แง่ววววว!!!!!!!!{/cps}"

                    play audio "teleport.mp3" volume 0.3
                    show character1a at Position(xalign=0.1, yalign=1.0)zorder 1  # ตัวละครผู้เล่น
                    show character0 at Position(xalign=0.2, yalign=1.0)zorder 3  # ตัวละครผู้เล่น
                    show character2a at Position(xalign=0.3, yalign=1.0)zorder 5  # ตัวละครผู้เล่น
                    show character3d at Position(xalign=0.4, yalign=1.0)zorder 7  # ตัวละครผู้เล่น
                    with dissolve
                    $ renpy.pause(0.5, hard=True)
                    
                    L "{cps=50}เทสโต้! อาวุธมีไม่ใช่เหรอ!!..เอามาใช้เซ่!!!{/cps}"
                    L "{cps=50}จังหวะนี้แหละดีที่สุดแล้ว!{/cps}"
                    T "{cps=50}อะ!..เออนั่นสินะ{/cps}"
                    T "{cps=50}ทุกคนเอาไป!{/cps}"

                    show ak at Transform(zoom=0.3, xzoom=-1.0, rotate=-5, xalign=-0.07, yalign=1.14)zorder 2
                    show ak1 at Transform(zoom=0.3, rotate=-75, xalign=0.22, yalign=0.50)zorder 4
                    show ak2 at Transform(zoom=0.3, xzoom=-1.0, rotate=-45, xalign=0.18, yalign=1.35)zorder 6
                    show ak3 at Transform(zoom=0.3, rotate=-95, xalign=0.48, yalign=1.35)zorder 8
                    with dissolve
                    play audio "shocked-sound-effect.mp3" volume 0.6
                    $ renpy.pause(1.0, hard=True)

                    C "{cps=30}*..!!!??*{/cps}"
                    L "{cps=60}ยิงง!!!!!!{/cps}"

                    play audio "gun_shots_1.mp3" volume 0.3
                    $ renpy.pause(2.0, hard=True)
                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake # ศัตรูอยู่บน
                    $ renpy.pause(1.5, hard=True)
                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
                    $ renpy.pause(1.5, hard=True)
                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
                    $ renpy.pause(1.5, hard=True)
                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
                    $ renpy.pause(2.0, hard=True)

                    C "{cps=40}แง่กกกก!!!!!{/cps}"
                    stop music fadeout 2.0
                    play audio "death-bong.mp3" volume 0.3
                    hide capiparaboss battle with dissolve
                    $ renpy.pause(1.0, hard=True)
                    play music "tmpbxydyrz3.mp3" volume 0.3 fadein 1.0
                    show glass at Transform(zoom=0.25, xalign=0.109, yalign=0.55)zorder 9
                    show glass1 at Transform(zoom=0.25, xalign=0.2605, yalign=0.5)zorder 9
                    show glass2 at Transform(zoom=0.25, xalign=0.3426, yalign=0.580)zorder 9
                    show glass3 at Transform(zoom=0.25, xalign=0.4405, yalign=0.67)zorder 9
                    with dissolve
                    $ renpy.pause(1.0, hard=True)
                    
                    L "{cps=60}หึหึ..{/cps}"
                    L "{cps=60}..ง่ายซะยิ่งกว่าง่าย{/cps}"
                    stop music fadeout 2.0
                    jump end2

        "ลอบโจมตีแทงข้างหลัง!":
            L "{cps=60}ความคิดดีเลย{/cps}"
            L "{cps=60}นี่แหละโอกาสที่ดีที่สุดในการโจมตีของเรา{/cps}"
            L "{cps=60}สมาชิกทุกท่าน! ลุย!!{/cps}"
            what "{cps=60}?!..{/cps}"
            show capiparaboss at Position(xalign=0.5, yalign=1.0)
            with dissolve
            $ renpy.pause(1.0, hard=True)
            show capiparaboss at Position(xalign=0.5, yalign=1.0), shake

            C "{cps=40}แง่ววววววววววววว!!!!!!!!!!!!!{/cps}"
            stop music fadeout 2.0
            scene expression Solid("#bcbcbc") with dissolve
            $ renpy.pause(0.5, hard=True)
            play music "final boss.mp3" volume 0.3
            scene background
            with dissolve 
            show character1a at Position(xalign=0.1, yalign=1.0)zorder 1  # ตัวละครผู้เล่น
            show character0 at Position(xalign=0.2, yalign=1.0)zorder 3  # ตัวละครผู้เล่น
            show character2a at Position(xalign=0.3, yalign=1.0)zorder 5  # ตัวละครผู้เล่น
            show character3d at Position(xalign=0.4, yalign=1.0)zorder 7  # ตัวละครผู้เล่น
            show capiparaboss battle at Position(xalign=0.8, yalign=0.4) # ศัตรูอยู่บน
            with dissolve 

            menu:
                "พลังมิตรภาพ":
                    jump finalboss
            
        "ใช้อาวุธของเทสโต้":
            L "{cps=60}เดี๋ยวก่อน!{/cps}"
            L "{cps=60}เทสโต้ นายมีอุปกรณ์เจ๋งๆเยอะแยะเลย..แม่นบ่?{/cps}"
            T "{cps=60}ใช่ ก็มีที่ทำไว้รับมือกับเจ้านี่อยู่{/cps}"
            L "{cps=60}ดีล่ะ! เรามาใช้เจ้านั่นกัน{/cps}"
            L "{cps=60}สมาชิกทุกท่าน! หยิบอุปกรณ์จากเทสโต้แล้วเข้าจู่โจม!!{/cps}"
            what "{cps=60}?!..{/cps}"
            show capiparaboss at Position(xalign=0.5, yalign=1.0)
            with dissolve
            $ renpy.pause(1.0, hard=True)
            show capiparaboss at Position(xalign=0.5, yalign=1.0), shake

            C "{cps=40}แง่ววววววววววววว!!!!!!!!!!!!!{/cps}"
            stop music fadeout 2.0

            scene expression Solid("#bcbcbc") with dissolve
            $ renpy.pause(0.5, hard=True)
            play music "final boss.mp3" volume 0.3
            scene background
            with dissolve 
            show character1a at Position(xalign=0.1, yalign=1.0)zorder 1  # ตัวละครผู้เล่น
            show character0 at Position(xalign=0.2, yalign=1.0)zorder 3  # ตัวละครผู้เล่น
            show character2a at Position(xalign=0.3, yalign=1.0)zorder 5  # ตัวละครผู้เล่น
            show character3d at Position(xalign=0.4, yalign=1.0)zorder 7  # ตัวละครผู้เล่น
            show capiparaboss battle at Position(xalign=0.8, yalign=0.4) # ศัตรูอยู่บน
            with dissolve 

            menu:
                "อาวุธสุดแกร่ง":
                    show ak at Transform(zoom=0.3, xzoom=-1.0, rotate=-5, xalign=-0.07, yalign=1.14)zorder 2
                    show ak1 at Transform(zoom=0.3, rotate=-75, xalign=0.22, yalign=0.50)zorder 4
                    show ak2 at Transform(zoom=0.3, xzoom=-1.0, rotate=-45, xalign=0.18, yalign=1.35)zorder 6
                    show ak3 at Transform(zoom=0.3, rotate=-95, xalign=0.48, yalign=1.35)zorder 8
                    with dissolve
                    play audio "shocked-sound-effect.mp3" volume 0.6
                    $ renpy.pause(1.0, hard=True)

                    C "{cps=30}*.....  .. ..*{/cps}"
                    L "{cps=60}ยิงง!!!!!!{/cps}"

                    play audio "gun_shots_1.mp3" volume 0.3
                    $ renpy.pause(2.0, hard=True)
                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake # ศัตรูอยู่บน
                    $ renpy.pause(1.5, hard=True)
                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
                    $ renpy.pause(1.5, hard=True)
                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
                    $ renpy.pause(1.5, hard=True)
                    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
                    $ renpy.pause(2.0, hard=True)

                    C "{cps=40}แง่กกกก!!!!!{/cps}"
                    stop music fadeout 2.0
                    play audio "death-bong.mp3" volume 0.3
                    hide capiparaboss battle with dissolve
                    $ renpy.pause(1.0, hard=True)
                    play music "tmpbxydyrz3.mp3" volume 0.3 fadein 1.0
                    show glass at Transform(zoom=0.25, xalign=0.109, yalign=0.55)zorder 9
                    show glass1 at Transform(zoom=0.25, xalign=0.2605, yalign=0.5)zorder 9
                    show glass2 at Transform(zoom=0.25, xalign=0.3426, yalign=0.580)zorder 9
                    show glass3 at Transform(zoom=0.25, xalign=0.4405, yalign=0.67)zorder 9
                    with dissolve
                    $ renpy.pause(1.0, hard=True)
                    
                    L "{cps=60}หึหึ..{/cps}"
                    L "{cps=60}..ง่ายซะยิ่งกว่าง่าย{/cps}"
                    stop music fadeout 2.0
                    jump end2


label finalboss:
    L "{cps=60}ทุกคน..รวมพลัง!!{/cps}"
    play audio "kame_charge.mp3" volume 1.3
    show character1a at Position(xalign=0.1, yalign=1.0), shake
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    show character2a at Position(xalign=0.3, yalign=1.0), shake
    show character3d at Position(xalign=0.4, yalign=1.0), shake
    L "{cps=60}ยาาา!!{/cps}"
    play audio "kame_charge.mp3" volume 1.3
    show character1a at Position(xalign=0.1, yalign=1.0), shake
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    show character2a at Position(xalign=0.3, yalign=1.0), shake
    show character3d at Position(xalign=0.4, yalign=1.0), shake
    R "{cps=60}ยาาาาาาาาาา!!!!!!!!{/cps}"
    play audio "kame_charge.mp3" volume 1.3
    show character1a at Position(xalign=0.1, yalign=1.0), shake
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    show character2a at Position(xalign=0.3, yalign=1.0), shake
    show character3d at Position(xalign=0.4, yalign=1.0), shake                    
    T "{cps=60}ยาาาาาาาาาาาาาาาาาาา!!!!!!!!!!!!!!{/cps}"
    play audio "kame.mp3" volume 1.3
    show character1a at Position(xalign=0.1, yalign=1.0), shake_open
    show character0 at Position(xalign=0.2, yalign=1.0), shake_open
    show character2a at Position(xalign=0.3, yalign=1.0), shake_open
    show character3d at Position(xalign=0.4, yalign=1.0), shake_open               
    P "{cps=60}ยาาาาาาาา!!แค่กก.{/cps}"
    P "{cps=60}อะแห่ม!..โทษที{/cps}"
    play audio "kame_charge.mp3" volume 1.3
    show character1a at Position(xalign=0.1, yalign=1.0), shake
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    show character2a at Position(xalign=0.3, yalign=1.0), shake
    show character3d at Position(xalign=0.4, yalign=1.0), shake                        
    P "{cps=60}ยาาาาาาาาาาาา!!!!!!{/cps}"     

    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
    play audio "strongpunch.mp3" volume 0.3
    $ renpy.pause(2.0, hard=True)

    L "{cps=60}เป็นไงบ้าง..?{/cps}"

    C "{cps=40}แง่กกกก!!!!!{/cps}"
    play audio "death-bong.mp3" volume 0.3
    hide capiparaboss battle with dissolve     
    $ renpy.pause(1.0, hard=True)              

    play audio "kids-saying-yay-sound-effect_2.mp3" volume 0.4
    L "{cps=60}ยอดเยี่ยม! กระเดียมทอง!!{/cps}"
    stop music fadeout 2.0
    jump end2


label city:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene city
    show character0a 
    with dissolve

    L "{cps=60}ฮ่าๆ..รอดโว้ยย{/cps}"
    L "{cps=60}หือ? นั่นใครน่ะ{/cps}"
    stop music fadeout 2.0

    play audio "01-opening.mp3" volume 0.6
    hide character0a 
    show character1bshadow
    with dissolve
    $ renpy.pause(6.0, hard=True)

    show character1b
    with dissolve
    $ renpy.pause(2.0, hard=True)

    play music "Loop Hero.mp3" volume 0.3 fadein 2.0

    L "{cps=50}ตาลุงแก่เหงือกหงำ?{/cps}"

    hide character1bshadow
    hide character1b
    show character0a at Position(xalign=0.1, yalign=1.0)
    show character1 at Position(xalign=0.85, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)

    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1 at Position(xalign=0.85, yalign=1.0), fade_back
    whatP "{cps=60}หืม? ผุใด๋ยุม่องหั่น!!{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}ใครจะบอกล่ะ! เพิ่งเจอกันแท้ๆ{/cps}"
    L "{cps=60}ผมชื่อเลย์{/cps}"
    L "{cps=60}อายุ 26 ปี ส่วนสูง 179 ซม. น้ำหนัก 60 กก.{/cps}"
    L "{cps=60}ส่วนอาชีพ......{/cps}"
    L "{cps=60}{size=50}ไม่มี!!!{/size}{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1 at Position(xalign=0.85, yalign=1.0), fade_back
    whatP "{cps=60}..........{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}ที่นี่มันอะไรกัน ผมเจอสัตว์ประหลาดด้วย มันคืออะไรกันแน่?{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1 at Position(xalign=0.85, yalign=1.0), fade_back
    whatP "{cps=60}ไม่เคยเห็นหน้า เจ้าคงมาใหม่สินะ{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}คงงั้นมั้ง{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1 at Position(xalign=0.85, yalign=1.0), fade_back
    P "{cps=60}ฉันชื่อปูไทยหรือศาสตราจารย์ปูไทย{/cps}"
    P "{cps=60}ตามมาสิ นายคงอยากรู้ว่าเกิดอะไรขึ้น{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}โอเค ก็ได้{/cps}"
    jump subway

label subway:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene subway
    show character0a at Position(xalign=0.1, yalign=1.0)
    show character1 at Position(xalign=0.85, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    P "{cps=60}ที่นี่คือที่ที่ฉันใช้หลบพวกสัตว์ประหลาด{/cps}"
    P "{cps=60}แปปนึงนะไอ้หนู{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    L "{cps=60}..?{/cps}"
    play audio "goku-teleport-sound.mp3" volume 0.3
    hide character1 with dissolve
    $ renpy.pause(0.5, hard=True)
    show character1a at Position(xalign=0.85, yalign=1.0)
    P "{cps=60}มาละ{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    P "{cps=60}เอาล่ะ ฉันจะเล่าให้ฟัง อย่ากดข้ามล่ะ{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1a at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}.......{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1a at Position(xalign=0.85, yalign=1.0), fade_back
    P "{cps=60}เมืองนี้เคยเป็นศูนย์กลางวิทยาศาสตร์และการทดลอง{/cps}"
    P "{cps=60}จนกระทั่ง โครงการมนุษย์พันธ์ใหม่หัวฟวยนั่นเกิดขึ้น{/cps}"
    P "{cps=60}มันทำไวรัสแพร่กระจายไปทั่วเมือง{/cps}"
    P "{cps=60}ผู้คนก็เริ่มกลายร่างเป็นสัตว์ประหลาด{/cps}"
    P "{cps=60}เฮ้อ..มีผู้รอดชีวิตไม่กี่คน... เราต้องซ่อนตัวและหาทางเอาชีวิตรอด{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1a at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}บ่เป็นหยังๆ โอ๋ๆนะลุง{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1a at Position(xalign=0.85, yalign=1.0), fade_back
    P "{cps=30}.....{/cps}"
    P "{cps=30}มีชายคนหนึ่ง... ชื่อว่าเทสโต้{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1a at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}ตัดบทกันงี้เลย?{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1a at Position(xalign=0.85, yalign=1.0), fade_back
    P "{cps=60}เทสโต้เขาออกไปจากที่นี่วันก่อน บอกว่าจะไปหาเสบียงกับเบาะแสของพวกสัตว์ประหลาด{/cps}"
    P "{cps=60}ฉันขอร้องไรนายสักอย่างได้รึป่าว{/cps}"
    menu:
            "เดะพี่ช่วยเอง":
                jump Lap

            "ฉันขอปฏิเสธ":
                show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                show character1a at Position(xalign=0.85, yalign=1.0), fade_away
                L "{cps=60}ผมขอปฏิเสธ{/cps}"
                L "{cps=60}ผมตามคุณมาเพื่อฟังเรื่องราว เรื่องอื่นม่ายยเกี่ยวววววว{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_away
                show character1a at Position(xalign=0.85, yalign=1.0), fade_back
                P "{cps=60}เค๊ กะแล้วแต่เจ้า{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                show character1a at Position(xalign=0.85, yalign=1.0), fade_away
                L "{cps=60}ลาล่ะ ตาแก่เหงือกหงำ{/cps}"

                hide character0a
                hide character1a
                show character0a
                with dissolve
                L "{cps=60}เอาล่ะ คงต้องหาทางออกไปจากที่นี่ด้วยตนเอง{/cps}"
                jump city02

label city02:
    scene expression Solid("#FFFFFF")
    with fade
    window hide
    show text "{color=#000000}ระหว่างทางถึงจะเจอสัตว์ประหลาดบ้างแต่ก็ระดับกีกี้เท่านั้น ไม่ใช่ปัญหา จนกระทั่ง..{/color}" with dissolve
    pause 60

    scene city
    show capiparabossshadow at Position(xalign=0.5, yalign=1.0), shake
    with dissolve

    L "{cps=60}นั่นมันตัวอะไร มองได้ไม่ชัดเลย{/cps}"
    "{cps=90}*มันพุ่งเข้ามาโจมตีเร็วมาก..จนเกิดการต่อสู้ขึ้น..*{/cps}"
    L "{cps=60}อะ!..อะไรน่ะะ!!{/cps}"
    stop music fadeout 2.0

    scene expression Solid("#bcbcbc") with dissolve
    $ renpy.pause(0.5, hard=True)
    play music "final boss.mp3" volume 0.3
    scene background
    with dissolve
    show character0 at Position(xalign=0.2, yalign=1.0)  # ตัวละครผู้เล่น
    show capiparaboss battleshadow at Position(xalign=0.8, yalign=0.4) # ศัตรูอยู่บน
    with dissolve 

    menu:
        "ล้มเสือด้วยมือเปล่าฉบับสมบูรณ์(มือเปล่า)":
            jump battle_bossshadow1

        "ไม่อาจเห็นหนทาง(หนี)":
            play audio "goku-teleport-sound.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)           
            show character0 at Position(xalign=0.2, yalign=1.0), out
            stop music fadeout 2.0
            $ renpy.pause(1.0, hard=True)
            jump battle_bossshadow2

label battle_bossshadow1:
    L "{cps=60}วัน ทรู หลบ! วัน ทรู ต่อย!{/cps}"

    show capiparaboss battleshadow at Position(xalign=0.8, yalign=0.4), shake
    play audio "weak-punch.mp3" volume 0.3
    C "{cps=60}แง่วว!!{/cps}"
    
    L "{cps=60}บ้าเอ้ย! ไม่ใช่เสือเลยไม่ได้ผล{/cps}"
    L "{cps=60}ไม่มีทางเลือก คงต้องหนีเท่านั้น{/cps}"

    menu:
        "ไม่อาจเห็นหนทาง(หนี)":
            play audio "goku-teleport-sound.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)            
            show character0 at Position(xalign=0.2, yalign=1.0), out
            stop music fadeout 2.0
            $ renpy.pause(1.0, hard=True)
            jump battle_bossshadow2

label battle_bossshadow2:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    play music "Loop Hero.mp3" volume 0.3 fadein 2.0
    scene hospital
    show character0a 
    with dissolve

    L "{cps=60}ฮ่าๆ! ไอ้กระจอกหนีพ้นละโว้ยย{/cps}"
    L "{cps=60}ต้องหาที่พักผ่อน..{/cps}"

    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene lap
    show character0a 
    with dissolve

    L "{cps=60}ที่นี่น่าจะใช้ได้{/cps}"
    L "{cps=60}นอนละ{/cps}"
    L "{cps=60}บัย!{/cps}"

    scene expression Solid("#FFFFFF")
    with fade
    window hide
    show text "{color=#000000}เช้าวันถัดมา.....ป๊อกป้อกกก!!{/color}" with dissolve
    pause 60

    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene lap
    show character0a 
    with dissolve

    L "{cps=60}เช้าแล้ว...เอาล่ะมีแรงขึ้นมาเลย!{/cps}"
    L "{cps=60}ว่าแต่ที่นี่มัน ห้องแลปหนิ{/cps}"
    L "{cps=60}!? นั่นมัน{/cps}"

    show character0a at Position(xalign=0.1, yalign=1.0)
    show character3died at Position(xalign=0.95, yalign=1.0)
    with dissolve

    L "{cps=60}ศพเหรอ เหมือนเพิ่งตายได้ไม่นาน{/cps}"
    L "{cps=60}มีอาวุธวางอยู่...{/cps}"
    L "{cps=60}..เสร็จโจร!{/cps}"
    menu:
        "ปืนพกเก่าๆ":
            L "{cps=60}ขอบใจสำหรับอาวุธปืน ถึงจะไม่รู้ว่าใคร{/cps}"
            jump battle_bosss

        "กระบองไฟฟ้ากากๆ":
            L "{cps=60}ขอบใจสำหรับอาวุธกระบอง ถึงจะไม่รู้ว่าใคร{/cps}"
            jump battle_bosss

label battle_bosss:
    scene lap
    show character0a with dissolve

    L "{cps=60}ได้เวลา..ลุย!!{/cps}"

    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene city
    show capiparabossshadow
    with dissolve

    L "{cps=60}ฮ่า! คิดแล้วว่าแกยังอยู่ที่นี่{/cps}"
    L "{cps=60}วันนี้แหละ! ฉันจะจัดการแกซะ!!{/cps}"

    show capiparaboss at Position(xalign=0.5, yalign=1.0), shake
    C "{cps=90}แง่ววววววววววววว!!!!!!!!!!!!!{/cps}"

    stop music fadeout 2.0

    scene expression Solid("#bcbcbc") with dissolve
    $ renpy.pause(0.5, hard=True)
    play music "final boss.mp3" volume 0.3
    scene background
    with dissolve
    show character0 at Position(xalign=0.2, yalign=1.0)  # ตัวละครผู้เล่น
    show capiparaboss battle at Position(xalign=0.8, yalign=0.4) # ศัตรูอยู่บน
    with dissolve 

    menu:
        "เหตุฉไหนข้าจะใช้มือ(สู้ด้วยอาวุธที่มี)":
            jump battle_boss301

        "ล้มเสือด้วยมือเปล่าฉบับสมบูรณ์(มือเปล่า)":
            jump battle_boss3

label Lap:
    scene subway
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1a at Position(xalign=0.85, yalign=1.0), fade_away

    L "{cps=60}คุณอยากให้ผมตามหาเขา..แม่นบ่?{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1a at Position(xalign=0.85, yalign=1.0), fade_back
    P "{cps=60}ใช่ ฉันอยากให้นายไปดูที่ แลปทดลองเก่า{/cps}"
    P "{cps=60}นั่นเป็นที่ที่เขาเคยพูดว่าจะไปสำรวจ{/cps}"
    P "{cps=60}เขามีอาวุธหลายแบบพกติดตัว ฉันก็อดห่วงไม่ได้{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1a at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}โอเค ผมจะลองดู{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character1a at Position(xalign=0.85, yalign=1.0), fade_back
    P "{cps=60}ขอบใจมาก เลย์{/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_back
    show character1a at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}สบม. สบายมาก{/cps}"
    
    scene expression Solid("#FFFFFF")
    with fade
    window hide
    show text "{color=#000000}ระหว่างทางถึงจะเจอสัตว์ประหลาดบ้างแต่ก็ไม่ใช่ปัญหา{/color}" with dissolve
    pause 60

    scene lap
    show character0a
    with dissolve

    "{cps=60}*..ณ แลป..*{/cps}"
    L "{cps=60}ที่นี่เหรอแลปที่ว่า{/cps}"

    hide character0a
    show character3b
    with dissolve

    whatT "{cps=60}เห้! นายเป็นใคร? นายตามฉันมาเหรอ!?{/cps}"

    hide character3b
    show character0a at Position(xalign=0.1, yalign=1.0)
    show character3a at Position(xalign=0.85, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)
    show character3a at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}ใจเย็นก่อน ฉันชื่อเลย์ ฉันไม่ได้มาร้าย{/cps}"
    L "{cps=60}(*หมอนี่คือ เทสโต้..สินะ*){/cps}"
    show character0a at Position(xalign=0.1, yalign=1.0), fade_away
    show character3a at Position(xalign=0.85, yalign=1.0), fade_back
    T "{cps=60}ฉันไม่รู้จักนาย นายอาจเป็นหนึ่งในพวกนั้นก็ได้{/cps}"

    menu:
            "บอกชื่อศาสตราจารย์ปูไทย":
                show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                show character3a at Position(xalign=0.85, yalign=1.0), fade_away
                L "{cps=60}ศาสตราจารย์ปูไทยเป็นคนส่งฉันมา เขาเป็นห่วงนาย{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_away
                show character3a at Position(xalign=0.85, yalign=1.0), fade_back
                T "{cps=60}ศาสตราจารย์ปูไทยเหรอ... งั้นนายอาจจะพูดความจริงก็ได้{/cps}"
                T "{cps=60}นาย..ต้องการอะไรล่ะ{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                show character3a at Position(xalign=0.85, yalign=1.0), fade_away
                L "{cps=60}ศาสตราจารย์ปูไทยอยากให้นายกลับไป{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_away
                show character3a at Position(xalign=0.85, yalign=1.0), fade_back
                T "{cps=60}งั้นเหรอ ฉันคงออกมานานเกินไปสินะ{/cps}"
                T "{cps=60}ก็ได้ งั้นนายนำฉันไป{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                show character3a at Position(xalign=0.85, yalign=1.0), fade_away
                L "{cps=60}ได้ แล้วแต่นาย{/cps}"
                jump subway1

            "สัตว์ประหลาดอะไรจะหล่อเหลาขนาดนี้":
                show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                show character3a at Position(xalign=0.85, yalign=1.0), fade_away
                L "{cps=60}สัตว์ประหลาดบ้าอะไรจะหน้าตาดีแบบนี้!...{/cps}"
                L "{cps=60}ใช้ตาไหนดูถึงคิดว่าฉันเป็นพวกมัน!{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_away
                show character3a at Position(xalign=0.85, yalign=1.0), fade_back
                T "{cps=60}หึ! ใส่หมวกฟางอย่างกะคนบ้า คิดว่าเท่เหรอวะะะะะะะะะะะ!{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                show character3a at Position(xalign=0.85, yalign=1.0), fade_away
                L "{cps=60}คิดว่าตรูอยากใส่เร่ออ!! ไอ้คนออกแบบมันทำเองต่างหาก!{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_away
                show character3a at Position(xalign=0.85, yalign=1.0), fade_back
                T "{cps=60}เลิกคุยไร้สาระ ฉันไม่ต้อนรับนาย ออกไปจากที่นี่ซะ!{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                show character3a at Position(xalign=0.85, yalign=1.0), fade_away
                L "{cps=60}อ้ะ! เดี๋ยวก่อน{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_away
                show character3a at Position(xalign=0.85, yalign=1.0), fade_back
                T "{cps=60}อะไรถ้าอยากได้อาวุธล่ะก็ฉันให้นายได้ เพราะเห็นว่าเป็นผู้มีชีวิตรอดด้วยกัน{/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                show character3a at Position(xalign=0.85, yalign=1.0), fade_away
                L "{cps=60}(*เอ่อถึงจะไม่ใช่เรื่องนั้น ยังไงหมอนี่ก็ไม่เชื่อใจเราแล้วล่ะก็.. *){/cps}"
                show character0a at Position(xalign=0.1, yalign=1.0), fade_away
                show character3a at Position(xalign=0.85, yalign=1.0), fade_back
                T "{cps=60}เลือกซะ มีให้แค่นี้อย่างเรื่องมากนักล่ะ{/cps}"
                menu:
                    "ปืนพกเก่าๆ":
                        show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                        show character3a at Position(xalign=0.85, yalign=1.0), fade_away
                        L "{cps=60}ปืนพกนี่แหละเท่สุด!{/cps}"
                        show character0a at Position(xalign=0.1, yalign=1.0), fade_away
                        show character3a at Position(xalign=0.85, yalign=1.0), fade_back
                        T "{cps=60}เอาล่ะไปได้แล้ว{/cps}"
                        jump city03

                    "กระบองสายฟ้ากากๆ":
                        show character0a at Position(xalign=0.1, yalign=1.0), fade_back
                        show character3a at Position(xalign=0.85, yalign=1.0), fade_away
                        L "{cps=60}ฉันเลือกกระบองสุดเจ๋ง!{/cps}"
                        show character0a at Position(xalign=0.1, yalign=1.0), fade_away
                        show character3a at Position(xalign=0.85, yalign=1.0), fade_back
                        T "{cps=60}เอาล่ะไปได้แล้ว{/cps}"
                        jump city03
    
label subway1:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene subway
    show character0a at Position(xalign=0.70, yalign=1.0)
    show character3a2 at Position(xalign=0.30, yalign=1.0)    
    with dissolve
    $ renpy.pause(1.0, hard=True)
    L "{cps=60}ถึงแล้ว{/cps}"
    show character0a at Position(xalign=0.70, yalign=1.0), fade_away
    T "{cps=60}เหมือนจะเป็นที่อยู่ของศาสตราจารย์จริงๆ{/cps}"

    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    show character3a2 at Position(xalign=0.01, yalign=1.0)
    show character1 at Position(xalign=0.95, yalign=1.0)
    with dissolve

    P "{cps=60}มาถึงแล้วรึ{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.95, yalign=1.0), fade_away
    T "{cps=60}ศาสตราจารย์!{/cps}"

    show character3a2 at Position(xalign=0.70, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)

    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.95, yalign=1.0), fade_back
    show character3a2 at Position(xalign=0.70, yalign=1.0), fade_away
    P "{cps=60}ปลอดภัยดีสินะ{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.95, yalign=1.0), fade_away
    show character3a2 at Position(xalign=0.70, yalign=1.0), fade_back
    T "{cps=60}ผมเจอข่าวดีล่ะ{/cps}"
    T "{cps=60}มันมีสัตว์ประหลาดตัวพิเศษ ที่ถ้าจัดการมันได้..{/cps}"
    T "{cps=60}มันสามารถพาพวกเราออกจากที่นี่ได้!{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.95, yalign=1.0), fade_back
    show character3a2 at Position(xalign=0.70, yalign=1.0), fade_away
    P "{cps=60}เจ๋งแจ๋วเลย!{/cps}"
    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    show character1 at Position(xalign=0.95, yalign=1.0), fade_away
    show character3a2 at Position(xalign=0.70, yalign=1.0), fade_away
    L "{cps=60}แล้วสัตว์ประหลาดตนนั้นตอนนี้อยู่ไหนล่ะ{/cps}"

    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    hide character3a2
    show character3a at Position(xalign=0.70, yalign=1.0) ,with dissolve

    show character1 at Position(xalign=0.95, yalign=1.0), fade_away
    T "{cps=60}นั่นน่ะฉันจะสร้างอุปกรณ์ของฉันตามหามันเอง{/cps}"
    T "{cps=60}อีกอย่างกำลังของเราตอนนี้ยังไม่พร้อมรับมือหรอกนะ{/cps}"
    T "{cps=60}เราจำเป็นต้องหาพวกเพิ่ม{/cps}"
    show character3a at Position(xalign=0.70, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_away
    show character1 at Position(xalign=0.95, yalign=1.0), fade_back
    P "{cps=60}ฉันรู้จักคนนึง เราสามารถไปหาเธอได้{/cps}"
    show character3a at Position(xalign=0.70, yalign=1.0), fade_away
    show character0a at Position(xalign=0.20, yalign=1.0), fade_back
    show character1 at Position(xalign=0.95, yalign=1.0), fade_away
    L "{cps=60}งั้นรออะไรล่ะ ไปกันนนนนนนน!{/cps}"

    scene expression Solid("#FFFFFF")
    with fade
    window hide
    show text "{color=#000000}หาเท่าไหร่ก็หาไม่เจอจนมาหยุดอยู่ห้องแลป อีกแล้ว?{/color}" with dissolve
    pause 60

    scene lap
    show character3a2 at Position(xalign=0.65, yalign=1.0)
    show character1 at Position(xalign=0.45, yalign=1.0)
    show character0a2 at Position(xalign=0.80, yalign=1.0)  
    with dissolve

    L "{cps=60}ไปอยู่ที่ไหนกันนะ{/cps}"

    hide character3a2
    hide character0a2
    hide character1
    show character2
    with dissolve

    R "{cps=60}เฮ้! พวกนายน่ะ..ตามฉันมามีธุระอะไร{/cps}"

    hide character1
    show character3a2 at Position(xalign=0.01, yalign=1.0)
    show character0a at Position(xalign=0.40, yalign=1.0)
    show character12 at Position(xalign=0.20, yalign=1.0)
    show character2 at Position(xalign=0.85, yalign=1.0)
    with dissolve

    show character3a2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.40, yalign=1.0), fade_away
    show character12 at Position(xalign=0.20, yalign=1.0), fade_back
    show character2 at Position(xalign=0.85, yalign=1.0), fade_away
    P "{cps=60}อิหนู..ใจเย็นก่อนนี่ฉันเอง{/cps}"
    show character3a2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.40, yalign=1.0), fade_away
    show character12 at Position(xalign=0.20, yalign=1.0), fade_away
    show character2 at Position(xalign=0.85, yalign=1.0), fade_back
    R "{cps=60}ตาแก่เหงือกหงำเหรอ...{/cps}"
    R "{cps=60}เฮ้อ..ถ้ามีเห็ดผลไม่พอล่ะก็{/cps}"
    show character3a2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.40, yalign=1.0), fade_away
    show character12 at Position(xalign=0.20, yalign=1.0), fade_back
    show character2 at Position(xalign=0.85, yalign=1.0), fade_away
    P "{cps=60}ไม่เป็นต้องห่วง..เห็ดผลน่ะมีเยอะแยะ แต่เอาไว้ก่อน{/cps}"
    P "{cps=60}ฉันมีเรื่องสำคัญจะบอกและต้องการให้ช่วย{/cps}"

    scene expression Solid("#FFFFFF")
    with fade
    window hide
    show text "{color=#000000}ก๊าาาาาาาาาาาาาาาาา ก๊าาาาาาา 5 นาทีผ่านไป๊{/color}" with dissolve
    pause 60

    scene lap
    show character3a2 at Position(xalign=0.01, yalign=1.0)
    show character0a at Position(xalign=0.40, yalign=1.0)
    show character12 at Position(xalign=0.20, yalign=1.0)
    show character2 at Position(xalign=0.85, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)
    show character3a2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.40, yalign=1.0), fade_away
    show character12 at Position(xalign=0.20, yalign=1.0), fade_away
    show character2 at Position(xalign=0.85, yalign=1.0), fade_back
    R "{cps=60}แบบนี้นี่เอง{/cps}"
    R "{cps=60}ได้ ฉันให้ความร่วมมือ{/cps}"
    show character3a2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.40, yalign=1.0), fade_back
    show character12 at Position(xalign=0.20, yalign=1.0), fade_away
    show character2 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}แจ๋ว เป็นไปด้วยดี{/cps}"
    show character3a2 at Position(xalign=0.01, yalign=1.0), fade_back
    show character0a at Position(xalign=0.40, yalign=1.0), fade_away
    show character12 at Position(xalign=0.20, yalign=1.0), fade_away
    show character2 at Position(xalign=0.85, yalign=1.0), fade_away
    T "{cps=60}เอาล่ะๆ เรื่องตามหาทางออกน่ะ เอาไว้พรุ่งนี้เช้า{/cps}"
    T "{cps=60}ทางเราจำเป็นต้องพักเอาแรง..{/cps}"
    show character3a2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.40, yalign=1.0), fade_back
    show character12 at Position(xalign=0.20, yalign=1.0), fade_away
    show character2 at Position(xalign=0.85, yalign=1.0), fade_away
    L "{cps=60}เครๆ เอางั้นก็ด้ะ{/cps}"
    show character3a2 at Position(xalign=0.01, yalign=1.0), fade_away
    show character0a at Position(xalign=0.40, yalign=1.0), fade_away
    show character12 at Position(xalign=0.20, yalign=1.0), fade_away
    show character2 at Position(xalign=0.85, yalign=1.0), fade_back
    R "{cps=60}......{/cps}"
    jump bossfight
    
label city03:
    scene expression Solid("#FFFFFF")
    with fade
    window hide
    show text "{color=#000000}คุณโดนไล่แล้วหล่ะ{/color}" with dissolve
    $ renpy.pause(3.0, hard=True)

    scene lap
    show character0a
    with dissolve
    L "{cps=60}เห้อเอาจั่งใด๋ดีน้อ กลับไปหาเฒ่าปูไทยก่อนกะได้วะะ{/cps}"

    scene black with fade
    $ renpy.pause(1.0, hard=True)
    scene city with dissolve
    L "{cps=60}นี่เรามาผิดทางหรือเปล่า... ทำไมเงียบจัง{/cps}"
    
    what "{cps=20}*กรอบ... กึก.*{/cps}"
    L "{cps=60}เสียงอะไรน่ะ...{/cps}"

    show capiparabossshadow at center
    with dissolve
    L "{cps=60}นั่น..มัน{/cps}"
    show capiparaboss at Position(xalign=0.5, yalign=1.0), shake
    C "{cps=90}แง่ววววววววววววว!!!!!!!!!!!!!{/cps}"
    
    L "{cps=60}บ้าเอ้ย! มันโผล่มาจากไหน!!{/cps}"
    stop music fadeout 2.0

    scene expression Solid("#bcbcbc") with dissolve
    $ renpy.pause(0.5, hard=True)
    play music "final boss.mp3" volume 0.3
    scene background
    with dissolve 
    show character0 at Position(xalign=0.2, yalign=1.0)  # ตัวละครผู้เล่น
    show capiparaboss battle at Position(xalign=0.8, yalign=0.4) # ศัตรูอยู่บน
    with dissolve 
    menu:
        "เหตุฉไหนข้าจะใช้มือ(สู้ด้วยอาวุธที่มี)":
            jump battle_boss301

        "ล้มเสือด้วยมือเปล่าฉบับสมบูรณ์(มือเปล่า)":
            jump battle_boss3

label battle_boss3:
    L "{cps=60}วัน ทรู หลบ! วัน ทรู ต่อย!{/cps}"
    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
    play audio "weak-punch.mp3" volume 0.3
    C "{cps=60}แง่วว!!{/cps}"

    L "{cps=60}บ้าเอ้ย! ไม่ใช่เสือเลยไม่ได้ผล{/cps}"
    L "{cps=60}คงต้องใช้อาวุธสินะ{/cps}"
    menu:
        "เหตุฉไหนข้าจะใช้มือ(สู้ด้วยอาวุธที่มี)":
            jump battle_boss301

label battle_boss301:
    scene background
    show character0 at Position(xalign=0.2, yalign=1.0)
    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
    play audio "strongpunch.mp3" volume 0.3
    $ renpy.pause(1.0, hard=True)
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    play audio "strongpunch.mp3" volume 0.3
    $ renpy.pause(1.0, hard=True)
    C "{cps=90}แง่วววว!!!!!!!!{/cps}"

    L "{cps=60}*อึ้ก..*{/cps}"
    L "{cps=60}ฮ่าๆ เป็นไงล่ะ{/cps}"
    L "{cps=60}(*โถ่เอ้ย อาวุธพังจนได้*){/cps}"

    menu:
        "แก้มือ10ปียังไม่สาย(หนี)":
            play audio "goku-teleport-sound.mp3" volume 0.3
            $ renpy.pause(1.0, hard=True)            
            show character0 at Position(xalign=0.2, yalign=1.0), out
            stop music fadeout 2.0
            $ renpy.pause(1.0, hard=True)
            jump end3

        "มือเปล่าสู้เสือทะลุขีดจำกัด(มือเปล่า)":
            jump end4
                            

label end1:
    L "{cps=60}ทุกคน..รวมพลัง!!{/cps}"
    T "{cps=60}จะไหวไหมเนี่ย?!{/cps}"
    play audio "kame_charge.mp3" volume 1.3
    show character1a at Position(xalign=0.1, yalign=1.0), shake
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    show character2a at Position(xalign=0.3, yalign=1.0), shake
    show character3d at Position(xalign=0.4, yalign=1.0), shake
    L "{cps=60}ยาาา!!{/cps}"
    play audio "kame_charge.mp3" volume 1.3
    show character1a at Position(xalign=0.1, yalign=1.0), shake
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    show character2a at Position(xalign=0.3, yalign=1.0), shake
    show character3d at Position(xalign=0.4, yalign=1.0), shake
    R "{cps=60}ยาาาาา!!!{/cps}"
    play audio "kame_charge.mp3" volume 1.3
    show character1a at Position(xalign=0.1, yalign=1.0), shake
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    show character2a at Position(xalign=0.3, yalign=1.0), shake
    show character3d at Position(xalign=0.4, yalign=1.0), shake
    T "{cps=60}ยาาาาาาาาาาาาาาาาาา!!!{/cps}"    
    play audio "kame.mp3" volume 1.3                
    show character1a at Position(xalign=0.1, yalign=1.0), shake
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    show character2a at Position(xalign=0.3, yalign=1.0), shake
    show character3d at Position(xalign=0.4, yalign=1.0), shake           
    P "{cps=60}ยาาาาาาาา!!แค่กก..แค่กๆ{/cps}"

    C "{cps=50}แง่ววว!!!!{/cps}"
    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
    play audio "strongpunch.mp3" volume 0.3
    $ renpy.pause(2.0, hard=True)

    L "{cps=60}เป็นไงบ้าง?..มันตายไหม?{/cps}"

    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
    C "{cps=50}แง่ววววววววววววววววว!!!!!!!!!!!!!!!!{/cps}"
    
    L "{cps=60}โถ่เอ้ย! มันยังไม่ตาย!!{/cps}"
    L "{cps=60}ไม่มีแรงขับเสียงร้องพลังเลยลดลง บ้าเอ้ย!{/cps}"

    C "{cps=50}แง่วว.............{/cps}"
    L "{cps=60}เหอ!?{/cps}"
    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
    C "{cps=50}แง่วววววววววววววววววววววววววววววววว!!!!!!!!!!!!!!!!!!!!!{/cps}"


    L "{cps=50}หะเอื้ออออออออออออ!!!!!!!!!!!!!!!!!!!!{/cps}"
    show character1a at Position(xalign=0.1, yalign=1.0), shake
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    show character2a at Position(xalign=0.3, yalign=1.0), shake
    show character3d at Position(xalign=0.4, yalign=1.0), shake
    play audio "strongpunch.mp3" volume 0.3
    everyone "{cps=50}รางไม่ดีอีกแล้วววววววววว!!!!!!!!!{/cps}"
    stop music fadeout 2.0
    $ renpy.pause(1.0, hard=True)

    play audio "super-mario-death-sound-sound-effect.mp3" volume 0.6
    hide character0 with dissolve
    hide character1a with dissolve
    hide character3d with dissolve
    hide character2a with dissolve
    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
    C "{cps=50}แง่ววววววว!!!!!!!!!!!!!!!!!!!!!{/cps}"

    scene black with fade
    $ renpy.pause(1.0, hard=True)    
    play music "Loop Hero.mp3" volume 0.3 fadein 2.0
    scene hospital
    with dissolve
    show text "{cps=30}เพราะการตัดสินใจอันผิดพลาดทำให้ตุยยกฝูง ลาก่อนเหล่าผู้รอดชีวิต \nยินดีด้วยคุณจบเกมแบบ กลับบ้านเก่า แล้ว{/cps}" with dissolve
    pause 60 
    return    

label end2:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    play music "Loop Hero.mp3" volume 0.3 fadein 2.0
    scene hospital
    show character3a2 at Position(xalign=0.65, yalign=1.0)
    show character1 at Position(xalign=0.45, yalign=1.0)
    show character2 at Position(xalign=0.22, yalign=1.0)
    show character0a2 at Position(xalign=0.80, yalign=1.0)
    with dissolve
    L "{cps=60}สำเร็จ! จัดการได้แล้ว!{/cps}"
    P "{cps=60}ดูนั่น! มีบางอย่างปรากฎออกมา{/cps}"

    hide character3a2
    hide character1
    hide character2
    hide character0a2
    show portal 
    with dissolve
    everyone "{cps=30}..?!{/cps}"

    play audio "portal_EIeiKty.mp3" volume 0.3
    show portal at Position(xalign=0.95, yalign=1.0)
    show character3a2 at Position(xalign=-0.07, yalign=1.0)
    show character2b at Position(xalign=0.31, yalign=1.0)
    show character12 at Position(xalign=0.11, yalign=1.0)
    show character0a2 at Position(xalign=0.45, yalign=1.0)
    with dissolve
    $ renpy.pause(1.0, hard=True)
    show character3a2 at Position(xalign=-0.07, yalign=1.0), fade_away
    show character2b at Position(xalign=0.31, yalign=1.0), fade_back
    show character12 at Position(xalign=0.11, yalign=1.0), fade_away
    show character0a2 at Position(xalign=0.45, yalign=1.0), fade_away
    R "{cps=60}นั่น..อะไรน่ะ ประตูเหรอ{/cps}"
    show character3a2 at Position(xalign=-0.07, yalign=1.0), fade_back
    show character2b at Position(xalign=0.31, yalign=1.0), fade_away
    show character12 at Position(xalign=0.11, yalign=1.0), fade_away
    show character0a2 at Position(xalign=0.45, yalign=1.0), fade_away
    T "{cps=60}ฉันว่านี่แหละทางออก{/cps}"
    show character3a2 at Position(xalign=-0.07, yalign=1.0), fade_away
    show character2b at Position(xalign=0.31, yalign=1.0), fade_away
    show character12 at Position(xalign=0.11, yalign=1.0), fade_away
    show character0a2 at Position(xalign=0.45, yalign=1.0), fade_back
    L "{cps=60}งั้นเหรอ ได้เวลาออกจากที่นี่แล้วสินะ{/cps}"
    show character3a2 at Position(xalign=-0.07, yalign=1.0), fade_back
    show character2b at Position(xalign=0.31, yalign=1.0), fade_back
    show character12 at Position(xalign=0.11, yalign=1.0), fade_back
    show character0a2 at Position(xalign=0.45, yalign=1.0), fade_back
    everyone "{cps=60}*สัมผัส..*{/cps}"

    hide character3a2
    hide character2b
    hide character12
    hide character0a2
    hide portal
    with dissolve

    show text "{cps=30}หลังจากสัมผัสทุกคนก็ถูกวาปกลับไปยังที่อยู่ของแต่ละคน \nยินดีด้วยคุณจบเกมแบบ หลายหัวดีกว่าหัวเดียว แล้ว {/cps}" with dissolve
    pause 60 
    return

label end3:
    scene black with fade
    $ renpy.pause(1.0, hard=True)
    play music "Loop Hero.mp3" volume 0.3 fadein 2.0
    scene hospital
    show character0a
    with dissolve
    L "{cps=60}หนีรอดแล้วสินะ คราวหน้าแกเจอฉันแน่!{/cps}"
    hide character0a
    with dissolve
    show text "{cps=30}นั่นเป็นการตัดสินใจที่ผิดพลาด สัตว์ประหลาดนั่นก็ไม่เคยปรากฏออกมาให้เขาเห็นอีกเลยและเขาติดอยู่ที่นี่ตลอดกาล \nยินดีด้วยคุณจบเกมแบบ ติดเกาะแล้วล่ะ แล้ว{/cps}" with dissolve
    pause 60
    return

label end4:
    scene background
    show character0 at Position(xalign=0.2, yalign=1.0)
    show capiparaboss battle at Position(xalign=0.8, yalign=0.4)

    L "{cps=60}ยาาา!!!!!!!!!!!!!{/cps}"

    show capiparaboss battle at Position(xalign=0.8, yalign=0.4), shake
    play audio "strongpunch.mp3" volume 0.3
    $ renpy.pause(1.0, hard=True)
    show character0 at Position(xalign=0.2, yalign=1.0), shake
    play audio "strongpunch.mp3" volume 0.3
    $ renpy.pause(1.0, hard=True)
    L "{cps=30}*อึ่ก..*{/cps}"
    L "{cps=60}เป็นยังไงบ้าง..{/cps}"

    C "{cps=90}แง่กกก!!{/cps}"
    play audio "death-bong.mp3" volume 0.3
    hide capiparaboss battle with dissolve

    L "{cps=60}สะ..สำเร็จ!{/cps}"
    play audio "kids-saying-yay-sound-effect_2.mp3" volume 0.4
    stop music fadeout 2.0

    scene black with fade
    $ renpy.pause(1.0, hard=True)
    play music "Loop Hero.mp3" volume 0.3 fadein 2.0
    scene city
    show character0a
    with dissolve

    L "{cps=60}มือเปล่านี่แหละเจ๋งจริง{/cps}"

    play audio "portal_EIeiKty.mp3" volume 0.3
    show character0a at Position(xalign=0.1, yalign=1.0)
    show portal at Position(xalign=0.95, yalign=1.0)
    with dissolve

    L "{cps=60}นั่น..อะไรน่ะ ประตูเหรอ{/cps}"
    L "{cps=60}*สัมผัส..*{/cps}"

    hide character0a with dissolve
    hide portal with dissolve

    show text "{cps=30}หลังจากสัมผัสก็โดนวาปกลับบ้าน \nยินดีด้วยคุณจบเกมแบบ นักสู้ผู้โดดเดี่ยว แล้ว {/cps}" with dissolve
    pause 60 
    return