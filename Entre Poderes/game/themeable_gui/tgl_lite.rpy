## Themeable GUI Lite - the Midnight theme for the textbox, the name tag, the choice menu and the main menu.
##
## Copy the folder themeable_gui/ into game/. Nothing else to do: this file replaces the say, choice and
## main_menu screens of your screens.rpy (it runs after it) and leaves every other screen as it is.
##
## The full Themeable GUI Kit (6 themes switchable in game, every screen, portrait layout for phones):
## https://juliusschmidt.itch.io/renpy-themeable-gui-kit

init offset = 1

init python in tgl:
    import store
    ROOT = "themeable_gui/"
    THEME = ROOT + "themes/midnight/"
    INK, MUTED, BRASS, NAVY = "#F4F1EA", "#BFCBC2", "#B6C9A8", "#435548"
    SERIF = ROOT + "fonts/SourceSerif4-Regular.ttf"
    SERIF_BOLD = ROOT + "fonts/SourceSerif4-Semibold.ttf"

    for _p in ("textbox.png", "namebox.png", "button_idle.png", "button_hover.png", "choice_idle.png", "choice_hover.png", "main_land.jpg"):
        if not renpy.loadable(THEME + _p):
            raise Exception("themeable_gui lite: %s%s is missing. Copy the whole themeable_gui/ folder into game/." % (THEME, _p))

    def scale():
        return min(store.config.screen_width, store.config.screen_height) / 1080.0

    def px(n):
        return int(round(n * scale()))

    def frame(name, l, t, r, b):
        s = scale()
        child = THEME + name + ".png"
        if s != 1.0:
            child = store.Transform(child, zoom=s)
        return store.Frame(child, int(l * s), int(t * s), int(r * s), int(b * s))


## Textbox and name tag (the styles the characters use) ##########################

style window:
    xalign 0.5
    xfill False
    xsize config.screen_width - tgl.px(140)
    yalign 1.0
    ysize tgl.px(260)
    yoffset -tgl.px(35)
    padding (tgl.px(74), tgl.px(48), tgl.px(74), tgl.px(24))
    background tgl.frame("textbox", 50, 46, 50, 46)

style namebox:
    xpos tgl.px(-10)
    xanchor 0.0
    xsize None
    xminimum tgl.px(220)
    ypos -tgl.px(64)
    yanchor 0.5
    ysize tgl.px(66)
    padding (tgl.px(30), tgl.px(8), tgl.px(30), tgl.px(8))
    background tgl.frame("namebox", 26, 14, 26, 14)

style say_label:
    font tgl.SERIF_BOLD
    size tgl.px(36)
    color tgl.INK
    outlines []
    xalign 0.5
    yalign 0.5

style say_dialogue:
    font tgl.SERIF
    size tgl.px(36)
    color tgl.INK
    outlines []
    xpos 0
    xsize None
    xfill True
    ypos 0
    line_spacing tgl.px(8)


screen say(who, what):
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window:
    variant "small"
    xsize config.screen_width - tgl.px(80)


screen input(prompt):
    window:
        vbox:
            xalign 0.0
            xfill True
            yalign 0.5
            spacing tgl.px(16)

            text prompt style "tgl_input_prompt"
            input id "input" style "tgl_input_text"

style tgl_input_prompt:
    font tgl.SERIF
    size tgl.px(36)
    color tgl.INK
    xalign 0.0
    text_align 0.0
    outlines []

style tgl_input_text:
    font tgl.SERIF
    size tgl.px(36)
    color tgl.INK
    xalign 0.0
    xfill True
    text_align 0.0
    outlines []


## Choice menu ####################################################################

screen choice(items):
    vbox:
        style "tgl_choice_vbox"
        for i in items:
            textbutton i.caption action i.action style "tgl_choice_button" text_style "tgl_choice_text"

style tgl_choice_vbox:
    xalign 0.5
    yalign 0.42
    spacing tgl.px(22)

style tgl_choice_button:
    xsize tgl.px(960)
    yminimum tgl.px(86)
    padding (tgl.px(60), tgl.px(18), tgl.px(60), tgl.px(22))
    background tgl.frame("choice_idle", 52, 22, 52, 26)
    hover_background tgl.frame("choice_hover", 52, 22, 52, 26)

style tgl_choice_text:
    font tgl.SERIF_BOLD
    size tgl.px(33)
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color tgl.INK
    hover_color tgl.BRASS
    outlines []


## Main menu ######################################################################

screen main_menu():
    tag menu
    add Transform("images/frenteCongresso_LeonardoSá_AgênciaSenado.png",
        xysize=(config.screen_width, config.screen_height), fit="cover")

    frame:
        style "tgl_main_frame"
        vbox:
            spacing tgl.px(6)
            text "[config.name!t]" style "tgl_main_title"
            text "[config.version]" style "tgl_main_version"
            null height tgl.px(30)
            textbutton _("Início") action Start() style "tgl_nav_button" text_style "tgl_nav_text"
            textbutton _("Carregar") action ShowMenu("load") style "tgl_nav_button" text_style "tgl_nav_text"
            textbutton _("Preferências") action ShowMenu("preferences") style "tgl_nav_button" text_style "tgl_nav_text"
            textbutton _("Sobre") action ShowMenu("about") style "tgl_nav_button" text_style "tgl_nav_text"
            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                textbutton _("Ajuda") action ShowMenu("help") style "tgl_nav_button" text_style "tgl_nav_text"
            if renpy.variant("pc"):
                textbutton _("Sair") action Quit(confirm=False) style "tgl_nav_button" text_style "tgl_nav_text"

style tgl_main_frame:
    xpos tgl.px(110)
    yalign 0.5
    xsize tgl.px(600)
    padding (tgl.px(56), tgl.px(56), tgl.px(56), tgl.px(52))
    background tgl.frame("textbox", 50, 46, 50, 46)

style tgl_main_title:
    font tgl.SERIF_BOLD
    size tgl.px(92)
    color tgl.INK
    outlines []
    line_spacing -tgl.px(10)

style tgl_main_version:
    font tgl.SERIF
    size tgl.px(25)
    color tgl.MUTED
    outlines []

style tgl_nav_button:
    xfill True
    yminimum tgl.px(64)
    padding (tgl.px(44), tgl.px(10), tgl.px(24), tgl.px(10))
    background None
    hover_background None

style tgl_nav_text:
    font tgl.SERIF_BOLD
    size tgl.px(38)
    color tgl.INK
    hover_color tgl.INK
    yalign 0.5
    outlines []
