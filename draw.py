# import matplotlib.pyplot as plt
# import numpy as np
#
# x = np.arange(1, 6, 1)
# y1 = [53.8, 60, 55, 56.3, 53.8]         # 第一条线的数据，y值在0到50之间
# y2 = [0.27, 0.33, 0.28, 0.28, 0.23]        # 第二条线的数据，y值在0到0.5之间
#
# fig, ax1 = plt.subplots()
#
# plt.xticks(x)
# # 绘制第一条线，使用蓝色，左侧y轴
# line1, = ax1.plot(x, y1, 'b-', label='Acc. (%)', marker='o')  # 为图例添加标签
# ax1.set_xlabel('Discussion Turns')
# ax1.set_ylabel('Acc. (%)', color='b')
# ax1.tick_params('y', colors='b')
# ax1.grid(True, axis='both', linestyle='-')  # 添加y轴的刻度线
#
# ax2 = ax1.twinx()  # 创建具有相同x轴的第二个y轴
# # 绘制第二条线，使用红色，右侧y轴
# line2, = ax2.plot(x, y2, 'r-', label='Kap.', marker='x')  # 为图例添加标签
# ax2.set_ylabel('Kap.', color='r')
# ax2.tick_params('y', colors='r')
# ax2.grid(True, axis='both', linestyle='--')  # 添加y轴的刻度线
#
# # plt.title('Two Lines with Different Scales')
#
# # 添加图例
# lines = [line1, line2]
# labels = [l.get_label() for l in lines]
# plt.legend(lines, labels, loc='best')
#
# plt.tight_layout()
# plt.savefig('discussion_turns.pdf')
# plt.show()



import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6, 1)
y1 = [53.8, 60, 62.5, 62.5, 58.8]         # 第一条线的数据，y值在0到50之间
y2 = [0.27, 0.33, 0.37, 0.38, 0.32]        # 第二条线的数据，y值在0到0.5之间

fig, ax1 = plt.subplots()

plt.xticks(x)
# 绘制第一条线，使用蓝色，左侧y轴
line1, = ax1.plot(x, y1, 'b-', label='Acc. (%)', marker='o')  # 为图例添加标签
ax1.set_xlabel('Role Numbers')
ax1.set_ylabel('Acc. (%)', color='b')
ax1.tick_params('y', colors='b')
ax1.grid(True, axis='both', linestyle='-')  # 添加y轴的刻度线

ax2 = ax1.twinx()  # 创建具有相同x轴的第二个y轴
# 绘制第二条线，使用红色，右侧y轴
line2, = ax2.plot(x, y2, 'r-', label='Kap.', marker='x')  # 为图例添加标签
ax2.set_ylabel('Kap.', color='r')
ax2.tick_params('y', colors='r')
ax2.grid(True, axis='both', linestyle='--')  # 添加y轴的刻度线

# plt.title('Two Lines with Different Scales')

# 添加图例
lines = [line1, line2]
labels = [l.get_label() for l in lines]
plt.legend(lines, labels, loc='best')

plt.tight_layout()
plt.savefig('agent_nums.pdf')
plt.show()