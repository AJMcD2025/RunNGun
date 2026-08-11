import pygame

from characters.player import Player
from weapons.smg import SMG
from pickups.health_pickup import HealthPickup

def main():
    pygame.init()

    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    bullets_group = pygame.sprite.Group()
    pickups_group = pygame.sprite.Group()

    player = Player(
        pos=(200, 300),
        weapon=SMG(),
        bullets_group=bullets_group,
        pickups_group=pickups_group
    )

    pickups_group.add(HealthPickup((400, 300)))

    running = True
    while running:
        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)
        bullets_group.update(dt, [])
        pickups_group.update(dt)

        screen.fill("black")

        pickups_group.draw(screen)
        bullets_group.draw(screen)
        screen.blit(player.image, player.rect)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()