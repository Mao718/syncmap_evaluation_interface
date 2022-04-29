from Codes.dsa20220429_115407 import SyncMapX

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
    model = SyncMapX(1)
    dict_score['name'] = model.name
    for problem in problems:
        start = time.time()
        score = []
        problem_path_whole = [problem_path+"/"+problem]
        score = mutiprocess(problem_path_whole, 10)  # TODO----
        mean = np.array(score).mean()
        std = np.array(score).std()
        time_used = time.time()-start

        dict_score[problem] = {"mean": mean, "std": std, "time": time_used}

    problem_path = "service/dynamic"
    problems = os.listdir(problem_path)
    for problem in problems:
        start = time.time()
        score = []
        problem_now = problem_path+"/"+problem
        score = mutiprocess_dynamic(problem_now, 10)  # TODO----

        mean = np.array(score).mean()
        std = np.array(score).std()
        time_used = time.time()-start
        model = SyncMapX(1)
        dict_score[problem] = {"mean": mean, "std": std, "time": time_used}

    return dict_score


def mutiprocess_work_dynamic(problem_now):
    dynamics = os.listdir(problem_now)
    for dynamic in dynamics:
        task = GraphWalkTest(10, problem_now+"/"+dynamic)
        model = SyncMapX(task.getOutputSize())
        for i in range(1000):  #
            seq = task.getSequence(10000)
            model.input(seq[0])
    return task.evaluation(model.organize())


def mutiprocess_dynamic(problem_path, repeat):
    work_list = [problem_path]*repeat
    with Pool(multiprocessing.cpu_count()) as p:
        r = list(p.imap(mutiprocess_work_dynamic, work_list))
    return r


def mutiprocess_work_normal(problem_path):
    task = GraphWalkTest(10, problem_path)
    model = SyncMapX(task.getOutputSize())
    for i in range(1000):
        seq = task.getSequence(10000)
        model.input(seq[0])
    return task.evaluation(model.organize())


def mutiprocess(problem_path, repeat):
    work_list = problem_path*repeat
    with Pool(multiprocessing.cpu_count()) as p:
        r = list(p.imap(mutiprocess_work_normal, work_list))
    return r
