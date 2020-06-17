import arcade


VELOCIDADEDEMOVIMENTO = 8
VELOCIDADEPULO =23
GRAVIDADE = 1.3

DIMENSAO_LARGURA = 100*128
DIMENSAO_ALTURA = 8*128
LARGURA_TILE = 128

JANELA_LARGURA = 1366
JANELA_ALTURA = 768

METADE_LARGURA = JANELA_LARGURA//2

class InstrucoesView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("A floresta está em risco!", JANELA_LARGURA/2, JANELA_ALTURA/2,
                         arcade.color.BLACK, font_size=50, anchor_x="center")
        arcade.draw_text("Para Salva-la,colete todo o lixo", JANELA_LARGURA/2, JANELA_ALTURA/2-75,
                         arcade.color.GRAY, font_size=30, anchor_x="center")
        arcade.draw_text("Use as setas para se movimentar", JANELA_LARGURA/2, JANELA_ALTURA/2-95,
                         arcade.color.GRAY, font_size=30, anchor_x="center")
        arcade.draw_text("Clique para Iniciar", JANELA_LARGURA / 2, JANELA_ALTURA / 2 - 115,
                         arcade.color.GRAY, font_size=30, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        janelagame = JanelaGame(JANELA_LARGURA, JANELA_LARGURA, "SALVADORES DA FLORESTA")
        self.window.show_view(janelagame)

class FlorestaSalva(arcade.View):

    def __init__(self):

        super().__init__()
        self.texture = arcade.load_texture("SPRITES/florestasalva.png")

        arcade.set_viewport(0, DIMENSAO_LARGURA - 1, 0, DIMENSAO_ALTURA - 1)

    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(DIMENSAO_LARGURA / 2, DIMENSAO_ALTURA / 2,
                                DIMENSAO_LARGURA, DIMENSAO_ALTURA)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        janelagame = JanelaGame(JANELA_LARGURA,JANELA_ALTURA,"SALVADORES DA FLORESTA")
        janelagame.setup()
        self.window.show_view(janelagame)

class MenuView(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.LIGHT_MOSS_GREEN)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Salvadores da Floresta", JANELA_LARGURA/2, JANELA_ALTURA/2,
                         arcade.color.BLACK, font_size=80, anchor_x="center")
        arcade.draw_text("Clique para Iniciar", JANELA_LARGURA/2, JANELA_ALTURA/2-75,
                         arcade.color.BLACK, font_size=20, anchor_x="center")


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instrucoes_view = InstrucoesView()
        self.window.show_view(instrucoes_view)



