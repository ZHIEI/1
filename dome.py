import pygame

# 初始化 Pygame
pygame.init()

# 获取当前屏幕的分辨率信息
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

#导入词库信息
理科=[
    [    
    ],
    [  
    ],
    [
    ]
    ]
文科=[
    ['以头抢地尔','杨二嫂','孙悟空','掷铁饼者','闰土','桃园三结义','诸葛亮','托塔天王','秦王绕柱','负荆请罪','司马光','武松','屈原','老人与海'
    ],
    [
    ],
    [
    ]
    ]
自然=[
    [
    ],
    [
    ],
    [
    ]
    ]
日常=[
    [
    ],
    [
    ],
    [
    ]
    ]
原神=[
    [
    ],
    [
    ],
    [
    ]
    ]
二次元=[
    [
    ],
    [
    ],
    [
    ]
    ]
梗=[
    [
    ],
    [
    ],
    [
    ]
    ]
成分复杂=[
    [
    ],
    [
    ],
    [
    ]
    ]
高三三班=[
    [
    ],
    [
    ],
    [
    ]
    ]

# 创建一个全屏窗口
screen = pygame.display.set_mode((screen_width, screen_height))

# 设置字体
font = pygame.font.Font(None, 24)

# 设置词库名称
词库名称 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# 设置九宫格的大小和位置
grid_size = screen_width/81*screen_height/81
grid_padding = 10
grid_start_x = (screen_width - (grid_size * 3 + grid_padding * 2)) // 2
grid_start_y = screen_height - (grid_size * 3 + grid_padding * 2)

# 绘制九个小框并显示词库名称
for i in range(3):
    for j in range(3):
        index = i * 3 + j
        grid_rect = pygame.Rect(grid_start_x + (grid_size + grid_padding) * j, grid_start_y + (grid_size + grid_padding) * i, grid_size, grid_size)
        pygame.draw.rect(screen, (255, 255, 255), grid_rect, 2)
        text = font.render(词库名称[index], True, (255, 255, 255))
        text_rect = text.get_rect(center=grid_rect.center)
        screen.blit(text, text_rect)

# 刷新屏幕
pygame.display.flip()


# 游戏主循环
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # 获取鼠标点击位置
            mouse_pos = pygame.mouse.get_pos()
            # 判断是否点击在九宫格内
            if grid_start_x <= mouse_pos[0] <= grid_start_x + grid_size * 3 + grid_padding * 2 and grid_start_y <= mouse_pos[1] <= grid_start_y + grid_size * 3 + grid_padding * 2:
                # 计算点击的小框索引
                click_x = (mouse_pos[0] - grid_start_x) // (grid_size + grid_padding)
                click_y = (mouse_pos[1] - grid_start_y) // (grid_size + grid_padding)
                selected_index = click_y * 3 + click_x
                # 移动选中的小框至屏幕最上方
                grid_rect = pygame.Rect(grid_start_x + (grid_size + grid_padding) * click_x, grid_start_y + (grid_size + grid_padding) * click_y, grid_size, grid_size)
                grid_rect.move_ip(0, -grid_start_y)
                pygame.draw.rect(screen, (255, 255, 255), grid_rect, 2)
                text = font.render(词库名称[selected_index], True, (255, 255, 255))
                text_rect = text.get_rect(center=grid_rect.center)
                screen.blit(text, text_rect)
                # 刷新屏幕
                pygame.display.flip()