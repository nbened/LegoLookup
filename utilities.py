import pickle


def dump_pickle(path, objects):
    with open(path, 'wb') as f:
        pickle.dump(objects, f)

def load_pickle(path):
    with open(path, 'rb') as f:
        objects = pickle.load(f)
    return objects