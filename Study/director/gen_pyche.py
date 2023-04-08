from pyecharts.charts import  Line,Pie,Bar
from pyecharts  import options as opts
import datetime
from pyecharts.faker import  Faker
from pyecharts.render import make_snapshot
# local_time = datetime.datetime.now()
# print(local_time)
list1 = [15, 20, 30, 56, 88]
list2 = [55, 33, 66, 99, 88]
list3 = ['error1','error2','error3','error4']
list4 = [20,25,22,63]
# a = list(zip(list1,list2))
# print(a)
# b = [x for x in zip(list1,list2)]
# print(b)

def gen_line(dirpath):
    '通过第三方库pyecharts绘制折线图line'
    line = Line()
    line.add_xaxis(['衣服', '鞋子', '服装', '裤子', '包包'])
    line.add_yaxis('a店', list1)
    line.add_yaxis('b店', list2)
    line.set_global_opts(
        title_opts=opts.TitleOpts(title="商家店面销售对比", title_link='https://www.baidu.com/', subtitle='副标题'))
    line.render(dirpath+'/'+'line_render.html')
    return line
    # line.render_notebook()
def gen_bar(dirpath):
    '通过第三方库pyecharts绘制柱状图 Bar'
    bar = (
        Bar()
        .add_xaxis(Faker.choose())
        .add_yaxis('类型1', Faker.values())
        .add_yaxis('类型2', Faker.values())
        .set_global_opts(
        title_opts=opts.TitleOpts(title='类型比较', title_link='https://www.baidu.com', subtitle='这是一个副标题'),
            legend_opts=opts.LegendOpts(pos_right='right')
    )
        .render(dirpath+'/bar_render.html')
    )
    return bar
#
def gen_pie():
    '绘制饼图 Pie'
    pie =(
        Pie()
        .add('', list(zip(list3, list4)))
        .set_global_opts(title_opts=opts.TitleOpts(title='饼图类型比较', subtitle='副标题'),   #何止图表标题
                         legend_opts=opts.LegendOpts(pos_right='right'))   #图标的显示位置
        .set_series_opts(label_opts=opts.LabelOpts(formatter='{b}:{c}:{d}%'))   #图的比例显示
        .render()   #渲染
    )




if __name__ == '__main__':
    dirpath = 'D:/study'
    gen_line(dirpath)
    gen_bar(dirpath)
    gen_pie()
