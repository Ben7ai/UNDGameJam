import pygame
import math
import random

pygame.init()

font = pygame.font.Font(None, 36)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SEA_BLUE = (0, 69, 94)

# Define screen size
SCREEN_SIZE = (1080, 720)

class Boat(pygame.sprite.Sprite):
    def __init__(self, sprite_path, speed=0, angle=0, spin_cooldown=0, spin_cooldown_duration=360):
        super().__init__()
        self.image = pygame.image.load(sprite_path)
        self.rect = self.image.get_rect(center=(SCREEN_SIZE[0] // 2, SCREEN_SIZE[1] // 2))
        self.speed = speed
        self.angle = angle
        self.spin_cooldown = spin_cooldown
        self.spin_cooldown_duration = spin_cooldown_duration
        self.spin_target_angle = None
        self.spin_animation_frames = 60

    def update(self, keys=None):
        if keys is not None:
            if keys[pygame.K_w]:
                self.speed += 0.3
            if keys[pygame.K_a]:
                self.angle -= 3
            elif keys[pygame.K_d]:
                self.angle += 3
        
        if self.spin_cooldown > 0:
            self.spin_cooldown -= 1
            if self.spin_animation_frames:
                self.angle = ((self.spin_target_angle - self.angle) / self.spin_animation_frames) + self.angle
                self.spin_animation_frames -= 1
            else:
                self.angle = self.spin_target_angle

        self.speed *= 0.9

        if self.spin_cooldown > 0:
            self.spin_cooldown -= 1

        x_movement = self.speed * math.cos(math.radians(self.angle))
        y_movement = self.speed * math.sin(math.radians(self.angle))

        self.rect.x += x_movement
        self.rect.y += y_movement

        self.rect.x %= SCREEN_SIZE[0]
        self.rect.y %= SCREEN_SIZE[1]

    def draw(self, screen):
        rotated_boat = pygame.transform.rotate(self.image, -self.angle)
        screen.blit(rotated_boat, rotated_boat.get_rect(center=self.rect.center))

class PlayerBoat(Boat):
    def __init__(self, sprite_path="assets/sprites/player.png"):
        super().__init__(sprite_path)

class EnemyBoat(Boat):
    def __init__(self, sprite_path="assets/sprites/enemy.png", target=None):
        super().__init__(sprite_path)
        self.target = target
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        if self.target is not None:  # Check if target is not None before calling ai_behavior
            self.ai_behavior(self.target)  # Pass the target explicitly


    def ai_behavior(self, target):
        # Calculate the vector from the enemy boat to the target
        dx = target.rect.x - self.rect.x
        dy = target.rect.y - self.rect.y
        distance = math.sqrt(dx**2 + dy**2)
        
        # Normalize the vector to get the direction
        if distance!= 0:
            dx /= distance
            dy /= distance
        
        # Calculate the angle towards the target
        target_angle = math.degrees(math.atan2(dy, dx)) % 360
        
        # Gradually turn the enemy boat towards the target angle
        if abs(target_angle - self.angle) > 5:  # Only turn if the difference is significant
            if target_angle > self.angle:
                self.angle += 5  # Turn right
            else:
                self.angle -= 5  # Turn left
                
        # Move towards the target
        self.speed = 3  # Set a constant speed for simplicity
        
        min_distance = 100  # Adjust based on your boat sizes
        if distance < min_distance:
            self.speed = 0  # Stop moving if too close
        else:
            self.speed = 3  # Normal speed

    def update(self, target=None):
        if target is not None:
            self.ai_behavior(target)
        else:
            super().update(None)  # Call the parent class's update method without keys

def draw_screen(screen, boat):
    screen.fill(SEA_BLUE)
    boat.draw(screen)
    
    if isinstance(boat, EnemyBoat):
        cooldown_seconds = round(boat.spin_cooldown / 60)
        cooldown_text = font.render(f"Cooldown: {cooldown_seconds}s", True, WHITE)
        screen.blit(cooldown_text, (10, 10))
        
def spawn_enemy(screen_width, screen_height, sprite_path="assets/sprites/enemy.png"):
    # Create a dummy target for the temporary EnemyBoat
    dummy_target = pygame.Rect(0, 0, 1, 1)  # A single pixel rect

    # Create an instance of EnemyBoat to get its dimensions
    temp_enemy_boat = EnemyBoat(sprite_path, target=dummy_target)
    enemy_boat_width = temp_enemy_boat.width
    enemy_boat_height = temp_enemy_boat.height
    
    # Delete the temporary instance to free resources
    del temp_enemy_boat
    
    # Generate a random position within the screen boundaries
    x_position = random.randint(0, screen_width - enemy_boat_width)
    y_position = random.randint(0, screen_height - enemy_boat_height)
    
    # Create an instance of EnemyBoat at the random position with the actual target
    enemy_boat = EnemyBoat(sprite_path)
    enemy_boat.rect.center = (x_position, y_position)
    enemy_boat.target = dummy_target  # Assign the dummy target to the actual EnemyBoat
    
    return enemy_boat
    
def main():
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Boat Game")
    clock = pygame.time.Clock()

    player_boat = PlayerBoat()
    enemy_boat = spawn_enemy(*SCREEN_SIZE)  # Spawn the first enemy boat

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        player_boat.update(keys)
        enemy_boat.update(player_boat)
        
        draw_screen(screen, player_boat)

        pygame.display.flip()
        clock.tick(60) / 1000

    pygame.quit()

if __name__ == "__main__":
    main()
