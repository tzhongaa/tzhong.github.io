# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt
import librosa
import librosa.display
import matplotlib.pyplot as plt

# name = "simulated/0-15/clean/00011"


def print_figure(name):
    y, sr = librosa.load(f"{name}.wav", sr=16000, mono=False)
    # fig, ax = plt.subplots(nrows=2, ncols=1, sharex=True)
    fig, ax = plt.subplots()
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y, n_fft=512, hop_length=256)), ref=np.max)
    img = librosa.display.specshow(D, y_axis='linear', x_axis='s', hop_length=256, sr=sr, ax=ax)
    # ax.set(title='Linear-frequency power spectrogram')
    # ax.label_outer()
    plt.savefig(f"{name}.png")
    # plt.show()

# clean
# name1 = "test/official_clean/00018"
# print_figure(name1)
# name2 = "test/official_clean/00019"
# print_figure(name2)
# name3 = "test/official_clean/00027"
# print_figure(name3)
# name4 = "test/official_clean/00029"
# print_figure(name4)


# mixture
# name1 = "simulated/0-15/0-mc/mixture/00019"
# print_figure(name1)
# name2 = "simulated/15-45/0-mc/mixture/00027"
# print_figure(name2)
# name3 = "simulated/45-90/0-mc/mixture/00029"
# print_figure(name3)
# name4 = "simulated/90-180/0-mc/mixture/00018"
# print_figure(name4)

# # rvb only
# name1 = "simulated/0-15/0-mc/rvb-only/00019"
# print_figure(name1)
# name2 = "simulated/15-45/0-mc/rvb-only/00027"
# print_figure(name2)
# name3 = "simulated/45-90/0-mc/rvb-only/00029"
# print_figure(name3)
# name4 = "simulated/90-180/0-mc/rvb-only/00018"
# print_figure(name4)

# clean
# name1 = "simulated/0-15/0-mc/clean/00019"
# print_figure(name1)
# name2 = "simulated/15-45/0-mc/clean/00027"
# print_figure(name2)
# name3 = "simulated/45-90/0-mc/clean/00029"
# print_figure(name3)
# name4 = "simulated/90-180/0-mc/clean/00018"
# print_figure(name4)


# # [1] ao-mvdr-only pipelined
# name1 = "simulated/0-15/1-ao-mvdr-only/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/1-ao-mvdr-only/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/1-ao-mvdr-only/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/1-ao-mvdr-only/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [1] ao-mvdr-only joint2
# name1 = "simulated/0-15/1-ao-mvdr-only/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/1-ao-mvdr-only/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/1-ao-mvdr-only/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/1-ao-mvdr-only/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)

# # [2] av-mvdr-only pipelined
# name1 = "simulated/0-15/2-av-mvdr-only/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/2-av-mvdr-only/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/2-av-mvdr-only/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/2-av-mvdr-only/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [1] av-mvdr-only joint2
# name1 = "simulated/0-15/2-av-mvdr-only/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/2-av-mvdr-only/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/2-av-mvdr-only/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/2-av-mvdr-only/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)



# # [3] ao-mvdr-dwpe pipelined
# name1 = "simulated/0-15/3-ao-mvdr-dwpe/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/3-ao-mvdr-dwpe/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/3-ao-mvdr-dwpe/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/3-ao-mvdr-dwpe/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [3] ao-mvdr-dwpe joint2
# name1 = "simulated/0-15/3-ao-mvdr-dwpe/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/3-ao-mvdr-dwpe/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/3-ao-mvdr-dwpe/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/3-ao-mvdr-dwpe/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)


# # [4] av-mvdr-dwpe pipelined
# name1 = "simulated/0-15/4-av-mvdr-dwpe/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/4-av-mvdr-dwpe/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/4-av-mvdr-dwpe/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/4-av-mvdr-dwpe/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [4] av-mvdr-dwpe joint2
# name1 = "simulated/0-15/4-av-mvdr-dwpe/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/4-av-mvdr-dwpe/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/4-av-mvdr-dwpe/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/4-av-mvdr-dwpe/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)


