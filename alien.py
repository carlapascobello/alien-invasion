import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
  """A class to represent a single alien in the fleet."""

  def __init__(self, ai_game):
    """Initialize the alien and set its starting position."""
    super().__init__()
    self.screen = ai_game.screen
    self.settings = ai_game.settings

    # Load the alien image and set its rect attribute.
    self.image = pygame.image.load('images/ship.bmp')
    self.rect = self.image.get_rect()

    # Start each new alien near the top left of the screen.
    self.rect.x = self.rect.width
    self.rect.y = self.rect.height

    # Store the alien's exact horizontal position.
    self.x = float(self.rect.x)
  
  def check_edges(self):
    """Return True of alien is at edge of screen."""
    screen_rect = self.screen.get_rect()
    if self.rect.right >= screen_rect.right or self.rect.left <= 0:
      return True
  
  def update(self):
    """Move the alien right or left."""
    self.x += (self.settings.alien_speed * self.settings.fleet_direction)
    self.rect.x = self.x
  
  def _check_fleet_edges(self):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in self.aliens.sprite():
      if alien.check.edges():
        self._change_fleet_direction()
        break
      
  def _change_fleet_direction(self):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in self.aliens.sprites():
      alien.rect.y += self.settings.fleet_drop_speed
    self.settings.fleet_direction *= -1
