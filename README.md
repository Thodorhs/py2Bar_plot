# py2Bar_plot
Python script to generate bar plots for groups with two bars each: one for `local` and one for `nvmeOF`.

## Example Plot

![Example Plot](https://raw.githubusercontent.com/Thodorhs/py2Bar_plot/main/plot.png)

## Overview

This script is designed to read data from a file, parse it, and generate a bar plot. Each group in the dataset will have two bars: one for `local` and one for `nvmeOF`.

## Script Configuration

The script uses a configuration file (`config.py`) to set various plot parameters:

- `fullfigsize = (13, 2)`: Full figure size.
- `halffigsize = (7, 3)`: Half figure size.
- `thirdfigsize = (5, 3)`: One third figure size.
- `quartfigsize = (3.25, 3)`: One fourth figure size.
- `eightfigsize = (1.625, 1.6)`: One eighth figure size.
- `fontsize = 12`: Font size.
- `linewidth = 3`: Graph line width.
- `linewidth_2 = 0.6`: Secondary line width.
- `edgewidth = 1.2`: Edge width.
- `edgecolor = 'k'`: Edge color (black).
- `markersize = 12`: Marker size.
- `bar_width = 0.5`: Bar width.
- `colors = ['#444444', '#888888', '#cccccc']`: Color palette for the bars.
- `dpi = 450`: Quality of the plot (Dots Per Inches).
- `workload_name_pos = 0`: Position adjustment for workload names.
- `bbox_to_anchor = (0.5, 1)`: Legend position.
- `bar_names_loc = -120`: Position adjustment for bar names.
- `group_spacing_factor = 0.25`: Factor to control the spacing between groups.

## Data File (`data.txt`)

The data file should contain information about the plot in a specific format. Below is a sample `data.txt` file:

```
name=Spark Reads
group=PR
337,379
group=CC
373,369
group=LR
1031,982
group=LgR
976,1033
group=TR
9,9
group=SSSP
275,270
group=SVD
154,156
group=SVM
227,2980
```

### Explanation

- `name`: Title of the plot.
- `group`: Name of each group.
- The following lines contain two values for each group, corresponding to `local` and `nvmeOF`.

## Usage

1. **Prepare your `data.txt` file** following the format described above.

2. **Run the script**:
   ```bash
   python3 plot_data.py

