from Codes.adf20220426_134143 import SyncMapX

# ---------------don't revised belowed
from .GraphWalkTest import GraphWalkTest
import numpy as np
import os
import time
#import tqdm
from multiprocessing import Pool
import multiprocessing

# ----usable version


def normal_test():
    problem_path = "service/normal"
    problems = os.listdir(problem_path)
    length = 10000
    dict_score = {}
    for problem in problems:
        start = time.time()
        score = []
        for i in range(3):  # TODO
            print(problem, "   ", i)
            task = GraphWalkTest(10, problem_path+"/"+problem)
            model = SyncMapX(task.getOutputSize())
            for i in range(100):  # TODO
                seq = task.getSequence(length)
                model.input(seq[0])
            score.append(task.evaluation(model.organize()))
        mean = np.array(score).mean()
        std = np.array(score).std()
        time_used = time.time()-start
        dict_score['name'] = model.name
        dict_score[problem] = {"mean": mean, "std": std, "time": time_used}
    return dict_score


def normal_test_muti():
    problem_path = "service/normal"
    problems = os.listdir(problem_path)
    length = 10000
    dict_score = {}
    for problem in problems:
        start = time.time()
        score = []
        problem_path_whole = [problem_path+"/"+problem]
        score = mutiprocess(problem_path_whole, 30)  # TODO----

        mean = np.array(score).mean()
        std = np.array(score).std()
        time_used = time.time()-start
        model = SyncMapX(1)
        dict_score['name'] = model.name
        dict_score[problem] = {"mean": mean, "std": std, "time": time_used}
    return dict_score


def mutiprocess_work(problem_path):
    task = GraphWalkTest(10, problem_path)
    model = SyncMapX(task.getOutputSize())
    for i in range(1000):
        seq = task.getSequence(10000)
        model.input(seq[0])
    return task.evaluation(model.organize())


def mutiprocess(problem_path, repeat):
    work_list = problem_path*repeat
    with Pool(multiprocessing.cpu_count()) as p:
        r = list(p.imap(mutiprocess_work, work_list))
    return r
