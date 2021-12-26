# tarot_cards.py
# Randomly selects one tarot card from the 22 cards in the major deck.
# Author: Jackie P, aka TheDataElemental


import random
import pygame


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode((512, 480))
pygame.display.set_caption("TAROT CARD SELECTOR")
text_font = pygame.font.Font("NESfont.ttf", 14)
WHITE = (255, 255, 255)

# Generate list of card names
card_names = {
	0: 'The Fool',
	1: 'The Magician',
	2: 'The High Priestess',
	3: 'The Empress',
	4: 'The Emperor',
	5: 'The Hierophant',
	6: 'The Lovers',
	7: 'The Chariot',
	8: 'Strength',
	9: 'The Hermit',
	10: 'Wheel of Fortune',
	11: 'Justice',
	12: 'The Hanged Man',
	13: 'Death',
	14: 'Temperance',
	15: 'The Devil',
	16: 'The Tower',
	17: 'The Star',
	18: 'The Moon',
	19: 'The Sun',
	20: 'Judgement',
	21: 'The World',
	}

# Load card images
card_0_img = pygame.image.load("Assets/card_0.png")
card_1_img = pygame.image.load("Assets/card_1.png")
card_2_img = pygame.image.load("Assets/card_2.png")
card_3_img = pygame.image.load("Assets/card_3.png")
card_4_img = pygame.image.load("Assets/card_4.png")
card_5_img = pygame.image.load("Assets/card_5.png")
card_6_img = pygame.image.load("Assets/card_6.png")
card_7_img = pygame.image.load("Assets/card_7.png")
card_8_img = pygame.image.load("Assets/card_8.png")
card_9_img = pygame.image.load("Assets/card_9.png")
card_10_img = pygame.image.load("Assets/card_10.png")
card_11_img = pygame.image.load("Assets/card_11.png")
card_12_img = pygame.image.load("Assets/card_12.png")
card_13_img = pygame.image.load("Assets/card_13.png")
card_14_img = pygame.image.load("Assets/card_14.png")
card_15_img = pygame.image.load("Assets/card_15.png")
card_16_img = pygame.image.load("Assets/card_16.png")
card_17_img = pygame.image.load("Assets/card_17.png")
card_18_img = pygame.image.load("Assets/card_18.png")
card_19_img = pygame.image.load("Assets/card_19.png")
card_20_img = pygame.image.load("Assets/card_20.png")
card_21_img = pygame.image.load("Assets/card_21.png")

card_images = [
	card_0_img,
	card_1_img,
	card_2_img,
	card_3_img,
	card_4_img,
	card_5_img,
	card_6_img,
	card_7_img,
	card_8_img,
	card_9_img,
	card_10_img,
	card_11_img,
	card_12_img,
	card_13_img,
	card_14_img,
	card_15_img,
	card_16_img,
	card_17_img,
	card_18_img,
	card_19_img,
	card_20_img,
	card_21_img,
	]

# Select random card
card_choice = random.randint(0, (len(card_names) - 1))

# Show welcome message
welcome_text = "Welcome to PyGame Tarot."
welcome_message = text_font.render(welcome_text, True, WHITE)
screen.blit(welcome_message, (80, 40))

# Generate card message
card_text_1 = "Your Tarot Card for the day is:  " 
card_text_2 = str(card_choice) + ". " + card_names[card_choice]
card_message_1 = text_font.render(card_text_1, True, WHITE)
card_message_2 = text_font.render(card_text_2, True, WHITE)

# Center text displaying name of card (bc message is of variable length)
name_offset = (len(card_names[card_choice])) * 5

# Display message and card image
screen.blit(card_message_1, (35, 85))
screen.blit(card_message_2, ((200 - name_offset), 130))
screen.blit(card_images[card_choice], (200, 200))
pygame.display.flip()

# Wait 5 seconds, then close
pygame.time.delay(10000)
quit()
