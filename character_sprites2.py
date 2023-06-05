import pygame
def check_hero_chosen(hero,player):
    if hero==0:
        player_size=128
        player_scale=2
        if player==1:
            player_offset=[40,47]
        else:
            player_offset=[50,47]
        kroki_animacji=[5,9,8,2,6,4,5,7,2]
        postac="Samurai_Commander/"
        sprajty=["Idle.png","Walk.png","Run.png","Hurt.png","Dead.png","Attack_1.png","Attack_2.png","Jump.png","Protect.png"]
        tekstury=generate_sprites(postac,sprajty)
        player_data=[[player_size,player_scale,player_offset],tekstury,kroki_animacji]
        return player_data
    elif hero==1:
        player_size=128
        player_scale=2
        if player==1:
            player_offset=[12,47]
        else:
            player_offset=[76,47]
        kroki_animacji=[6,9,8,3,6,4,4,9,2]
        postac="Samurai_Warrior/"
        sprajty=["Idle.png","Walk.png","Run.png","Hurt.png","Dead.png","Attack_1.png","Attack_3.png","Jump.png","Protection.png"]
        tekstury=generate_sprites(postac,sprajty)
        player_data=[[player_size,player_scale,player_offset],tekstury,kroki_animacji]
        return player_data
    elif hero==2:
        player_size=128
        player_scale=2
        if player==1:
            player_offset=[38,47]
        else:
            player_offset=[48,47]
        kroki_animacji=[8,7,8,4,4,7,9,8,6]
        postac="Nomad_Mage/"
        sprajty=["Idle.png","Walk.png","Run.png","Hurt.png","Dead.png","Attack_1.png","Attack_2.png","Jump.png","matemp.png"]
        tekstury=generate_sprites(postac,sprajty)
        player_data=[[player_size,player_scale,player_offset],tekstury,kroki_animacji]
        return player_data
    elif hero==3:
        player_size=128
        player_scale=2
        if player==1:
            player_offset=[32,47]
        else:
            player_offset=[56,47]
        kroki_animacji=[7,7,6,3,5,4,4,6]
        postac="Skeleton_Spearman/"
        sprajty=["Idle.png","Walk.png","Run.png","Hurt.png","Dead.png","Attack_1.png","Attack_2.png","Jump.png"]
        tekstury=generate_sprites(postac,sprajty)
        player_data=[[player_size,player_scale,player_offset],tekstury,kroki_animacji]
        return player_data
    else:
        player_size=128
        player_scale=2
        player_offset=[40,47]
        kroki_animacji=[5,8,9,2,6,4,5,7,2]
        postac="Samurai_Commander/"
        sprajty=["Idle.png","Walk.png","Run.png","Hurt.png","Dead.png","Attack_1.png","Attack_3.png","Jump.png","Protection.png"]
        generate_sprites(postac,sprajty)
        player_data=[[player_size,player_scale,player_offset],tekstury,kroki_animacji]
        return player_data

def generate_sprites(sciezka,lista_sprajtow):
    gracz_tekstury=[]
    for i in lista_sprajtow:
        sciezka_do_tekstury="assets/images/characters/sprites/"+sciezka+i
        gracz_tekstura=pygame.image.load(sciezka_do_tekstury).convert_alpha()
        gracz_tekstury.append(gracz_tekstura)
    return gracz_tekstury