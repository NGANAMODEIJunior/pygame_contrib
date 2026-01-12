import pygame

def test_fill_keywords_basic():
    surf = pygame.Surface((20, 20), pygame.SRCALPHA)
    rect = pygame.Rect(5, 5, 10, 10)
    color = (10, 200, 30, 255)

    surf.fill(color=color, rect=rect)

    # Inside rect → color must match
    assert surf.get_at((10, 10)) == color

    # Outside rect → must be unchanged (0,0,0,0)
    assert surf.get_at((0, 0)) != color
