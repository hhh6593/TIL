

import numpy as np



arm_success = None  #Holds the paramter \alpha for each arm

arm_failures = None  #Holds the paramter \beta for each arm 

arm = None

total_returns = 0



def agent(observation, configuration):

    global arm_success, arm_failures, arm, total_returns

    

    n_bandits = configuration.banditCount

    

    if observation.step == 0:

        arm_success = np.ones(n_bandits)

        arm_failures = np.ones(n_bandits)

    else:

        reward = observation.reward - total_returns

        arm_success[arm] += reward

        arm_failures[arm] += (1 - reward)

        total_returns = observation.reward

        

    arm_samples = np.random.beta(arm_success, arm_failures)

        

    arm = int(np.argmax(arm_samples))

    

    return (arm)
