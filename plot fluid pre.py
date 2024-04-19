import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file_path ="D:\Desktop\graduate paper\ spaw fluid pinns data_pred.npz"

# 加载预测数据
predictions = np.load(file_path)
u11_pre = predictions["u11_pred"]
u12_pre = predictions["u12_pred"]
p1_pre = predictions["p1_pred"]
u21_pre = predictions["u21_pred"]
u22_pre = predictions["u22_pred"]
p2_pre = predictions["p2_pred"]
X_pre_1 = predictions["x_pred_1"]
X_pre_2 = predictions["x_pred_2"]

# 创建包含所有子图的图形
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(15, 10), subplot_kw={'projection': '3d'},
                        gridspec_kw={'hspace': 0.4, 'wspace': 0.4})

# 3D plot of u11
p1 = axs[0, 0].scatter(X_pre_1[:, 0], X_pre_1[:, 1], X_pre_1[:, 2], c=u11_pre, cmap='viridis')
axs[0, 0].set_title('prediction of u11')
axs[0, 0].set_xlabel('x')
axs[0, 0].set_ylabel('y')
axs[0, 0].set_zlabel('t')
cbar1 = fig.colorbar(p1, ax=axs[0, 0], orientation='vertical', location='left', fraction=0.02, pad=0.1)
cbar1.ax.tick_params(labelsize=8)

# 3D plot of u12
p2 = axs[0, 1].scatter(X_pre_1[:, 0], X_pre_1[:, 1], X_pre_1[:, 2], c=u12_pre, cmap='viridis')
axs[0, 1].set_title('prediction of u12')
axs[0, 1].set_xlabel('x')
axs[0, 1].set_ylabel('y')
axs[0, 1].set_zlabel('t')
cbar2 = fig.colorbar(p2, ax=axs[0, 1], orientation='vertical', location='left', fraction=0.02, pad=0.1)
cbar2.ax.tick_params(labelsize=8)

# 3D plot of p1
p3 = axs[0, 2].scatter(X_pre_1[:, 0], X_pre_1[:, 1], X_pre_1[:, 2], c=p1_pre, cmap='viridis')
axs[0, 2].set_title('prediction of p1')
axs[0, 2].set_xlabel('x')
axs[0, 2].set_ylabel('y')
axs[0, 2].set_zlabel('t')
cbar3 = fig.colorbar(p3, ax=axs[0, 2], orientation='vertical', location='left', fraction=0.02, pad=0.1)
cbar3.ax.tick_params(labelsize=8)

# 3D plot of u21
p4 = axs[1, 0].scatter(X_pre_2[:, 0], X_pre_2[:, 1], X_pre_2[:, 2], c=u21_pre, cmap='viridis')
axs[1, 0].set_title('prediction of u21')
axs[1, 0].set_xlabel('x')
axs[1, 0].set_ylabel('y')
axs[1, 0].set_zlabel('t')
cbar4 = fig.colorbar(p4, ax=axs[1, 0], orientation='vertical', location='left', fraction=0.02, pad=0.1)
cbar4.ax.tick_params(labelsize=8)

# 3D plot of u22
p5 = axs[1, 1].scatter(X_pre_2[:, 0], X_pre_2[:, 1], X_pre_2[:, 2], c=u22_pre, cmap='viridis')
axs[1, 1].set_title('prediction of u22')
axs[1, 1].set_xlabel('x')
axs[1, 1].set_ylabel('y')
axs[1, 1].set_zlabel('t')
cbar5 = fig.colorbar(p5, ax=axs[1, 1], orientation='vertical', location='left', fraction=0.02, pad=0.1)
cbar5.ax.tick_params(labelsize=8)

# 3D plot of p2
p6 = axs[1, 2].scatter(X_pre_2[:, 0], X_pre_2[:, 1], X_pre_2[:, 2], c=p2_pre, cmap='viridis')
axs[1, 2].set_title('prediction of p2')
axs[1, 2].set_xlabel('x')
axs[1, 2].set_ylabel('y')
axs[1, 2].set_zlabel('t')
cbar6 = fig.colorbar(p6, ax=axs[1, 2], orientation='vertical', location='left', fraction=0.02, pad=0.1)
cbar6.ax.tick_params(labelsize=8)

# 显示图形
plt.show()
# 绘制 p1 的三维图形
ax3 = fig.add_subplot(233, projection='3d')
p3 = ax3.scatter(X_pre_1[:, 0], X_pre_1[:, 1], X_pre_1[:, 2], c=p1_pre, cmap='viridis')
ax3.set_title('prediction of p1')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_zlabel('t')
cbar3 = fig.colorbar(p3, ax=ax3, orientation='vertical', location='left', fraction=0.046, pad=0.04)
cbar3.ax.tick_params(labelsize=8)

# 绘制 u21 的三维图形
ax4 = fig.add_subplot(234, projection='3d')
p4 = ax4.scatter(X_pre_2[:, 0], X_pre_2[:, 1], X_pre_2[:, 2], c=u21_pre, cmap='viridis')
ax4.set_title('prediction of u21')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_zlabel('t')
cbar4 = fig.colorbar(p4, ax=ax4, orientation='vertical', location='left', fraction=0.046, pad=0.04)
cbar4.ax.tick_params(labelsize=8)

# 绘制 u22 的三维图形
ax5 = fig.add_subplot(235, projection='3d')
p5 = ax5.scatter(X_pre_2[:, 0], X_pre_2[:, 1], X_pre_2[:, 2], c=u22_pre, cmap='viridis')
ax5.set_title('prediction of u22')
ax5.set_xlabel('x')
ax5.set_ylabel('y')
ax5.set_zlabel('t')
cbar5 = fig.colorbar(p5, ax=ax5, orientation='vertical', location='left', fraction=0.046, pad=0.04)
cbar5.ax.tick_params(labelsize=8)
# 绘制 p2 的三维图形
ax6 = fig.add_subplot(236, projection='3d')
p6 = ax6.scatter(X_pre_2[:, 0], X_pre_2[:, 1], X_pre_2[:, 2], c=p2_pre, cmap='viridis')
ax6.set_title('prediction of p2')
ax6.set_xlabel('x')
ax6.set_ylabel('y')
ax6.set_zlabel('t')
cbar6 = fig.colorbar(p6, ax=ax6, orientation='vertical', location='left', fraction=0.046, pad=0.04)
cbar6.ax.tick_params(labelsize=8)

# 显示图形
plt.show()
