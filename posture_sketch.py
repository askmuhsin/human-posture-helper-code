import matplotlib.pyplot as plt
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", default='./dataset/skeleton_pos.txt',
                    help="path to input dataset")
args = vars(ap.parse_args())

with open(args["dataset"]) as f:
    data = f.readlines()

while True:
    for row in data:
        posture = row

        posture_data = [x.strip() for x in posture.split(',')]

        joint_info = {}
        for i, n in enumerate(range(1, len(posture_data), 3)):
            joint_info[i+1] = [-float(posture_data[n]), -float(posture_data[n+1]), posture_data[n+2]]

        # print("Number of people in scene:\t", len(joint_info)/15, end='\n\n')

        person_1 = {k:joint_info[k] for k in range(1,16,1)}
        person_2 = {k-15:joint_info[k] for k in range(16,31,1)}
        # print(person_1)
        joint_details = {1 : 'HEAD',
        				2 : 'NECK',
        				3 : 'TORSO',
        				4 : 'LEFT_SHOULDER',
        				5 : 'LEFT_ELBOW',
        				6 : 'LEFT_HAND',
        				7 : 'RIGHT_SHOULDER',
        				8 : 'RIGHT_ELBOW',
        				9 : 'RIGHT_HAND',
        				10 : 'LEFT_HIP',
        				11 : 'LEFT_KNEE',
        				12 : 'LEFT_FOOT',
        				13 : 'RIGHT_HIP',
        				14 : 'RIGHT_KNEE',
        				15 : 'RIGHT_FOOT'}
        connect_map = [[1,2,2,2,3,3,3,3,4,5,7,8,10,11,13,14],[2,3,4,7,4,7,10,13,5,6,8,9,11,12,14,15]]

        for key, value in person_1.items():
            plt.plot(value[0], value[1], 'bo')
            # plt.annotate(joint_details[key], (value[0], value[1]))
        for m, n in zip(connect_map[0], connect_map[1]):
            plt.plot((person_1[m][0], person_1[n][0]), (person_1[m][1], person_1[n][1]), 'b--')

        for key, value in person_2.items():
            plt.plot(value[0], value[1], 'go')
            # plt.annotate(joint_details[key], (value[0], value[1]))
        for m, n in zip(connect_map[0], connect_map[1]):
            plt.plot((person_2[m][0], person_2[n][0]), (person_2[m][1], person_2[n][1]), 'g--')

        plt.title(row[:3])
        plt.xlim(-1, 0)
        plt.ylim(-1.2, 0)
        plt.pause(0.1)
        plt.clf()

    # plt.show()
