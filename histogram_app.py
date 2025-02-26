import streamlit as st
import numpy as np
import plotly.figure_factory as ff
import scipy
import matplotlib


# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200)
x4 = np.random.randn(200) - 2
x5 = np.random.randn(200)
x6 = np.random.randn(200)
x7 = np.random.randn(200)
#变化于此
# Group data together

hist_data = [x1, x2, x3]
hist_data = [x4, x5, x6]
x7 = np.random.randn(200)
x7 = np.random.randn(200)
x7 = np.random.randn(200)
x7 = np.random.randn(200)
x7 = np.random.randn(200)
x7 = np.random.randn(200)
x7 = np.random.randn(200)
x7 = np.random.randn(200)
x7 = np.random.randn(200)
x7 = np.random.randn(200)
group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.5, .5, .5])

# Plot!
st.plotly_chart(fig)


