from Codes.sigma20220425_140624 import SyncMapX

# ---------------don't revised belowed
from .GraphWalkTest import GraphWalkTest
import numpy as np
import os
import time


def normal_test():
    problem_path = "service/normal"
    problems = os.listdir(problem_path)
    length = 100000
    dict_score = {}
    for problem in problems:
        start = time.time()
        score = []
        for i in range(10):  # TODO
            print(problem, "   ", i)
            task = GraphWalkTest(10, problem_path+"/"+problem)
            model = SyncMapX(task.getOutputSize())
            for i in range(10):  # TODO
                seq = task.getSequence(length)
                model.input(seq[0])
            score.append(task.evaluation(model.organize()))
        mean = np.array(score).mean()
        std = np.array(score).std()
        time_used = time.time()-start
        dict_score['name'] = model.name
        dict_score[problem] = {"mean": mean, "std": std, "time": time_used}
    return dict_score
