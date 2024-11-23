import pygame
import Peca as peca
class Jogo:
    def __init__(self):
        self.tamanhoX = 0
        self.tamanhoY = 0
        self.fundo = ""

    def buscaConfiguracoes(self):
        self.tamanhoX = 1000
        self.tamanhoY = 1000
        self.fundo = "white"
        conf = {"tamanhoX": self.tamanhoX,"tamanhoY": self.tamanhoY,"fundo": self.fundo }
        return conf

    def iniciar(self):
        conf = self.buscaConfiguracoes()
        self.loop(conf)
    def finalizar(self):
        pass

    def exibirConjuntos(self):
        peca.Peca.criaAtomo(self)

    def loop(self, conf):
        pygame.init()
        screen = pygame.display.set_mode((conf["tamanhoX"], conf["tamanhoY"]))
        clock = pygame.time.Clock()
        running = True
        dt = 0
        player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            screen.fill(conf["fundo"])

            pygame.draw.circle(screen, "red", player_pos, 40)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                player_pos.y -= 800 * dt
                peca_instance = peca.Peca()
                peca_instance.criaAtomo()
            if keys[pygame.K_s]:
                player_pos.y += 800 * dt
            if keys[pygame.K_a]:
                player_pos.x -= 800 * dt
            if keys[pygame.K_d]:
                player_pos.x += 800 * dt

            pygame.display.flip()

            # limits FPS to 60
            # dt is delta time in seconds since last frame, used for framerate-
            # independent physics.
            dt = clock.tick(60) / 1000

        pygame.quit()