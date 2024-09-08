# Toll Collecting System 

This project is a simple **Toll Collecting System** simulation created using Python and Pygame. It simulates a toll gate where cars pass through, paying a toll when the barrier is lifted. The system includes a dynamic weather system (rain and snow), traffic lights, car movement, and barrier control. 

## Features
- **Car movement:** The user can control the car's movement using the arrow keys.
- **Barrier control:** The barrier opens and closes manually or automatically when cars pass through.
- **Toll collection:** The system collects toll when cars successfully pass through the open barrier.
- **Traffic lights:** Red and green lights indicate whether the barrier is open or closed.
- **Weather simulation:** Users can switch between rain and snow conditions.

## Controls

- **Arrow keys:** Control the car's movement.
- **`C` key:** Close the barrier.
- **`O` key:** Open the barrier.
- **`1` key:** Switch to rain weather.
- **`2` key:** Switch to snow weather.

## Prerequisites

Before running this project, ensure that you have Python and Pygame installed on your machine.

To install Pygame, use:
```bash
pip install pygame
```

## How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/toll-collecting-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd toll-collecting-system
   ```

3. Run the program:
   ```bash
   python toll_collecting_system.py
   ```
## Screenshot
![toll collecting](https://github.com/user-attachments/assets/0292effb-2aee-4f6d-8deb-6cbc866f0f56)

## Project Structure

- `toll_collecting_system.py`: Main file containing the game logic and simulation.
- `background.png`: The background image for the toll scene.
- `car.png`: Image representing the car in the game.
- `car_engine.wav`: Sound effect for the car's engine.
- Other images or sound files required for the simulation.

## Game Flow

1. The car can move around the toll booth using the arrow keys. 
2. The barrier opens with the `O` key and closes with the `C` key.
3. The car passes through the toll gate when the barrier is open, and the toll amount is incremented by $10 for each car.
4. The number of cars that have entered is also displayed.
5. You can toggle between rain and snow conditions using the `1` and `2` keys.

## Future Improvements

- Add additional car models and random car movement.
- Implement a more complex toll fee structure.
- Add more weather effects like thunderstorms.



