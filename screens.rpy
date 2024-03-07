screen packmenu():
    tag menu
    add define_mods_images["mod_menu"]
    use menu_mod(_("Пак Меню"), scroll="viewport"):
        style_prefix "aff"
        grid 1 3:
            align (1, 1)
            xspacing 60
            yspacing 20
            imagebutton:
                idle "mods/packmod/Images/vestnik/churchnewhope1.png"
                hover "mods/packmod/Images/vestnik/churchnewhope2.png"
                # action [SetVariable("pack_name", "Вестник"), SetVariable("packmodimage", "mods/packmod/Images/letter01rus.png"), ShowMenu("packmenuimageviewer")]
                action [ShowMenu("packmod_vestnik")]
            imagebutton:
                idle "mods/packmod/Images/Utas_Love_Journal/yutajournal1.png"
                hover "mods/packmod/Images/Utas_Love_Journal/yutajournal2.png"
                action [SetVariable("pack_name", "Журнал Юты"), SetVariable("packmodimage", "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal1.png"), ShowMenu("packmenuimageviewer")]
            imagebutton:
                idle "mods/packmod/Images/Sensitive_Information/secretdossier1.png"
                hover "mods/packmod/Images/Sensitive_Information/secretdossier2.png"
                action [SetVariable("pack_name", "Секретное досье"), SetVariable("packmodimage", "mods/packmod/Images/Sensitive_Information/Chika_Chosokabe.png"), ShowMenu("packmenuimageviewer")]

screen packmod_vestnik():
    tag menu
    add define_mods_images["mod_menu"]
    use menu_mod(_("Вестник"), scroll="viewport"):
        style_prefix "aff"
        grid 5 1:
            align (1, 1)
            xspacing 60
            yspacing 20
            imagebutton:
                idle "mods/packmod/Images/vestnik/vestnikbutton1_1.png"
                hover "mods/packmod/Images/vestnik/vestnikbutton2_1.png"
                action [If(vestnik1 == True, true = [ShowMenu("vestnik", "mods/packmod/Images/vestnik/letter01rus.png")], false = [Show('value_input', message='ЛЮБИМОЕ СЛОВО ЯСУ', ok_action=Function(changevestnik, 'vestnik1'), alloww=None)])]
            imagebutton:
                idle "mods/packmod/Images/vestnik/vestnikbutton1_2.png"
                hover "mods/packmod/Images/vestnik/vestnikbutton2_2.png"
                action [If(vestnik2 == True, true = [ShowMenu("vestnik", "mods/packmod/Images/vestnik/letter02rus.png")], false = [Show('value_input', message='ЖАРКОЕ ВРЕМЯ ГОДА', ok_action=Function(changevestnik, 'vestnik2'), alloww=None)])]
            imagebutton:
                idle "mods/packmod/Images/vestnik/vestnikbutton1_3.png"
                hover "mods/packmod/Images/vestnik/vestnikbutton2_3.png"
                action [If(vestnik3 == True, true = [ShowMenu("vestnik", "mods/packmod/Images/vestnik/letter03rus.png")], false = [Show('value_input', message='КРОЛИК С ЧАЕПИТИЯ', ok_action=Function(changevestnik, 'vestnik3'), alloww=None)])]
            null
            null

screen vestnik(vestnik_image):
    tag menu
    add define_mods_images["mod_menu"]
    frame:
        xalign 0.5  
        add vestnik_image
    hbox:
        style_prefix "quick"
        xalign 0.5
        yalign 1.0
        textbutton _("Выйти") action ShowMenu("packmod_vestnik")

screen packmenuimageviewer():
    tag menu
    add define_mods_images["mod_menu"]
    frame:
        xalign 0.5  
        add packmodimage
    use packmodbar

screen packmodbar():
    zorder 100
    hbox:
        style_prefix "quick"
        xalign 0.5
        yalign 1.0
        textbutton _("Предыдущая") action [Function(swap_pack_image, pack_name, packmodimage, -1)]
        textbutton _("Выйти") action ShowMenu("packmenu")
        textbutton _("Следующая") action [Function(swap_pack_image, pack_name, packmodimage, 1)]