# # [5] ao-mvdr-specm pipelined
# name1 = "simulated/0-15/5-ao-mvdr-specm/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/5-ao-mvdr-specm/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/5-ao-mvdr-specm/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/5-ao-mvdr-specm/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [5] ao-mvdr-specm joint2
# name1 = "simulated/0-15/5-ao-mvdr-specm/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/5-ao-mvdr-specm/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/5-ao-mvdr-specm/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/5-ao-mvdr-specm/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)
#
#
# # [6] av-mvdr-specm pipelined
# name1 = "simulated/0-15/6-av-mvdr-specm/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/6-av-mvdr-specm/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/6-av-mvdr-specm/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/6-av-mvdr-specm/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [6] av-mvdr-specm joint2
# name1 = "simulated/0-15/6-av-mvdr-specm/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/6-av-mvdr-specm/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/6-av-mvdr-specm/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/6-av-mvdr-specm/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)


# # [7] ao-dwpe-mvdr pipelined
# name1 = "simulated/0-15/7-ao-dwpe-mvdr/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/7-ao-dwpe-mvdr/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/7-ao-dwpe-mvdr/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/7-ao-dwpe-mvdr/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [7] ao-dwpe-mvdr joint2
# name1 = "simulated/0-15/7-ao-dwpe-mvdr/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/7-ao-dwpe-mvdr/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/7-ao-dwpe-mvdr/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/7-ao-dwpe-mvdr/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)
#
#
# # [8] av-dwpe-mvdr pipelined
# name1 = "simulated/0-15/8-av-dwpe-mvdr/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/8-av-dwpe-mvdr/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/8-av-dwpe-mvdr/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/8-av-dwpe-mvdr/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [8] av-dwpe-mvdr joint2
# name1 = "simulated/0-15/8-av-dwpe-mvdr/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/8-av-dwpe-mvdr/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/8-av-dwpe-mvdr/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/8-av-dwpe-mvdr/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)


# # [9] ao-specm-mvdr pipelined
# name1 = "simulated/0-15/9-ao-specm-mvdr/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/9-ao-specm-mvdr/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/9-ao-specm-mvdr/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/9-ao-specm-mvdr/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [9] ao-specm-mvdrjoint2
# name1 = "simulated/0-15/9-ao-specm-mvdr/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/9-ao-specm-mvdr/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/9-ao-specm-mvdr/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/9-ao-specm-mvdr/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)
#
#
# # [10] av-specm-mvdr pipelined
# name1 = "simulated/0-15/10-av-specm-mvdr/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/10-av-specm-mvdr/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/10-av-specm-mvdr/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/10-av-specm-mvdr/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [10] av-specm-mvdr joint2
# name1 = "simulated/0-15/10-av-specm-mvdr/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/10-av-specm-mvdr/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/10-av-specm-mvdr/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/10-av-specm-mvdr/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)


# # [11] ao-wpd pipelined
# name1 = "simulated/0-15/11-ao-wpd/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/11-ao-wpd/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/11-ao-wpd/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/11-ao-wpd/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [11] ao-wpd joint2
# name1 = "simulated/0-15/11-ao-wpd/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/11-ao-wpd/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/11-ao-wpd/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/11-ao-wpd/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)
#
#
# # [12] av-wpd pipelined
# name1 = "simulated/0-15/12-av-wpd/pipelined/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/12-av-wpd/pipelined/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/12-av-wpd/pipelined/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/12-av-wpd/pipelined/rev4-6332062124509813446-00018"
# print_figure(name4)
# # [12] av-wpd joint2
# name1 = "simulated/0-15/12-av-wpd/joint2/rev1-6331559613336179781-00019"
# print_figure(name1)
# name2 = "simulated/15-45/12-av-wpd/joint2/rev2-6331559613336179781-00027"
# print_figure(name2)
# name3 = "simulated/45-90/12-av-wpd/joint2/rev3-6331559613336179781-00029"
# print_figure(name3)
# name4 = "simulated/90-180/12-av-wpd/joint2/rev4-6332062124509813446-00018"
# print_figure(name4)

