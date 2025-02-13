# 100 Prisoners Problem Simulation

## Disclaimer
**All documentation and comments were AI-generated.** While efforts were made to ensure accuracy, please verify details as needed.


This project simulates the **100 Prisoners Problem**, a probability puzzle where prisoners must find their own number in randomly shuffled boxes under a set of constraints. The simulation includes two strategies:

1. **Loop Strategy**: Prisoners follow a sequence based on the numbers inside the boxes.
2. **Random Choice Strategy**: Prisoners randomly select boxes instead of following a deterministic path.

## Features
- Simulates the classic **100 Prisoners Problem**.
- Supports **early stopping** for efficiency.
- Includes a subclass implementing a **randomized strategy** for comparison.
- Provides a **loop-based approach**, which follows a more optimal searching sequence.

## Installation & Usage
Ensure you have Python installed, then simply run:

```sh
python simulation.py
```

The script will execute the simulation and print the number of failed attempts before achieving a successful outcome.

## Project Structure
- `simulation.py` - Main script containing the logic and execution.
- `PrisonerSimulation` - Base class implementing the loop-following strategy.
- `RandomChoiceSimulation` - Subclass implementing a randomized approach.

## Example Output
```
Fail count: 0, Rate: ignored in early stop, Success: False
Fail count: 1, Rate: ignored in early stop, Success: False
...
Fail count: 45, Rate: ignored in early stop, Success: True
```

## License
This project is licensed under the MIT License.

