init python:
    installed_pack_images = dict()
    class PackImage:
        def __init__(self, name, file):
            self.name = name
            self.file = file
        def __repr__(self):
            return "(%s, %s)" % (self.name, self.file)
    def swap_pack_image(pack_name, current, shift):
        global packmodimage
        pack_images = installed_pack_images.get(pack_name.lower(), list())
        if current is None:
            packmodimage = pack_images[0].file
            return
        for idx, image in enumerate(pack_images):
            if current == image.name or current == image.file:
                packmodimage = pack_images[(idx + shift) % len(pack_images)].file
                return
        packmodimage = pack_images[0].file
        return
    def install_pack(pack_name, *images):
        pack_images = installed_pack_images.setdefault(pack_name.lower(), list())
        for i, image in enumerate(images):
            pack_images.append(PackImage(str(i+1), image))
    install_pack(
        "Вестник",
        "mods/packmod/Images/vestnik/letter01rus.png",
        "mods/packmod/Images/vestnik/letter02rus.png",
        "mods/packmod/Images/vestnik/letter03rus.png"
    )
    install_pack(
        "Журнал Юты",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal1.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal2.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal3.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal4.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal5.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal6.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal7.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal8.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal9.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal10.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal11.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal12.png",
        "mods/packmod/Images/Utas_Love_Journal/Utas_Love_Journal13.png",
    )
    install_pack(
        "Секретное досье",
        "mods/packmod/Images/Sensitive_Information/Chika_Chosokabe.png",
        "mods/packmod/Images/Sensitive_Information/Kaori_Kadowaki.png",
        "mods/packmod/Images/Sensitive_Information/Karin_Kanda.png",
        "mods/packmod/Images/Sensitive_Information/Maki_Miyamura.png",
        "mods/packmod/Images/Sensitive_Information/Osako_Osaka.png",
        "mods/packmod/Images/Sensitive_Information/Noriko_Nakayama.png",
        "mods/packmod/Images/Sensitive_Information/Sara_Sakakibara.png",
        "mods/packmod/Images/Sensitive_Information/Ayane_Amamiya.png"
    )
    class Vestnik:
        def __init__(self, password, hint, image):
            self.password = password
            self.hint = hint
            self.image = image
    vestnicdict = {
        "vestnik1" : Vestnik("славься", 'ЛЮБИМОЕ СЛОВО ЯСУ', "mods/packmod/Images/vestnik/letter01rus.png"),
        "vestnik2" : Vestnik("лето", 'ЖАРКОЕ ВРЕМЯ ГОДА', "mods/packmod/Images/vestnik/letter02rus.png"),
        "vestnik3" : Vestnik("захариэль", 'КРОЛИК С ЧАЕПИТИЯ', "mods/packmod/Images/vestnik/letter03rus.png")
    }
    def changevestnik(vestnik):
        global value
        # renpy.show_screen('dialog', message=vestnicdict[vestnik].hint, ok_action=Function(renpy.hide_screen, 'dialog'))
        if value.lower() == vestnicdict[vestnik].password:
            globals()[vestnik] = True
            renpy.hide_screen("value_input")
            value = ''
            renpy.show_screen('vestnik', vestnicdict[vestnik].image)
        else:
            renpy.hide_screen("value_input")
            value = ''
            renpy.show_screen('dialog', message="НЕПРАВИЛЬНО!\nПробуй снова!", ok_action=Function(renpy.hide_screen, 'dialog'))       