# #################################### Replayed ################################
# # mixture
# name1 = "replayed/0-15/0-mc/mixture/6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/0-mc/mixture/6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/0-mc/mixture/6392525815109495392-00008"
# print_figure(name3)
#
# # clean
# name1 = "replayed/0-15/0-mc/clean/00019"
# print_figure(name1)
# name2 = "replayed/15-45/0-mc/clean/00036"
# print_figure(name2)
# name3 = "replayed/45-90/0-mc/clean/00008"
# print_figure(name3)


# # [1] ao-mvdr-only pipelined
# name1 = "replayed/0-15/1-ao-mvdr-only/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/1-ao-mvdr-only/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/1-ao-mvdr-only/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [1] ao-mvdr-only joint2
# name1 = "replayed/0-15/1-ao-mvdr-only/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/1-ao-mvdr-only/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/1-ao-mvdr-only/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)
#
#
# # [2] av-mvdr-only pipelined
# name1 = "replayed/0-15/2-av-mvdr-only/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/2-av-mvdr-only/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/2-av-mvdr-only/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [2] av-mvdr-only joint2
# name1 = "replayed/0-15/2-av-mvdr-only/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/2-av-mvdr-only/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/2-av-mvdr-only/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)



# # [3] ao-mvdr-dwpe pipelined
# name1 = "replayed/0-15/3-ao-mvdr-dwpe/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/3-ao-mvdr-dwpe/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/3-ao-mvdr-dwpe/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [3] ao-mvdr-dwpe joint2
# name1 = "replayed/0-15/3-ao-mvdr-dwpe/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/3-ao-mvdr-dwpe/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/3-ao-mvdr-dwpe/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)
#
#
# # [4] av-mvdr-dwpe pipelined
# name1 = "replayed/0-15/4-av-mvdr-dwpe/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/4-av-mvdr-dwpe/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/4-av-mvdr-dwpe/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [4] av-mvdr-dwpe joint2
# name1 = "replayed/0-15/4-av-mvdr-dwpe/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/4-av-mvdr-dwpe/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/4-av-mvdr-dwpe/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)


# # [5] ao-mvdr-specm pipelined
# name1 = "replayed/0-15/5-ao-mvdr-specm/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/5-ao-mvdr-specm/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/5-ao-mvdr-specm/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [5] ao-mvdr-specm joint2
# name1 = "replayed/0-15/5-ao-mvdr-specm/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/5-ao-mvdr-specm/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/5-ao-mvdr-specm/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)
#
#
# # [6] av-mvdr-specm pipelined
# name1 = "replayed/0-15/6-av-mvdr-specm/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/6-av-mvdr-specm/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/6-av-mvdr-specm/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [6] av-mvdr-specm joint2
# name1 = "replayed/0-15/6-av-mvdr-specm/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/6-av-mvdr-specm/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/6-av-mvdr-specm/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)


# # [7] ao-dwpe-mvdr pipelined
# name1 = "replayed/0-15/7-ao-dwpe-mvdr/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/7-ao-dwpe-mvdr/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/7-ao-dwpe-mvdr/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [7] ao-dwpe-mvdr joint2
# name1 = "replayed/0-15/7-ao-dwpe-mvdr/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/7-ao-dwpe-mvdr/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/7-ao-dwpe-mvdr/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)
#
#
#
# # [8] av-dwpe-mvdr pipelined
# name1 = "replayed/0-15/8-av-dwpe-mvdr/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/8-av-dwpe-mvdr/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/8-av-dwpe-mvdr/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [8] av-dwpe-mvdr joint2
# name1 = "replayed/0-15/8-av-dwpe-mvdr/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/8-av-dwpe-mvdr/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/8-av-dwpe-mvdr/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)


# # [9] ao-specm-mvdr pipelined
# name1 = "replayed/0-15/9-ao-specm-mvdr/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/9-ao-specm-mvdr/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/9-ao-specm-mvdr/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [9] ao-specm-mvdrjoint2
# name1 = "replayed/0-15/9-ao-specm-mvdr/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/9-ao-specm-mvdr/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/9-ao-specm-mvdr/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)
#
#
# # [10] av-specm-mvdr pipelined
# name1 = "replayed/0-15/10-av-specm-mvdr/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/10-av-specm-mvdr/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/10-av-specm-mvdr/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [10] av-specm-mvdr joint2
# name1 = "replayed/0-15/10-av-specm-mvdr/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/10-av-specm-mvdr/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/10-av-specm-mvdr/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)


