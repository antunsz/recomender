
# Recomender 🚀

This repository houses the `recomender` Python package, a playful twist on "recommender". The essence of `recomender` is to enhance (mend) recommendation processes using Reinforcement Learning (RL) techniques.

## Architectural Concept

```mermaid
graph TD;
    A(Model Creation Module) -->|1. Define Model A with Keras, Torch, etc.| B(RLHF Processing Module)
    B -->|2. Apply RLHF| C(Reward Generator Module)
    C -->|3. Generate Rewards| B
    B -->|4. Interact with Gym Environment| D(Gym Environment)
    A --> E(Keras, Torch for Model Definition and Training)
    C -->|5. Use Clustering for Reward Calculation| F(Clustering Method)
    D -.->|6. Provide Simulated Feedback| B
    E -.->|7. Define & Train Model A| A
    F -.->|8. Calculate Distance-Based Rewards| C

    classDef library fill:#f9f,stroke:#333,stroke-width:4px;
    classDef external fill:#bbf,stroke:#333,stroke-width:4px;
    class A,B,C library;
    class E,F,D external;
```

## Package Architecture

```plaintext
/
├── examples/
│   ├── distance_based_reward.ipynb
│   └── sklearn_nn_model.ipynb
├── recomender/
│   ├── __init__.py
│   ├── builders/
│   │   ├── __init__.py
│   │   ├── DistanceBasedRewardBuilder.py
│   │   └── SklearnNNModelBuilder.py
│   └── interfaces/
│       ├── __init__.py
│       ├── RewardBuilderAbstract.py
│       └── SLModelBuilderAbstract.py
└── tests/
    └── builders/
        ├── __init__.py
        ├── test_reward_builder.py
        └── test_sklearn_nn_model_builder.py
```

## Installation

To get started with `recomender`, clone this repository and install the required packages using the following commands:

```bash
git clone https://github.com/antunsz/recomender.git
cd your-repository-directory
make install
```

## Features

- **Distance-Based Reward Building:** Utilizes machine learning techniques to calculate rewards based on the distance between entities, improving the efficiency of recommendation systems.
- **Modular Design:** Easy integration into existing ML workflows, allowing for quick experimentation and deployment.
- **Customizable Reward Strategies:** Implement your own reward strategies by extending the `RewardBuilderAbstract` class.

## Quick Start

1. **Set up your environment**
   
   Ensure you have Python 3.8+ installed. Clone the repository and set up a virtual environment:
   
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**
   
   Use the `Makefile` to install the necessary dependencies:
   
   ```bash
   make install
   ```

3. **Run the examples**
   
   Check out the `examples/` directory to see `recomender` in action. For a quick start, run the Jupyter notebook:
   
   ```bash
   jupyter notebook examples/distance_based_reward.ipynb
   ```

## Development

To contribute to the development of `recomender`, you can use the following commands:

- **Install for development:**
  
  ```bash
  make setup
  ```

- **Run tests:**
  
  ```bash
  make test
  ```

- **Linting:**
  
  ```bash
  make lint
  ```

For detailed guidelines on contributing, please refer to the `CONTRIBUTING.md` file.

## To Do

- [x] Define the Model Creation Module with support for multiple libraries (Keras, Torch, etc.)
- [x] Implement the RLHF Processing Module
- [x] Create the Reward Generator Module with a Distance-Based Reward Builder
- [ ] Implement interaction with Gym Environment for simulation feedback
- [x] Support for External Libraries and Tools in model architecture and training
- [ ] Enhance Reward Calculation with additional clustering methods
- [ ] Define and implement custom reward strategies

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Happy recommending! 🎉
