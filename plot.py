import matplotlib.pyplot as plt
import numpy as np
import config

def parse_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    data = {}
    groups = []
    title = ""

    for line in lines:
        line = line.strip()
        if line.startswith('name='):
            title = line.split('=')[1]
        elif line.startswith('group='):
            group = line.split('=')[1]
            groups.append(group)
            data[group] = []
        else:
            values = list(map(int, line.split(',')))
            data[group].extend(values)
    
    return title, groups, data

def plot_data(title, groups, data):
    n_groups = len(groups)
    index = np.arange(n_groups) * (1 + config.group_spacing_factor)

    fig, ax = plt.subplots(figsize=config.quartfigsize, dpi=config.dpi)
    
    for group_index, group in enumerate(groups):
        local_value = data[group][0]
        nvmeOF_value = data[group][1]

        plt.bar(index[group_index], local_value, config.bar_width, color=config.colors[0], edgecolor=config.edgecolor, linewidth=config.linewidth_2)
        plt.bar(index[group_index] + config.bar_width, nvmeOF_value, config.bar_width, color=config.colors[1], edgecolor=config.edgecolor, linewidth=config.linewidth_2)

        # Add labels below each bar
        plt.text(index[group_index], config.bar_names_loc, 'L', ha='center', fontsize=config.fontsize-3)
        plt.text(index[group_index] + config.bar_width, config.bar_names_loc, 'R', ha='center', fontsize=config.fontsize-3)

    plt.xlabel('Workloads', fontsize=config.fontsize,)
    plt.ylabel('Gigabytes', fontsize=config.fontsize,)
    plt.xticks(index + config.bar_width / 2, groups, fontsize=config.fontsize, rotation=0)
    plt.yticks(fontsize=config.fontsize)

    # Adjust the position of the workload names (group names)
    ax.set_xticks(index + config.bar_width / 2)
    ax.set_xticklabels(groups, fontsize=config.fontsize,rotation=40)
    for tick in ax.get_xticklabels():
        tick.set_y(config.workload_name_pos)  # Lower the position of the workload names

    # Add legend
    #legend_elements = [
     #   plt.Rectangle((0, 0), 1, 1, color=config.colors[0], edgecolor='w', label='local'),
      #  plt.Rectangle((0, 0), 1, 1, color=config.colors[1], edgecolor='w', label='nvmeOF')
    #]
    #ax.legend(handles=legend_elements, fontsize=config.fontsize, loc='upper center', bbox_to_anchor=config.bbox_to_anchor, ncol=2)  # Lowered the legend

    plt.tight_layout()
    plt.subplots_adjust(bottom=0.25)  # Adjust bottom margin to add space for x-axis labels
    plt.savefig('plot.eps',bbox_inches='tight', dpi=config.dpi,format='eps')

def main(filename):
    title, groups, data = parse_data(filename)
    plot_data(title, groups, data)

if __name__ == "__main__":
    main('data.txt')
