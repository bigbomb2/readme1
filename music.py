from tkinter import *  # init __all__=[a]   *为导入all列表之中的文件


# 爬取网易云音乐
def download_song():
    pass
# 搭建界面

# 创建窗口
root=Tk() # root为最大副题窗口
# 窗口标题
root.title("网易云音乐")
# 窗口大小   小写x代表乘
root.geometry("550x400+550+230")
# 窗口出现在屏幕中的位置
# root.geometry("+550+230")   # 距离屏幕左上距离
# 创建标签控件
label=Label(root,text="请输入要下载的歌单URL",font=('华文行楷，10'))
# 定位  grid 网格式布局   pack  包 place位置
label.grid()

# 输入框
entry=Entry(root,font=('微软雅黑',20))
entry.grid(row=0,column=1)

# 列表框控件
text=Listbox(root,font=('微软雅黑',14),width=49,height=11)
# columnspan  组件跨越的列数
text.grid(row=1,columnspan=2)

# 点击按钮
button=Button(root,text="开始下载",font=('微软雅黑',14),command=download_song)
# sticky 对齐方式  N   S   W   E
button.grid(row=2,column=0,sticky=W)

# command 点击触发的方法
button1=Button(root,text="退出",font=('微软雅黑',14),command=root.quit)
button1.grid(row=2,column=1,sticky=E)


# 显示窗口  消息循环
root.mainloop()


# 爬取网易云音乐