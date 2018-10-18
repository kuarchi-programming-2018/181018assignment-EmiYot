# -*- coding: utf-8 -*-

points = {"国語" : 70, "算数" : 35, "英語" : 52}
sum = 0
# この下で、辞書の値の合計をループで計算してみよう
for total in points:
    sum += points[total]
print(int(sum))
    
    
    