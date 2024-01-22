import pandas as pd
import numpy as np
import cmprsk.cmprsk as cmprsk
from lifelines import KaplanMeierFitter,CoxPHFitter
from cmprsk import utils
from lifelines.datasets import load_rossi, load_dd
from matplotlib import pyplot as plt
def cmprsk_cuminc_analysis():
    np.random.seed(2)
    ss = np.random.exponential(size=100)
    gg = np.random.choice([1, 2, 3], size=100, replace=True)
    cc = np.random.choice([0, 1, 2], size=100, replace=True)
    strt = np.random.choice([1, 2], size=100, replace=True)

    cuminc_res = cmprsk.cuminc(ss, cc, gg, strt)
    print(cuminc_res.print)
    _, ax = plt.subplots()
    for name, group in cuminc_res.groups.items():
        ax.plot(group.time, group.est, label=name)
        ax.fill_between(group.time, group.low_ci, group.high_ci, alpha=0.4)

    ax.set_ylim([0, 1])
    ax.legend()
    ax.set_title('foo bar')
    plt.show()

def cmprsk_crr_analysis():
    np.random.seed(10)
    ftime = np.random.exponential(size=200)
    fstatus = np.random.choice([0, 1, 2], size=200, replace=True)
    cov = np.random.uniform(size=(200, 3))
    cov_columns = ['x1', 'x2', 'x3']
    cov_df = pd.DataFrame({cov_columns[0]: cov[:, 0], cov_columns[1]: cov[:, 1], cov_columns[2]: cov[:, 2]})

    print(cov_df)
    crr_result = cmprsk.crr(ftime,fstatus,cov_df,failcode=2)
    print('Hazard ratio',crr_result.hazard_ratio())

if __name__=='__main__':
    #mprsk_crr_analysis()
    cmprsk_cuminc_analysis()