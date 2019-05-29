# Basic_Q-Learning
Basic Python implementation of Tabular Q-Learning working with OpenAI-Gym

### Requirements
* Python 3
* [OpenAI-Gym](https://github.com/openai/gym)
* NumPy

### Usage
To choose different Environment simply change the following line to the name of the environment you'd like to test.
```
env = gym.make("Taxi-v2")
```
To change the parameters for learning rate, discount factor and episodes, respectively, change these lines: 
```
lr = 0.618
gamma = 1.0
MAX_EPISODES = 1001
```
For learning purposes I encourage you to test different parameters and compare performances.

### Useful Links

[Medium Tutorial, Arthur Juliani](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0)

[Q-Learning by hand example](http://mnemstudio.org/path-finding-q-learning-tutorial.htm)
