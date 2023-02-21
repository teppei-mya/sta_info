# import googlemaps
# import pandas as pd

# df = pd.read_excel('data/stadium.xlsx')

# gm = googlemaps.Client(key='AIzaSyA76135QmRTiEL8zzLRCit84ZO1UtVICug')

# for i, r in df.iterrows():
#     res = gm.geocode(r['スタジアム名'])
#     try:
#         df.loc[i,'緯度'] = res[0]['geometry']['location']['lat']
#         df.loc[i,'経度'] = res[0]['geometry']['location']['lng']
#     except IndexError:
#         print(str(i) + ':error ')
        

    # print(i)
    # print(res[0]['geometry']['location'])

# df.to_excel('data/stadium.xlsx', index=None)

import folium
from folium.features import CustomIcon
# from folium.features import DivIcon ←マーカを自由に変えることができる
import pandas as pd

##### 自作画像をアイコンにする #####
icon = CustomIcon(
    icon_image = 'images/ball.png',
    icon_size = (50, 50),
    icon_anchor = (30, 30),
    popup_anchor = (3, 3),
)

df = pd.read_excel('data/stadium.xlsx')

map = folium.Map(location=[df.loc[0,'緯度'], df.loc[0, '経度']], zoom_start=7)

for i, r in df.iterrows():
    folium.Marker(location=[r['緯度'],
        r['経度']], 
        tooltip=r['スタジアム名'], 
        popup=r['スタジアム名'], 
        html='<div style="max-width:100px;></div>',
        # icon = icon,
     ).add_to(map)

map.save("sta_infos/map.html")