class JanelaGame(arcade.View):
    def __init__(self,width, height, title):
        super().__init__()


        arcade.set_background_color(arcade.color.RED)

        self.ground_list = None
        self.player_list = None
        self.player = None
        self.player_engine = None
        self.player_papel = 0
        self.player_vidro = 0
        self.player_plastico = 0
        self.player_organico = 0

        self.setup()


    def setup(self):
        fundo_layer = 'FUNDO'
        fundo_garrafav = 'GARRAFAV'
        fundo_garrafap = 'GARRAFAP'
        fundo_pisoplataforma = 'PLATAFORMASPISO'
        fundo_papel = 'PAPEL'
        fundo_organico = 'MACA'
        lixeira_plastico = 'LIXEIRAPLASTICO'
        lixeira_vidro = 'LIXEIRAVIDRO'
        lixeira_papel = 'LIXEIRAPAPEL'
        lixeira_organica = 'LIXEIRAORGANICA'
        carrega_mapa = arcade.tilemap.read_tmx("maps/MAPATILE.tmx")
        self.camadafundo = arcade.tilemap.process_layer(carrega_mapa,fundo_layer)
        self.camadafundo2 = arcade.tilemap.process_layer(carrega_mapa, fundo_garrafav)
        self.camadafundo3 = arcade.tilemap.process_layer(carrega_mapa, fundo_garrafap)
        self.camadafundo4 = arcade.tilemap.process_layer(carrega_mapa, fundo_pisoplataforma)
        self.camadafundo5 = arcade.tilemap.process_layer(carrega_mapa, fundo_papel)
        self.camadafundo6 = arcade.tilemap.process_layer(carrega_mapa, fundo_organico)
        self.camadafundo7 = arcade.tilemap.process_layer(carrega_mapa, lixeira_papel)
        self.camadafundo8 = arcade.tilemap.process_layer(carrega_mapa, lixeira_plastico)
        self.camadafundo9 = arcade.tilemap.process_layer(carrega_mapa, lixeira_vidro)
        self.camadafundo10 = arcade.tilemap.process_layer(carrega_mapa, lixeira_organica)


        self.player_list = arcade.SpriteList()
        self.player = arcade.AnimatedWalkingSprite()

        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Idle (1).png"))

        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Idle (1).png", mirrored=True))

        self.player.walk_right_textures = []
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (1).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (2).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (3).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (4).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (5).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (6).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (7).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (8).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (9).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (10).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (11).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (12).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (13).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (14).png"))
        self.player.walk_right_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (15).png"))

        self.player.walk_left_textures = []
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (1).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (2).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (3).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (4).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (5).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (6).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (7).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (8).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (9).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (10).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (11).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (12).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (13).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (14).png", mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("SPRITES/PERSONAGEM/Walk (15).png", mirrored=True))


        self.player.scale = 0.4
        self.player.center_x = 1366//2
        self.player.center_y = 768//2

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player,self.camadafundo4,gravity_constant=GRAVIDADE)

        self.player_list.append(self.player)


    def on_draw(self):
        arcade.start_render()
        self.camadafundo.draw()
        self.camadafundo2.draw()
        self.camadafundo3.draw()
        self.camadafundo4.draw()
        self.camadafundo5.draw()
        self.camadafundo6.draw()
        self.camadafundo7.draw()
        self.camadafundo8.draw()
        self.camadafundo9.draw()
        self.camadafundo10.draw()
        self.player_list.draw()
        arcade.draw_text(f"Plastico:{self.player_plastico}",arcade.get_viewport()[0]+10,arcade.get_viewport()[2]+800,arcade.color.BROWN,font_size= 32)
        arcade.draw_text(f"Papel:{self.player_papel}", arcade.get_viewport()[0] + 10,arcade.get_viewport()[2] + 770, arcade.color.BROWN, font_size=32)
        arcade.draw_text(f"Vidro:{self.player_vidro}", arcade.get_viewport()[0] + 10,arcade.get_viewport()[2] + 740, arcade.color.BROWN, font_size=32)
        arcade.draw_text(f"Organico:{self.player_organico}", arcade.get_viewport()[0] + 10,arcade.get_viewport()[2] + 707, arcade.color.BROWN, font_size=32)
    def clamp(self,valor,mini,maxi):
        return max(min(valor,maxi),mini)
    def on_update(self, delta_time):
        self.player_list.update()
        self.player_list.update_animation()
        self.physics_engine.update()

        self.player.center_x = self.clamp(self.player.center_x, 0, DIMENSAO_LARGURA)

        if self.player.center_x >  METADE_LARGURA and self.player.center_x <  DIMENSAO_LARGURA-LARGURA_TILE-METADE_LARGURA:
            change_view = True
        else:
            change_view = False

        if change_view:
            arcade.set_viewport(self.player.center_x - METADE_LARGURA,self.player.center_x + METADE_LARGURA,0,JANELA_ALTURA+300)

        colisao_plastico = arcade.check_for_collision_with_list(self.player,self.camadafundo3)
        colisao_vidro = arcade.check_for_collision_with_list(self.player, self.camadafundo2)
        colisao_papel = arcade.check_for_collision_with_list(self.player, self.camadafundo5)
        colisao_organico = arcade.check_for_collision_with_list(self.player, self.camadafundo6)
        colisao_lixeirapapel = arcade.check_for_collision_with_list(self.player,self.camadafundo7)
        colisao_lixeiraplastico = arcade.check_for_collision_with_list(self.player, self.camadafundo8)
        colisao_lixeiravidro = arcade.check_for_collision_with_list(self.player, self.camadafundo9)
        colisao_lixeiraorganica = arcade.check_for_collision_with_list(self.player, self.camadafundo10)

        if (colisao_lixeiraorganica == True):
            view = FlorestaSalva()
            self.window.show_view(view)


        for plastico in colisao_plastico:
            self.player_plastico += 1
            plastico.kill()
        for vidro in colisao_vidro:
            self.player_vidro += 1
            vidro.kill()
        for papel in colisao_papel:
            self.player_papel += 1
            papel.kill()
        for organico in colisao_organico:
            self.player_organico += 1
            organico.kill()
        for lixopapel in colisao_lixeirapapel:
            self.player_papel = self.player_papel-self.player_papel
            lixopapel.update()

        for lixoplastico in colisao_lixeiraplastico:
            self.player_plastico = self.player_plastico - self.player_plastico
            lixoplastico.update()
        for lixovidro in colisao_lixeiravidro:
            self.player_vidro = self.player_vidro - self.player_vidro
            lixovidro.update()
        for lixoorganico in colisao_lixeiraorganica:
            self.player_organico = self.player_organico -self.player_organico
            lixoorganico.update()
            view = FlorestaSalva()
            self.window.show_view(view)


    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.RIGHT:
            self.player.change_x = VELOCIDADEDEMOVIMENTO
        if symbol == arcade.key.LEFT:
            self.player.change_x = -VELOCIDADEDEMOVIMENTO
        if symbol == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player.change_y = VELOCIDADEPULO
    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player.change_x = 0


def main():
    window = arcade.Window(JANELA_LARGURA, JANELA_ALTURA, "Salvadores da Floresta",resizable=True)
    menu_view = MenuView()
    window.show_view(menu_view)
    arcade.run()

if __name__ == "__main__":
    main()


