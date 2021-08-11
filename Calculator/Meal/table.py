import sys,os
import random

def firstimeresponse():
    print("今天吃什麼?")
    print("早餐:1","午餐:2","晚餐:3","宵夜:4","飲料:5","要不要衝:0")

def morthing():
    table=[
    "麥味登","萬家鄉","早安美之城","拉亞漢堡","全家","7-11","麥樂多","麥軒","其他"
    ]
    Final=random.randint(0,len(table)-1)
    return(table[Final])

def evening():
    table=[
    "小姨拌麵","麥味登","早安美之城","蘭州拉麵","全家","7-11","港龍燒臘","龍城燒臘","羹大王",
    "珍味小館","八方雲集","學生食堂","極鮮坊","其他"
    ]
    Final=random.randint(0,len(table)-1)
    return(table[Final]) 

def night():
    table=[
    "肉粽伯","餐車","齊庭簡餐","學生食堂","全家","7-11","羹大王","小姨拌麵","八方雲集","極鮮坊",
    "珍味小館","允八芳","其他","林記興滷味","陳媽媽小吃","心饗食城"
    ]
    Final=random.randint(0,len(table)-1)
    return(table[Final])

def dim():
    table=[
    "鹽水雞","全家","ayan炸雞","優派","皇家貴族派","章魚燒","其他"
    ]
    Final=random.randint(0,len(table)-1)
    return(table[Final])
def beingornot():
    final=random.randint(0,1)
    event=["不要/不要買/不要吃","買/買爆/吃爆"]

    Final=random.randint(0,len(event)-1)
    return(event[Final])
def drink():
    table=[
        "清心福全-多多綠茶","鮮茶道","叮哥茶飲","清心福全-綠茶","清心福全-自由","其他"
    ]
    Final=random.randint(0,len(table)-1)
    return(table[Final])

def shutdown():
    os.system('pause') 
    sys.exit()
