# Game Theory Meets Large Language Models

This repository provides a simulation-based exploration of the intersection between game theory and large language models (LLMs), inspired by the paper *Game Theory Meets Large Language Models: A Systematic Survey* (arXiv:2502.09053v1).

## Project Structure

```
Game-Theory-LLM/
├── README.md               # Project overview and instructions
├── requirements.txt        # Python dependencies
├── .gitignore              # Files/directories to ignore in git
├── LICENSE                 # License information (MIT)
├── evaluation/             # Benchmarking and evaluation scripts
│   ├── matrix_game.py      # Simulation of 2×2 matrix games
│   ├── communication_game.py  # Simulation of communication-based games
│   └── benchmark_runner.py     # Runner for game-based benchmarks
├── innovation/             # Code for algorithmic innovations
│   ├── recursive_reasoning.py  # Prototype for recursive thinking strategies
│   ├── auxiliary_module.py     # Integration of external computation modules
│   └── training_simulation.py  # Simulation of game-theoretic training objectives (e.g., NLHF)
└── modeling/               # Models for societal impact and strategic interaction
    ├── auction_simulation.py   # Auction mechanism simulation with incentive compatibility
    ├── competition_model.py    # Simulation of competitive dynamics between LLMs and humans
    └── social_impact_model.py  # Modeling the societal impact of LLM-enabled interactions
```

---

## Installation

```bash
git clone https://github.com/yourusername/Game-Theory-LLM.git
cd Game-Theory-LLM
pip install -r requirements.txt
```

---

## Usage

Run each module separately:
- **Matrix Game Simulation:**
  ```bash
  python evaluation/matrix_game.py
  ```
- **Communication Game Simulation:**
  ```bash
  python evaluation/communication_game.py
  ```
- **Benchmark Runner:**
  ```bash
  python evaluation/benchmark_runner.py
  ```
- **Recursive Reasoning:**
  ```bash
  python innovation/recursive_reasoning.py
  ```
- **Auxiliary Module Computation:**
  ```bash
  python innovation/auxiliary_module.py
  ```
- **Training Simulation:**
  ```bash
  python innovation/training_simulation.py
  ```
- **Auction Simulation:**
  ```bash
  python modeling/auction_simulation.py
  ```
- **Competition Model:**
  ```bash
  python modeling/competition_model.py
  ```
- **Social Impact Simulation:**
  ```bash
  python modeling/social_impact_model.py
  ```

---

## Contribution

Feel free to fork, modify, and submit pull requests. Open issues for bugs or feature requests.

---

## License

MIT License.

---

## Acknowledgement

Inspired by *Game Theory Meets Large Language Models: A Systematic Survey* (arXiv:2502.09053v1).

# Game-Theory-Meets-Large-Language-Models
