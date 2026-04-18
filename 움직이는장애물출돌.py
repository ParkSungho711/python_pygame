import pygame

# 1. 초기화 및 설정
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("미로 탈출: 장애물을 피하라!")
clock = pygame.time.Clock()

# 색상 정의
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# 2. 플레이어 설정
player_size = 40
player_x = 50
player_y = screen_height // 2
player_speed = 5

# 3. 장애물 설정 (자동으로 위아래로 움직임)
enemy_width = 50
enemy_height = 50
enemy_x = 400
enemy_y = 100
enemy_speed_y = 4  # 장애물의 이동 속도

# 4. 목표 지점 (나무 역할)
goal_rect = pygame.Rect(720, screen_height // 2 - 25, 50, 50)

running = True
while running:
    clock.tick(60) # 60 FPS

    # 5. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 6. 플레이어 이동 (키보드 입력)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < screen_height - player_size:
        player_y += player_speed

    # 7. 장애물 이동 로직 (벽에 닿으면 튕기기)
    enemy_y += enemy_speed_y
    if enemy_y <= 0 or enemy_y >= screen_height - enemy_height:
        enemy_speed_y *= -1  # 방향 반전

    # 8. 충돌 감지 (Collision Detection)
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, enemy_width, enemy_height)

    # 장애물과 충돌했는가?
    if player_rect.colliderect(enemy_rect):
        print("장애물 충돌! 시작점으로 돌아갑니다.")
        player_x, player_y = 50, screen_height // 2

    # 목표 지점에 도달했는가?
    if player_rect.colliderect(goal_rect):
        print("미션 성공!")
        running = False

    # 9. 화면 그리기
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, BLUE, player_rect)  # 플레이어 (파랑)
    pygame.draw.rect(screen, RED, enemy_rect)   # 장애물 (빨강)
    pygame.draw.rect(screen, GREEN, goal_rect)  # 목표 지점 (초록)

    pygame.display.update()

pygame.quit()
