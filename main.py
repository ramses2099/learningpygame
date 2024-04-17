import pygame
import math, random
from Vector2Helper import Vector2Helper

# Global variables
images = {}
SCREEN_SIZE = (800, 600)
TITLE = "Pygame - FPS: "
FPS = 60
# Set up color
BLACK = (0, 0, 0)
WHITE = (255, 255, 225)

class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, position):
      pygame.sprite.Sprite.__init__(self)
      self.image = image
      self.rect = image.get_rect(center=Vector2Helper.round(position))
      # movement
      self.position = position
      self.velocity = pygame.math.Vector2(1, 0)
      self.acceleration = pygame.math.Vector2(0,0)
      self.maxspeed = 8
      self.maxforce = 0.2
      
    def update(self, dt) -> None:
        self.position += self.velocity
        self.rect.center = Vector2Helper.round(self.position)
        
    def applyForce(self, force) -> None:
        self.acceleration += force



class Game:
    def __init__(self) -> None:
        pygame.init()
        
        self.clock = pygame.time.Clock()
        self.running = False
        self.fps = 0.0
        
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        # delcaration
        self.group: pygame.sprite.Group
        self.vehicle: Vehicle
       
        # init all object
        self.init()
        
    def load_image(self, image_name) -> None:
        image = pygame.image.load(f'assets/{image_name}.png').convert()
        images[image_name] = image
        
    def init(self) -> None:
       self.group = pygame.sprite.Group()
       self.load_image('ship_A')
       self.vehicle = Vehicle(images['ship_A'],pygame.math.Vector2(SCREEN_SIZE[1]/2,
                                                                   SCREEN_SIZE[1]/2))
       self.group.add(self.vehicle)
       
    def update(self, dt) -> None:
       self.group.update(dt)
    
    def draw(self, surface) -> None:
        surface.fill(BLACK)
        # Draw 
        self.group.draw(self.screen)
       
        pygame.display.flip()
        
    def run(self) -> None:
        self.running = True
        
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.fps = self.clock.get_fps()
            pygame.display.set_caption(f'{TITLE} {self.fps}')
            # Event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        self.running = False
                        
            # update and draw
            self.update(dt)
            self.draw(self.screen)          
            

if __name__ == "__main__":
    Game().run()