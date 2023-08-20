""" 1 """
""" import multiprocessing

def square_sum(numbers):
    return sum(num ** 2 for num in numbers)

def worker_process(numbers, results):
    result = square_sum(numbers)
    results.put(result)

def main():
    # List of numbers to process
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Number of worker processes
    num_workers = multiprocessing.cpu_count()

    # Create a shared queue for results
    results = multiprocessing.Queue()

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_workers)

    # Handle the case where there are more worker processes than numbers
    if num_workers > len(numbers):
        num_workers = len(numbers)

    # Split the list of numbers into chunks for each worker
    chunk_size = len(numbers) // num_workers
    chunks = [numbers[i:i+chunk_size] for i in range(0, len(numbers), chunk_size)]

    # If there are remaining numbers, add them to the last chunk
    if len(numbers) % num_workers != 0:
        chunks[-1] += numbers[chunk_size * num_workers:]

    # Distribute the chunks to worker processes
    for chunk in chunks:
        pool.apply_async(worker_process, args=(chunk, results))

    # Close the pool and wait for the worker processes to finish
    pool.close()
    pool.join()

    # Collect the results from the worker processes
    total_sum = 0
    while not results.empty():
        result = results.get()
        total_sum += result

    print("Total sum of squares:", total_sum)

if __name__ == '__main__':
    main()
"""

""" 2 """
""" import multiprocessing
import re
from collections import Counter

def count_words(chunk):
    word_counts = Counter(chunk)
    return word_counts

def worker_process(chunk, results):
    result = count_words(chunk)
    results.put(result)

def main():
    # Open the large file for reading
    with open('C:\\Users\\pasha\\OneDrive\\Рабочий стол\\Текстовый документ.txt', 'r') as file:
        # Read the contents of the file
        file_contents = file.read()

    # Split the file contents into words
    words = re.findall(r'\w+', file_contents.lower())

    # Number of worker processes
    num_workers = multiprocessing.cpu_count()

    # Create a shared queue for results
    results = multiprocessing.Queue()

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_workers)

    # Split the words into chunks for each worker
    chunk_size = len(words) // num_workers
    chunks = [words[i:i+chunk_size] for i in range(0, len(words), chunk_size)]

    # If there are remaining words, add them to the last chunk
    if len(words) % num_workers != 0:
        chunks[-1] += words[chunk_size * num_workers:]

    # Distribute the chunks to worker processes
    for chunk in chunks:
        pool.apply_async(worker_process, args=(chunk, results))

    # Close the pool and wait for the worker processes to finish
    pool.close()
    pool.join()

    # Collect the results from the worker processes
    final_word_counts = Counter()
    while not results.empty():
        result = results.get()
        final_word_counts += result

    # Print the frequency count of words
    for word, count in final_word_counts.most_common():
        print(f"{word}: {count}")
        # Write the frequency count to the output file
    with open('output.txt', 'w') as output_file:
        for word, count in final_word_counts.most_common():
            output_file.write(f"{word}: {count}\n")

if __name__ == '__main__':
    main()
"""

""" 3 """
""" import multiprocessing
import random

# List of all possible winning combinations
WINNING_COMBINATIONS = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

# Possible players
PLAYER_X = 'X'
PLAYER_O = 'O'

def is_board_full(board):
    
    for row in board:
        if ' ' in row:
            return False
    return True

def check_winner(board):
    
    for combination in WINNING_COMBINATIONS:
        symbol = board[combination[0][0]][combination[0][1]]
        if symbol != ' ' and all(board[row][col] == symbol for row, col in combination):
            return symbol
    return None

def random_move(board):
    
    empty_positions = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                empty_positions.append((i, j))
    return random.choice(empty_positions)

def play_game():
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = PLAYER_X

    while not is_board_full(board):
        move = random_move(board)
        row, col = move
        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            return winner

        current_player = PLAYER_O if current_player == PLAYER_X else PLAYER_X

    return 'DRAW'

def worker_process(results):
    
    result = play_game()
    results.put(result)

def main():
    # Number of games to simulate
    num_games = 100

    # Number of worker processes
    num_workers = multiprocessing.cpu_count()

    # Create a shared queue for results
    results = multiprocessing.Queue()

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_workers)

    # Simulate multiple games using worker processes
    for _ in range(num_games):
        pool.apply_async(worker_process, args=(results,))

    # Close the pool and wait for the worker processes to finish
    pool.close()
    pool.join()

    # Collect the results from the worker processes
    game_results = []
    while not results.empty():
        result = results.get()
        game_results.append(result)

    # Count the number of wins for each player
    wins_x = game_results.count(PLAYER_X)
    wins_o = game_results.count(PLAYER_O)
    draws = game_results.count('DRAW')

    # Print the overall statistics
    print("Total games simulated:", num_games)
    print("Player X wins:", wins_x)
    print("Player O wins:", wins_o)
    print("Draws:", draws)

if __name__ == '__main__':
    main()
"""

""" 4 """
""" import multiprocessing
from PIL import Image

# List of image file paths to process
image_files = ['C:\\Users\\pasha\\Downloads\\premium_photo-1677362425101-a11ef7eaae03.avif', 'C:\\Users\\pasha\\Downloads\\photo-1685194926944-9750afc26e39.avif', 'C:\\Users\\pasha\\Downloads\\photo-1682685796063-d2604827f7b3.avif']

def process_image(image_file):
    # Open the image file
    image = Image.open(image_file)

    # Perform image processing tasks
    # Example: Convert the image to grayscale
    processed_image = image.convert('L')

    # Close the image file
    image.close()

    return processed_image

def worker_process(image_file, results):
    
    result = process_image(image_file)
    results.put((image_file, result))

def main():
    # Number of worker processes
    num_workers = multiprocessing.cpu_count()

    # Create a shared queue for results
    results = multiprocessing.Queue()

    # Create a pool of worker processes
    pool = multiprocessing.Pool(processes=num_workers)

    # Process images using worker processes
    for image_file in image_files:
        pool.apply_async(worker_process, args=(image_file, results))

    # Close the pool and wait for the worker processes to finish
    pool.close()
    pool.join()

    # Collect the results from the worker processes
    processed_images = {}
    while not results.empty():
        image_file, result = results.get()
        processed_images[image_file] = result

    # Combine the processed images into a final output image
    # Example: Combine the grayscale images into a single composite image
    composite_image = Image.new('L', (300, 300))
    for image_file, processed_image in processed_images.items():
        composite_image.paste(processed_image, (0, 0))

    # Save or display the final output image
    composite_image.show()

if __name__ == '__main__':
    main()
"""