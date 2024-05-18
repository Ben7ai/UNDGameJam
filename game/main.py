import pygame
import math


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SEA_BLUE = (0, 69, 94)

# Define screen size
WIDTH = 1080
HEIGHT = 720

# Define boat sprite properties
boat_image = pygame.image.load("Assets/boat.png")  # Replace with your boat image path
boat_rect = boat_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
boat_speed = 0  # Initial boat speed
boat_angle = 0  # Initial boat angle (rotation)
spin_cooldown = 0  # Initial cooldown timer for spacebar (ticks)
spin_cooldown_duration = 100  # Cooldown duration in ticks (adjust as needed)

def update_boat(keys):
    global boat_speed, boat_angle, spin_cooldown

    # Handle acceleration (w key)
    if keys[pygame.K_w]:
        boat_speed += 0.3  # Increase speed gradually

    # Handle turning (a and d keys)
    if keys[pygame.K_a]:
        boat_angle -= 3  # Turn left by some angle
    elif keys[pygame.K_d]:
        boat_angle += 3  # Turn right by some angle
    
    # Handle spinning (spacebar)
    if keys[pygame.K_SPACE] and spin_cooldown == 0:
        full_rotation_angle = 180  # Adjust for desired rotation amount
        # Update boat angle directly for a full rotation
        boat_angle = (boat_angle + full_rotation_angle) % 360 
        spin_cooldown = spin_cooldown_duration

    # Apply friction to slow down the boat gradually
    boat_speed *= 0.9  # Reduce speed by a factor (adjust for desired friction)
    

    # Update cooldown timer
    if spin_cooldown > 0:
        spin_cooldown -= 1  # Decrement cooldown timer

    # Calculate movement based on angle and speed
    x_movement = boat_speed * math.cos(math.radians(boat_angle))
    y_movement = boat_speed * math.sin(math.radians(boat_angle))

    # Update boat position based on movement
    boat_rect.x += x_movement
    boat_rect.y += y_movement
    

    # Wrap the boat around the screen edges
    boat_rect.x %= WIDTH
    boat_rect.y %= HEIGHT

def draw_screen(screen):
    screen.fill(SEA_BLUE)
    # Rotate the boat image based on angle and then blit it
    rotated_boat = pygame.transform.rotate(boat_image, -boat_angle)  # Negative for clockwise rotation
    screen.blit(rotated_boat, rotated_boat.get_rect(center=boat_rect.center))
    pygame.display.flip()

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Boat Game")
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        update_boat(keys)
        draw_screen(screen)

        clock.tick(60) / 1000  # Set FPS

    pygame.quit()

if __name__ == "__main__":
    main()