# # [11] ao-wpd pipelined
# name1 = "replayed/0-15/11-ao-wpd/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/11-ao-wpd/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/11-ao-wpd/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [11] ao-wpd joint2
# name1 = "replayed/0-15/11-ao-wpd/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/11-ao-wpd/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/11-ao-wpd/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)
#
#
# # [12] av-wpd pipelined
# name1 = "replayed/0-15/12-av-wpd/pipelined/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/12-av-wpd/pipelined/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/12-av-wpd/pipelined/rev1-6392525815109495392-00008"
# print_figure(name3)
# # [12] av-wpd joint2
# name1 = "replayed/0-15/12-av-wpd/joint2/rev1-6352498867394358158-00019"
# print_figure(name1)
# name2 = "replayed/15-45/12-av-wpd/joint2/rev1-6352893145392128503-00036"
# print_figure(name2)
# name3 = "replayed/45-90/12-av-wpd/joint2/rev1-6392525815109495392-00008"
# print_figure(name3)


# baseline 

# name = "test_audio/baseline/rev1-6331559613336179781-00019"
# print_figure(name)
# name = "test_audio/baseline/rev2-6331559613336179781-00027"
# print_figure(name)
# name = "test_audio/baseline/rev3-6331559613336179781-00029"
# print_figure(name)
# name = "test_audio/baseline/rev4-6332062124509813446-00018"
# print_figure(name)

# # low_rank 
# name = "test_audio/low_rank/rev1-6331559613336179781-00019"
# print_figure(name)
# name = "test_audio/low_rank/rev2-6331559613336179781-00027"
# print_figure(name)
# name = "test_audio/low_rank/rev3-6331559613336179781-00029"
# print_figure(name)
# name = "test_audio/low_rank/rev4-6332062124509813446-00018"
# print_figure(name)

# # low_rank + nas
# name = "test_audio/low_rank+nas/rev1-6331559613336179781-00019"
# print_figure(name)
# name = "test_audio/low_rank+nas/rev2-6331559613336179781-00027"
# print_figure(name)
# name = "test_audio/low_rank+nas/rev3-6331559613336179781-00029"
# print_figure(name)
# name = "test_audio/low_rank+nas/rev4-6332062124509813446-00018"
# print_figure(name)

# # low_rank + parameter_sharing 
# name = "test_audio/low_rank+parameter_sharing/rev1-6331559613336179781-00019"
# print_figure(name)
# name = "test_audio/low_rank+parameter_sharing/rev2-6331559613336179781-00027"
# print_figure(name)
# name = "test_audio/low_rank+parameter_sharing/rev3-6331559613336179781-00029"
# print_figure(name)
# name = "test_audio/low_rank+parameter_sharing/rev4-6332062124509813446-00018"
# print_figure(name)

# # low_rank + parameter_sharing+kl_based_quantization
# name = "test_audio/low_rank+parameter_sharing+kl_based_quantization/rev1-6331559613336179781-00019"
# print_figure(name)
# name = "test_audio/low_rank+parameter_sharing+kl_based_quantization/rev2-6331559613336179781-00027"
# print_figure(name)
# name = "test_audio/low_rank+parameter_sharing+kl_based_quantization/rev3-6331559613336179781-00029"
# print_figure(name)
# name = "test_audio/low_rank+parameter_sharing+kl_based_quantization/rev4-6332062124509813446-00018"
# print_figure(name)


# baseline 

name = "test_audio_ciavsr/baseline/final_select/C010-ICAVSP-00009-HKUSTXXX-XXXFXX-ih_10000040-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/baseline/final_select/C010-ICAVSP-00015-HKUSTXXX-XXXMXX-ih_20000090-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/baseline/final_select/C010-ICAVSP-00023-HKUSTXXX-XXXFXX-ih_20000098-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/baseline/final_select/C011-ICAVSP-00007-HKUSTXXX-XXXMXX-ih_20000007-2spk_S1_S4-BackgroundMusic_Rain_Hail_Ignition-DifferentGender"
print_figure(name)

# low_rank 

