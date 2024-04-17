import pygame

class Vector2Helper(object):
    
    @staticmethod
    def add(v1: pygame.math.Vector2, v2: pygame.math.Vector2) -> pygame.math.Vector2:
        rs = pygame.math.Vector2((v1.x + v2.x), (v1.y + v2.y))
        return rs
    
    @staticmethod
    def sub(v1: pygame.math.Vector2, v2: pygame.math.Vector2) -> pygame.math.Vector2:
        rs = pygame.math.Vector2((v1.x - v2.x), (v1.y - v2.y))
        return rs
    
    @staticmethod
    def mult(v1: pygame.math.Vector2, value: int) -> pygame.math.Vector2:
        rs = pygame.math.Vector2((v1.x * value), (v1.y * value))
        return rs
    
    @staticmethod
    def div(v1: pygame.math.Vector2, value: int) -> pygame.math.Vector2:
        rs = pygame.math.Vector2((v1.x / value), (v1.y / value))
        return rs
    
    @staticmethod
    def mag(v1: pygame.math.Vector2) -> pygame.math.Vector2:
        rs = pygame.math.Vector2((v1.x * v1.x), (v1.y * v1.y))
        return rs
    
    @staticmethod
    def normalize(v1: pygame.math.Vector2) -> pygame.math.Vector2:
        rs = pygame.math.Vector2(v1.x, v1.y)
        m = Vector2Helper.mag(v1)
        if m > 0:
            rs = Vector2Helper.div(m)
        return rs
    
    @staticmethod
    def round(v1: pygame.math.Vector2) -> tuple:
        return (round(v1.x), round(v1.y))
