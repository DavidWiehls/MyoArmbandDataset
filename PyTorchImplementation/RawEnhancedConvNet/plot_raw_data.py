import load_pre_training_dataset as lptd
import matplotlib.pyplot as plt
import numpy as np
import os 
def plot_raw_data(data):
    # Create time array (assuming 5ms steps)
    time_steps = 0.005 * np.arange(data.shape[1])

    # Create a grid of subplots with 4 rows and 2 columns
    fig, axes = plt.subplots(4, 2, figsize=(30, 15))

    # Flatten the axes array for easier indexing
    axes = axes.flatten()

    for i in range(data.shape[0]):
        # Plot the i-th channel data
        axes[i].plot(time_steps, data[i, :])
        #axes[i].set_xlabel('Time (ms)')
        axes[i].set_ylabel(f'Channel {i+1} value')
        #axes[i].set_title(f'Channel {i} vs. Time (ms)')
        axes[i].grid(True)

    # Adjust the layout to avoid overlapping labels
    plt.tight_layout()
    #plt.show()
    if not os.path.exists('plots'):
        os.makedirs('plots')
    plt.savefig(f'plots/plot_{candidate}_{classe_number}.png')
    plt.close(fig)

def read_data(candidate,classe_number):
    
    data_read_from_file = np.fromfile('../../PreTrainingDataset/Male'+str(candidate)+'/training0/classe_%d.dat' % classe_number,
                                              dtype=np.int16)
    data_read_from_file = np.array(data_read_from_file, dtype=np.float32)
    
    ## Create a list of arrays, each array is a gesture
    example = []
    emg_vector = []
    for value in data_read_from_file:
        emg_vector.append(value)
        if (len(emg_vector) >= 8):
            if (example == []):
                example = emg_vector
            else:
                example = np.row_stack((example, emg_vector))
            emg_vector = []
    example = example.transpose()
    
    return example

candidate = 0
classe_number = 0
for classe_number in range(24):
    data = read_data(candidate=candidate,classe_number=classe_number)
    plot_raw_data(data)