name = "test_audio_ciavsr/low_rank/final_select/C010-ICAVSP-00009-HKUSTXXX-XXXFXX-ih_10000040-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank/final_select/C010-ICAVSP-00015-HKUSTXXX-XXXMXX-ih_20000090-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank/final_select/C010-ICAVSP-00023-HKUSTXXX-XXXFXX-ih_20000098-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank/final_select/C011-ICAVSP-00007-HKUSTXXX-XXXMXX-ih_20000007-2spk_S1_S4-BackgroundMusic_Rain_Hail_Ignition-DifferentGender"
print_figure(name)

# low_rank+nas

name = "test_audio_ciavsr/low_rank+nas/final_select/C010-ICAVSP-00009-HKUSTXXX-XXXFXX-ih_10000040-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank+nas/final_select/C010-ICAVSP-00015-HKUSTXXX-XXXMXX-ih_20000090-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank+nas/final_select/C010-ICAVSP-00023-HKUSTXXX-XXXFXX-ih_20000098-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank+nas/final_select/C011-ICAVSP-00007-HKUSTXXX-XXXMXX-ih_20000007-2spk_S1_S4-BackgroundMusic_Rain_Hail_Ignition-DifferentGender"
print_figure(name)

# low_rank+sharing

name = "test_audio_ciavsr/low_rank+parameter_sharing/final_select/C010-ICAVSP-00009-HKUSTXXX-XXXFXX-ih_10000040-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank+parameter_sharing/final_select/C010-ICAVSP-00015-HKUSTXXX-XXXMXX-ih_20000090-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank+parameter_sharing/final_select/C010-ICAVSP-00023-HKUSTXXX-XXXFXX-ih_20000098-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank+parameter_sharing/final_select/C011-ICAVSP-00007-HKUSTXXX-XXXMXX-ih_20000007-2spk_S1_S4-BackgroundMusic_Rain_Hail_Ignition-DifferentGender"
print_figure(name)

# low_rank+sharing+kl

name = "test_audio_ciavsr/low_rank+parameter_sharing_kl_based_quantization/final_selected/C010-ICAVSP-00009-HKUSTXXX-XXXFXX-ih_10000040-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank+parameter_sharing_kl_based_quantization/final_selected/C010-ICAVSP-00015-HKUSTXXX-XXXMXX-ih_20000090-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank+parameter_sharing_kl_based_quantization/final_selected/C010-ICAVSP-00023-HKUSTXXX-XXXFXX-ih_20000098-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/low_rank+parameter_sharing_kl_based_quantization/final_selected/C011-ICAVSP-00007-HKUSTXXX-XXXMXX-ih_20000007-2spk_S1_S4-BackgroundMusic_Rain_Hail_Ignition-DifferentGender"
print_figure(name)



# mix

name = "test_audio_ciavsr/mix/0/C010-ICAVSP-00009-HKUSTXXX-XXXFXX-ih_10000040-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/mix/0/C010-ICAVSP-00015-HKUSTXXX-XXXMXX-ih_20000090-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/mix/0/C010-ICAVSP-00023-HKUSTXXX-XXXFXX-ih_20000098-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/mix/0/C011-ICAVSP-00007-HKUSTXXX-XXXMXX-ih_20000007-2spk_S1_S4-BackgroundMusic_Rain_Hail_Ignition-DifferentGender"
print_figure(name)

# official clean

name = "test_audio_ciavsr/official_clean/15/C010-ICAVSP-00009-HKUSTXXX-XXXFXX-ih_10000040-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/official_clean/15/C010-ICAVSP-00015-HKUSTXXX-XXXMXX-ih_20000090-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/official_clean/15/C010-ICAVSP-00023-HKUSTXXX-XXXFXX-ih_20000098-2spk_S1_S3-WindscreenWiper_Horn_RoadAmbiance_Alarm_CarDoor-SameGender"
print_figure(name)
name = "test_audio_ciavsr/official_clean/15/C011-ICAVSP-00007-HKUSTXXX-XXXMXX-ih_20000007-2spk_S1_S4-BackgroundMusic_Rain_Hail_Ignition-DifferentGender"
print_figure(name)
