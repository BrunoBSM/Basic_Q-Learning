import gym
import numpy as np

env = gym.make("Taxi-v2") # Initiating environment

Q = np.zeros([env.observation_space.n, env.action_space.n]) # creating Q-Table
lr = 0.6              # learning rate
gamma = 1.0           # discount factor
MAX_EPISODES = 1001   # maximum episodes

for episode in range(1,MAX_EPISODES):
    done = False 
    acc_reward = 0 #accumulated reward along the episode
    reward = 0
    state = env.reset()
    while done != True: # until episode finished
        action = np.argmax(Q[state])
        state2, reward, done, info = env.step(action) # step environment
        Q[state,action] += lr * (reward + gamma*np.max(Q[state2] - Q[state,action])) # Adaptation of Bellman Equation
        acc_reward += reward
        state = state2
    if episode % 50 == 0: # print every 50 episodes
        env.render()
        print('Episode {} Total Reward {}'.format(episode,acc_reward))
