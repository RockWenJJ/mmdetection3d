import pickle
import pprint

def compute_stats(data):
    result_dict = {}
    for d in data:
        for anno in d['annos']['name']:
            if anno in result_dict.keys():
                result_dict[anno] += 1
            else:
                result_dict.setdefault(anno, 1)
    pprint.pprint(result_dict)
    return result_dict

if __name__ == '__main__':
    # train_data = pickle.load(open('./data/kitti/kitti_infos_train.pkl', 'rb'))
    # train_mini = train_data[:121]
    # compute_stats(train_mini)
    # pickle.dump(train_mini, open('./data/kitti/kitti_infos_train_mini.pkl', 'wb'))

    train_mini = pickle.load(open('./data/kitti/kitti_infos_train_mini.pkl', 'rb'))
    # train_mini = train_data[:121]
    compute_stats(train_mini)