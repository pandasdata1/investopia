import sys #line:1
import os #line:2
import warnings #line:3
warnings .filterwarnings (action ='ignore')#line:4
from getpass import getpass #line:5
import webbrowser #line:6
import ctypes #line:7
import tkinter as tk #line:8
import tkinter .ttk #line:9
from tkinter import messagebox #line:10
import pandas as pd #line:11
import matplotlib .pyplot as plt #line:12
from matplotlib .widgets import Slider ,Button ,RadioButtons #line:13
import FinanceDataReader as fdr #line:14
import datetime #line:15
from datetime import date ,timedelta #line:16
import matplotlib .lines as mlines #line:17
import numpy as np #line:18
import matplotlib .patheffects as path_effects #line:19
from pykrx import stock #line:20
from pandas import DataFrame #line:21
from tkinter import *#line:22
from matplotlib .widgets import TextBox #line:23
df_today =datetime .datetime .now ().date ()#line:25
today =df_today .isoformat ()#line:26
while True :#line:28
    root =Tk ()#line:30
    root .title ('▒▒INVESTOPIA▒'+today +'▒▒Perspective&Performance▒')#line:31
    root .geometry ("637x63")#line:32
    root .config (bg ='#4682B4')#line:33
    root .resizable (width =False ,height =False )#line:34
    root .attributes ('-topmost',True )#line:35
    mystring =StringVar ()#line:37
    def getvalue ():#line:38
        print (mystring .get ())#line:39
    Label (root ,text ="종목 입력창",bg ='#4682B4',font ='맑은고딕 11 bold',foreground ='white').grid (row =0 ,column =0 ,sticky =W +E +N +S ,padx =5 ,pady =15 )#line:41
    Entry (root ,textvariable =mystring ,justify =CENTER ,foreground ='#4682B4',width =29 ,font ='맑은고딕 11 bold',relief ='solid',bd =4 ,highlightbackground ='black',highlightcolor ='black').grid (row =0 ,column =1 ,sticky =W +E +N +S ,ipadx =5 ,ipady =15 )#line:42
    WSingUp =Button (root ,fg ="white",bg ="black",font ='맑은고딕 11 bold',relief ='solid',overrelief ='sunken',bd =1 ,width =30 ,bitmap ='question',command =root .destroy ).grid (row =0 ,column =2 ,sticky =W +E +N +S ,ipadx =5 ,ipady =15 )#line:43
    Label (root ,text =" PANDAS DATA",bg ='#4682B4',font ='맑은고딕 11 bold',foreground ='white').grid (row =0 ,column =3 ,sticky =W +E +N +S ,padx =5 ,pady =15 )#line:44
    root .mainloop ()#line:45
    stocksellection =mystring .get ()#line:47
    portion =1.1 #line:50
    marketfollowing =1.15 #line:51
    daydays =365 #line:52
    while portion >1.0 :#line:56
        widthe =(df_today -datetime .timedelta (days =daydays )).isoformat ()#line:58
        url ='http://kind.krx.co.kr/corpgeneral/corpList.do?method=download'#line:60
        df_code =pd .read_html (url ,header =0 )[0 ]#line:61
        df_code ['종목코드']=df_code ['종목코드'].astype (str )#line:62
        df_code ['주요제품']=df_code ['주요제품'].astype (str )#line:63
        df_code ['업종']=df_code ['업종'].astype (str )#line:64
        df_code ['홈페이지']=df_code ['홈페이지'].astype (str )#line:65
        df_code ['상장일']=df_code ['상장일'].astype (str )#line:66
        df_code ['종목코드']=df_code ['종목코드'].apply (lambda O00O00O00OO00000O :O00O00O00OO00000O .zfill (6 ))#line:67
        df_code ['주요제품']=df_code ['주요제품'].apply (lambda OO0OO000OOO0OO000 :OO0OO000OOO0OO000 [:91 ])#line:68
        df_code ['주요제품']=df_code ['주요제품'].apply (lambda OOOO0O000OOO000O0 :OOOO0O000OOO000O0 +'..')#line:69
        df_code ['주요제품']=df_code ['주요제품'].apply (lambda OOO0O000OOOO0O00O :'주요제품 :'+OOO0O000OOOO0O00O )#line:71
        df_code ['업종']=df_code ['업종'].apply (lambda O0O00OOO0O00OOO00 :O0O00OOO0O00OOO00 [:61 ])#line:72
        df_code ['홈페이지']=df_code ['홈페이지'].apply (lambda OO000O00O0O0O000O :OO000O00O0O0O000O [:61 ])#line:74
        df_code ['홈페이지']=df_code ['홈페이지'].apply (lambda OO0OO0OOO00OO000O :'홈페이지 :'+OO0OO0OOO00OO000O )#line:75
        df_code ['상장일']=df_code ['상장일'].apply (lambda OOOOOOOO0O0000000 :'상장일 :'+OOOOOOOO0O0000000 )#line:76
        data_code =list (df_code ['종목코드'].values )#line:77
        data_product =list (df_code ['주요제품'].values )#line:78
        index_code =list (df_code ['회사명'].values )#line:79
        industry_code =list (df_code ['업종'].values )#line:80
        industry_code_blankoff =[OOO00OO0O000000OO .replace (' ','')for OOO00OO0O000000OO in industry_code ]#line:81
        homepage_code =list (df_code ['홈페이지'].values )#line:82
        startbegin_code =list (df_code ['상장일'].values )#line:83
        ss =pd .Series (data_code ,index =index_code )#line:84
        pp =pd .Series (data_product ,index =index_code )#line:85
        hh =pd .Series (industry_code ,index =index_code )#line:86
        hp =pd .Series (homepage_code ,index =index_code )#line:87
        stb =pd .Series (startbegin_code ,index =index_code )#line:88
        qwe =pd .Series (index_code ,index =industry_code_blankoff )#line:89
        df_1yago =df_today -datetime .timedelta (days =365 )#line:90
        y1ago =df_1yago .isoformat ()#line:91
        df_6mago =df_today -datetime .timedelta (days =182 )#line:92
        m6ago =df_6mago .isoformat ()#line:93
        df =pd .read_excel ('c:/pandasdata/stock정제.xlsx')#line:95
        df ["다"]=df ["다"].str .replace ("살루딩삵","카카오")#line:96
        df ["다"]=df ["다"].str .replace ("솔빈덴삵","삼성전자")#line:97
        df ["다"]=df ["다"].str .replace ("그룹스펠삵","힘스")#line:98
        df ["다"]=df ["다"].str .replace ("콘스트풀삵","흥아해운")#line:99
        df ["다"]=df ["다"].str .replace ("베벨스타삵","CJ ENM")#line:100
        df ["다"]=df ["다"].str .replace ("헴마픽사레삵","에이치엘비")#line:101
        df ["다"]=df ["다"].str .replace ("드뢰니엔스삵","삼성바이오로직스")#line:102
        df ["다"]=df ["다"].str .replace ("소케르비트삵","LG전자")#line:103
        df ["다"]=df ["다"].str .replace ("레투가드삵","NH투자증권")#line:104
        df ["다"]=df ["다"].str .replace ("베스템마삵","POSCO")#line:105
        df ["다"]=df ["다"].str .replace ("룸메르벡스트삵","스튜디오드래곤")#line:106
        df ["다"]=df ["다"].str .replace ("라프뉘클라르삵","LG화학")#line:107
        df ["다"]=df ["다"].str .replace ("릴셰른삵","삼성물산")#line:108
        df ["다"]=df ["다"].str .replace ("클렙스타드삵","린드먼아시아")#line:109
        df ["다"]=df ["다"].str .replace ("엔투시아슴삵","국일제지")#line:110
        df ["다"]=df ["다"].str .replace ("그라드비스삵","하림")#line:111
        df ["다"]=df ["다"].str .replace ("오스뷔셴삵","아난티")#line:112
        df ["다"]=df ["다"].str .replace ("페리클라르삵","한국종합기술")#line:113
        df ["다"]=df ["다"].str .replace ("이스브뤼타레삵","SK렌터카")#line:114
        df ["다"]=df ["다"].str .replace ("쿠기스삵","미스터블루")#line:115
        df ["다"]=df ["다"].str .replace ("헤스타게삵","시디즈")#line:116
        df ["다"]=df ["다"].str .replace ("페이카삵","대웅")#line:117
        df ["다"]=df ["다"].str .replace ("위테르셰르삵","롯데리츠")#line:118
        df ["다"]=df ["다"].str .replace ("우틀렝안삵","DI동일")#line:119
        df ["다"]=df ["다"].str .replace ("리나네스삵","NH프라임리츠")#line:120
        df ["다"]=df ["다"].str .replace ("칼락스삵","다우데이타")#line:121
        df ["다"]=df ["다"].str .replace ("트롤돔삵","이노메트리")#line:122
        df ["다"]=df ["다"].str .replace ("토르군삵","씨티케이")#line:123
        df ["다"]=df ["다"].str .replace ("순쇠삵","IHQ")#line:124
        df ["다"]=df ["다"].str .replace ("스뮈카삵","드래곤플라이")#line:125
        df ["다"]=df ["다"].str .replace ("브룬베르삵","한화에어로스페이스")#line:126
        df ["다"]=df ["다"].str .replace ("코싱엔삵","TIGER 인버스")#line:127
        df ["다"]=df ["다"].str .replace ("헴네스삵","룽투코리아")#line:128
        df ["다"]=df ["다"].str .replace ("핀니그삵","씨이랩")#line:129
        df ["다"]=df ["다"].str .replace ("빌리삵","실리콘투")#line:130
        df ["다"]=df ["다"].str .replace ("스모스타드삵","TCC스틸")#line:131
        df ["다"]=df ["다"].str .replace ("플리사트삵","원익피앤이")#line:132
        df ["다"]=df ["다"].str .replace ("칼프론트삵","유니퀘스트")#line:133
        df ["다"]=df ["다"].str .replace ("에케트삵","나노스")#line:134
        df ["다"]=df ["다"].str .replace ("뷔글레크삵","네이처셀")#line:135
        df ["다"]=df ["다"].str .replace ("셰나삵","한국주강")#line:136
        df ["다"]=df ["다"].str .replace ("에케나벤삵","마니커")#line:137
        df ["다"]=df ["다"].str .replace ("크록홀멘삵","웅진")#line:138
        df ["다"]=df ["다"].str .replace ("그릴셰르삵","이엔에프테크놀로지")#line:139
        df ["다"]=df ["다"].str .replace ("트로드프리삵","재영솔루텍")#line:140
        df ["다"]=df ["다"].str .replace ("드카스트삵","화승코퍼레이션")#line:141
        df ["다"]=df ["다"].str .replace ("후부스펠라레삵","에프앤가이드")#line:142
        df ["다"]=df ["다"].str .replace ("베스테뢰위삵","형지엘리트")#line:143
        df ["다"]=df ["다"].str .replace ("크나페르삵","KSS해운")#line:144
        df ["다"]=df ["다"].str .replace ("몰라삵","퓨쳐켐")#line:145
        df ["다"]=df ["다"].str .replace ("adsfasd삵","에이플러스에셋")#line:146
        df ["다"]=df ["다"].str .replace ("ad4f5삵","ISC")#line:147
        df ["다"]=df ["다"].str .replace ("yh4y8nh4삵","아이진")#line:148
        df ["다"]=df ["다"].str .replace ("0yh98n9y0삵","위메이드")#line:149
        df ["다"]=df ["다"].str .replace ("1s4fd41g삵","우리들휴브레인")#line:150
        df ["다"]=df ["다"].str .replace ("f4va516삵","KBSTAR 코스닥150")#line:151
        df ["다"]=df ["다"].str .replace ("a24s654g2652삵","KBSTAR 200IT")#line:152
        df ["다"]=df ["다"].str .replace ("2a5fd6f6a2df삵","퍼시스")#line:153
        df ["다"]=df ["다"].str .replace ("5BT2G9B삵","동운아나텍")#line:154
        df ["다"]=df ["다"].str .replace ("1VS65R1EV4삵","코오롱")#line:155
        df ["다"]=df ["다"].str .replace ("1CER56C1FER41삵","유바이오로직스")#line:156
        df ["다"]=df ["다"].str .replace ("14C8R1CF삵","뉴지랩파마")#line:157
        df ["다"]=df ["다"].str .replace ("4avv15dv1삵","메타랩스")#line:158
        df ["다"]=df ["다"].str .replace ("1av8df4d삵","휴마시스")#line:159
        df ["다"]=df ["다"].str .replace ("1sr4g1rv41삵","삼양홀딩스")#line:160
        df ["다"]=df ["다"].str .replace ("41vfr84f삵","한창")#line:161
        df ["다"]=df ["다"].str .replace ("v8etv7g삵","삼천당제약")#line:162
        df ["다"]=df ["다"].str .replace ("8grjb9r8g삵","제넥신")#line:163
        df ["다"]=df ["다"].str .replace ("a8sd6f8a삵","EDGC")#line:164
        df ["다"]=df ["다"].str .replace ("z9cv9z8v7삵","삼진제약")#line:165
        df ["다"]=df ["다"].str .replace ("v7a9d87f9a87v삵","일신석재")#line:166
        df ["다"]=df ["다"].str .replace ("5a67g5v삵","키움증권")#line:167
        df ["다"]=df ["다"].str .replace ("14bw6r8yw삵","카카오페이")#line:168
        df ["다"]=df ["다"].str .replace ("v85nu845vn58nvu39삵","HLB")#line:169
        df ["다"]=df ["다"].str .replace ("14p6l841l81삵","삼성중공업")#line:170
        df ["다"]=df ["다"].str .replace ("1erv8g14삵","이스트소프트")#line:171
        df ["다"]=df ["다"].str .replace ("4q6sx4d삵","SFA반도체")#line:172
        stockoneyou =df #line:173
        time2 =stockoneyou .shape [0 ]/portion #line:174
        time2 =int (time2 )#line:175
        stockoneyou2 =stockoneyou .iloc [time2 :]#line:176
        df =df .drop (['Unnamed: 0'],axis =1 )#line:177
        try :#line:179
                CODE =ss [stocksellection ]#line:180
                PRODUCT =pp [stocksellection ]#line:181
                INDUSTRY =hh [stocksellection ]#line:182
                INDUSTRY_blankoff =INDUSTRY .replace (' ','')#line:183
                HOMEPAGE =hp [stocksellection ]#line:184
                BEGIN =stb [stocksellection ]#line:185
        except KeyError :#line:186
            if stocksellection =="TIGER 인버스":#line:187
                CODE ='123310'#line:188
                PRODUCT ='주요제품 : KOSPI200 지수 반대방향의 수익률을 기대..'#line:189
            elif stocksellection =="KODEX 구리선물(H)":#line:190
                CODE ='138910'#line:191
                PRODUCT ='주요제품 : 동 ETF는 구리현물이 아닌 구리선물에 투자하는 상품..'#line:192
            elif stocksellection =="TIGER 200":#line:193
                CODE ='102110'#line:194
                PRODUCT ='주요제품 :  KOSPI200 지수의 변동률과 유사하도록 운용이 목표..'#line:195
            elif stocksellection =="삼성전자우":#line:196
                CODE ='005935'#line:197
                PRODUCT ='주요제품 :  ..'#line:198
            elif stocksellection =="KBSTAR 코스닥150":#line:199
                CODE ='270810'#line:200
                PRODUCT ='주요제품 : 코스닥150지수를 추적대상지수로 하여 1좌당 순자산..'#line:201
            elif stocksellection =="TIGER 차이나전기차레버리지(합성)":#line:202
                CODE ='456680'#line:203
                PRODUCT ='주요제품 : 차이나전기차 지수의 일간 수익률 2배를 추종하는 국내 최초 상품..'#line:204
            else :#line:205
                print ("\n◇종목명 에러.◇\
        \n↗알파벳 대문자 및 소문자를 정확히 입력해 주세요.\
        \n↗혹시 'F&F홀딩스'를 입력하셨나요? 그렇다면 'F&F 홀딩스'로 다시 입력해주세요.(한칸 띄우기)\
        \n↗혹시 '쌍용차'를 입력하셨나요? 그렇다면 '쌍용자동차'로 다시 입력해주세요.\
        \n↗혹시 'KCC'를 입력하셨나요? 그렇다면 '케이씨씨'로 다시 입력해주세요.\
        \n↗혹시 'IHQ'를 입력하셨나요? 그렇다면 '아이에이치큐'로 다시 입력해주세요.\
        \n↗혹시 'DI동일'를 입력하셨나요? 그렇다면 '디아이동일'로 다시 입력해주세요.\
        \n↗혹시 '현대차'를 입력하셨나요? 그렇다면 '현대자동차'로 다시 입력해주세요.")#line:213
                sys .exit ()#line:214
        chartoday =fdr .DataReader (CODE ,widthe ,today )#line:217
        chart =fdr .DataReader (CODE ,widthe ,chartoday .index .max ())#line:218
        time =df .shape [0 ]/portion #line:219
        time =int (time )#line:220
        df =df .iloc [time :]#line:221
        df ["다"]=df ["다"].str .replace (" ","")#line:223
        df ["다"]=df ["다"].str .replace ("&","")#line:224
        df ["다"]=df ["다"].str .replace ("-","")#line:225
        df ["다"]=df ["다"].str .replace ("(","")#line:226
        df ["다"]=df ["다"].str .replace (")","")#line:227
        data =list (df ['스'].values )#line:228
        index =list (df ['다'].values )#line:229
        s =pd .Series (data ,index =index )#line:230
        NowStockValue =fdr .DataReader (CODE ,chartoday .index .max ())#line:231
        Q =NowStockValue .Close .values #line:232
        try :#line:235
            i =s [stocksellection ]#line:236
        except KeyError :#line:237
            try :#line:238
                if stocksellection =="쌍용자동차":#line:239
                    i =s .쌍용차 #line:240
                elif stocksellection =="현대자동차":#line:241
                    i =s .현대차 #line:242
                elif stocksellection =="케이씨씨":#line:243
                    i =s .KCC #line:244
                elif stocksellection =="F&F 홀딩스":#line:245
                    i =s .FF홀딩스 #line:246
                elif stocksellection =="동원F&B":#line:247
                    i =s .동원FB #line:248
                elif stocksellection =="세이브존I&C":#line:249
                    i =s .세이브존IC #line:250
                elif stocksellection =="CSA 코스믹":#line:251
                    i =s .CSA코스믹 #line:252
                elif stocksellection =="동국S&C":#line:253
                    i =s .동국SC #line:254
                elif stocksellection =="에이프로젠 H&G":#line:255
                    i =s .에이프로젠HG #line:256
                elif stocksellection =="와이지-원":#line:257
                    i =s .와이지원 #line:258
                elif stocksellection =="서부T&D":#line:259
                    i =s .서부TD #line:260
                elif stocksellection =="CJ ENM":#line:261
                    i =s .CJENM #line:262
                elif stocksellection =="디아이동일":#line:263
                    i =s .DI동일 #line:264
                elif stocksellection =="아이에이치큐":#line:265
                    i =s .IHQ #line:266
                elif stocksellection =="TIGER 인버스":#line:267
                    i =s .TIGER인버스 #line:268
                elif stocksellection =="KODEX 구리선물(H)":#line:269
                    i =s .KODEX구리선물H #line:270
                elif stocksellection =="TIGER 200":#line:271
                    i =s .TIGER200 #line:272
                elif stocksellection =="KBSTAR 코스닥150":#line:273
                    i =s .KBSTAR코스닥150 #line:274
                elif stocksellection =="TIGER 차이나전기차레버리지(합성)":#line:275
                    i =s .TIGER차이나전기차레버리지합성 #line:276
                else :#line:277
                    print ("\n◇에러가 발생하였습니다.◇\
                \n↗거래정지 종목 여부를 확인하여 주세요.\
                \n↗세력의 동향이 전혀 나타나지 않는 경우일 수도 있습니다.\
                \n↗혹은, 프로그램 오류일 수 있으니 개발자에게 알려주세요.(개발자 연락처: csipusan@naver.com)")#line:281
                    sys .exit ()#line:283
            except AttributeError :#line:284
                print ("\n▨에러가 발생하였습니다.▨\
            \n↗거래정지 종목 여부를 확인하여 주세요.\
            \n↗세력의 동향이 전혀 나타나지 않는 경우일 수도 있습니다.")#line:287
                sys .exit ()#line:288
        try :#line:290
            setylimdata =pd .DataFrame (i .values ,columns =['ylimdata'])#line:291
        except AttributeError :#line:292
            print ("\n◈에러가 발생하였습니다.◈\
        \n↗거래정지 종목 여부를 확인하여 주세요.\
        \n↗세력의 동향이 전혀 나타나지 않는 경우일 수도 있습니다.")#line:295
            sys .exit ()#line:296
        except NameError :#line:297
            print ("\n◆에러가 발생하였습니다.◆\
        \n↗거래정지 종목 여부를 확인하여 주세요.\
        \n↗세력의 동향이 전혀 나타나지 않는 경우일 수도 있습니다.")#line:300
            sys .exit ()#line:301
        setylimdata2 =pd .DataFrame (chart ['Close'].values ,columns =['ylimdata'])#line:303
        setylimdata3 =pd .merge (setylimdata ,setylimdata2 ,how ='outer')#line:304
        t =(setylimdata3 .max ().values *1.1 -setylimdata3 .min ().values *0.9 )/8.5 #line:305
        high =i .values [i >i .median ()]#line:306
        low =i .values [i <i .median ()]#line:307
        expectation =(i .max ()-i .median ())/(i .max ()-i .min ())#line:308
        expectation2 =(i .median ()-i .min ())/(i .max ()-i .min ())#line:309
        stockoneyou3 =DataFrame (stockoneyou2 ,columns =['판','다','스','데','이','타','인','베','스토','피','아','comp'])#line:311
        stockoneyou3 .comp =stockoneyou3 .데 .str .contains ("A6541ECFA")#line:312
        stockoneyou3 =stockoneyou3 [stockoneyou3 .comp !=False ]#line:313
        stockoneyou4 =DataFrame (stockoneyou ,columns =['판','다','스','데','이','타','인','베','스토','피','아','comp'])#line:314
        stockoneyou4 .comp =stockoneyou4 .데 .str .contains ("A6541ECFA")#line:315
        stockoneyou4 =stockoneyou4 [stockoneyou4 .comp !=False ]#line:316
        grouped =stockoneyou4 .groupby ('다')#line:317
        grouped2 =stockoneyou3 .groupby ('다')#line:318
        weight =grouped2 .count ()[['판']].sort_values (by =['판'],ascending =False )#line:319
        atom =grouped .count ()[['판']].sort_values (by =['판'],ascending =False )#line:320
        atomdata ={'다':atom .index .values ,'atom':atom ['판'].values }#line:321
        weightdata ={'다':weight .index .values ,'weight':weight ['판'].values }#line:322
        atom =pd .DataFrame (atomdata )#line:323
        weight =pd .DataFrame (weightdata )#line:324
        qweframe =DataFrame (qwe [INDUSTRY_blankoff ].values ,columns =['다'])#line:325
        qweframe ['fk']=1004 #line:326
        weight .merge (atom ,left_on ='다',right_on ='다',how ='outer')#line:327
        qweframe2 =qweframe .merge (weight ,left_on ='다',right_on ='다',how ='outer').dropna (axis =0 )#line:328
        planet =weight .merge (atom ,left_on ='다',right_on ='다',how ='outer')#line:329
        planet =DataFrame (planet ,columns =['다','weight','atom','planet'])#line:330
        A =planet ['weight'].values #line:331
        B =planet ['atom'].values #line:332
        C =A *B #line:333
        planet ['planet']=C #line:334
        planet7 =planet .sort_values (by =['planet'],ascending =False ).head (71 )#line:335
        weight7 =planet .sort_values (by =['weight'],ascending =False ).head (71 )#line:336
        qweframe3 =qweframe2 .sort_values (by =['weight'],ascending =False ).head (10 )#line:337
        planet7 ['industryband']=''#line:338
        planet7 ['industryband']=planet7 ['다']#line:339
        planet7 ['회사명']=planet7 ['다']#line:340
        df_code ['업2종']=df_code ['업종']#line:341
        Outer_join =pd .merge (planet7 ,df_code ,on ='회사명',how ='outer')#line:342
        Outer_join =Outer_join .fillna (0 )#line:343
        Outer_join =pd .merge (planet7 ,df_code ,on ='회사명',how ='outer')#line:344
        Outer_join .dropna (axis =0 )#line:345
        Outer_join2 =Outer_join .dropna (axis =0 )#line:346
        grouped4 =Outer_join2 .groupby ('업2종')#line:347
        superior =grouped4 .count ()[['지역']].sort_values (by =['지역'],ascending =False )#line:349
        superiordata ={'업2종':superior .index .values ,'superior':superior ['지역'].values }#line:350
        superior2 =pd .DataFrame (superiordata )#line:351
        superior3 =superior2 .sort_values (by =['superior'],ascending =False ).head (10 )#line:352
        industrybandcon =superior3 .업2종 .values #line:353
        superior3_code =list (superior3 ['업2종'].values )#line:354
        superior3_code_frame =pd .DataFrame (superior3_code )#line:355
        asdfdsa =superior3_code_frame .T [0 ].map (str )+' , '+superior3_code_frame .T [1 ].map (str )+' , '+superior3_code_frame .T [2 ].map (str )+' , '+superior3_code_frame .T [3 ].map (str )+' , '+superior3_code_frame .T [4 ].map (str )+' , '+superior3_code_frame .T [5 ].map (str )+' , '+superior3_code_frame .T [6 ].map (str )+' , '+superior3_code_frame .T [7 ].map (str )+' , '+superior3_code_frame .T [8 ].map (str )+' , '+superior3_code_frame .T [9 ].map (str )#line:356
        superior4_code =list (qweframe3 ['다'].values )#line:357
        superior4_code_frame =pd .DataFrame (superior4_code )#line:358
        if superior4_code_frame .size ==10 :#line:359
            gtbfd =superior4_code_frame .T [0 ].map (str )+' , '+superior4_code_frame .T [1 ].map (str )+' , '+superior4_code_frame .T [2 ].map (str )+' , '+superior4_code_frame .T [3 ].map (str )+' , '+superior4_code_frame .T [4 ].map (str )+' , '+superior4_code_frame .T [5 ].map (str )+' , '+superior4_code_frame .T [6 ].map (str )+' , '+superior4_code_frame .T [7 ].map (str )+' , '+superior4_code_frame .T [8 ].map (str )+' , '+superior4_code_frame .T [9 ].map (str )#line:360
        elif superior4_code_frame .size ==9 :#line:361
            gtbfd =superior4_code_frame .T [0 ].map (str )+' , '+superior4_code_frame .T [1 ].map (str )+' , '+superior4_code_frame .T [2 ].map (str )+' , '+superior4_code_frame .T [3 ].map (str )+' , '+superior4_code_frame .T [4 ].map (str )+' , '+superior4_code_frame .T [5 ].map (str )+' , '+superior4_code_frame .T [6 ].map (str )+' , '+superior4_code_frame .T [7 ].map (str )+' , '+superior4_code_frame .T [8 ].map (str )#line:362
        elif superior4_code_frame .size ==8 :#line:363
            gtbfd =superior4_code_frame .T [0 ].map (str )+' , '+superior4_code_frame .T [1 ].map (str )+' , '+superior4_code_frame .T [2 ].map (str )+' , '+superior4_code_frame .T [3 ].map (str )+' , '+superior4_code_frame .T [4 ].map (str )+' , '+superior4_code_frame .T [5 ].map (str )+' , '+superior4_code_frame .T [6 ].map (str )+' , '+superior4_code_frame .T [7 ].map (str )#line:364
        elif superior4_code_frame .size ==7 :#line:365
            gtbfd =superior4_code_frame .T [0 ].map (str )+' , '+superior4_code_frame .T [1 ].map (str )+' , '+superior4_code_frame .T [2 ].map (str )+' , '+superior4_code_frame .T [3 ].map (str )+' , '+superior4_code_frame .T [4 ].map (str )+' , '+superior4_code_frame .T [5 ].map (str )+' , '+superior4_code_frame .T [6 ].map (str )#line:366
        elif superior4_code_frame .size ==6 :#line:367
            gtbfd =superior4_code_frame .T [0 ].map (str )+' , '+superior4_code_frame .T [1 ].map (str )+' , '+superior4_code_frame .T [2 ].map (str )+' , '+superior4_code_frame .T [3 ].map (str )+' , '+superior4_code_frame .T [4 ].map (str )+' , '+superior4_code_frame .T [5 ].map (str )#line:368
        elif superior4_code_frame .size ==5 :#line:369
            gtbfd =superior4_code_frame .T [0 ].map (str )+' , '+superior4_code_frame .T [1 ].map (str )+' , '+superior4_code_frame .T [2 ].map (str )+' , '+superior4_code_frame .T [3 ].map (str )+' , '+superior4_code_frame .T [4 ].map (str )#line:370
        elif superior4_code_frame .size ==4 :#line:371
            gtbfd =superior4_code_frame .T [0 ].map (str )+' , '+superior4_code_frame .T [1 ].map (str )+' , '+superior4_code_frame .T [2 ].map (str )+' , '+superior4_code_frame .T [3 ].map (str )#line:372
        elif superior4_code_frame .size ==3 :#line:373
            gtbfd =superior4_code_frame .T [0 ].map (str )+' , '+superior4_code_frame .T [1 ].map (str )+' , '+superior4_code_frame .T [2 ].map (str )#line:374
        elif superior4_code_frame .size ==2 :#line:375
            gtbfd =superior4_code_frame .T [0 ].map (str )+' , '+superior4_code_frame .T [1 ].map (str )#line:376
        else :#line:377
            sys .exit ()#line:378
        plt .subplots_adjust (bottom =0.25 )#line:380
        axcolor ='lightgoldenrodyellow'#line:381
        plt .subplot (221 )#line:383
        ax =plt .subplot (221 )#line:384
        ax .text (0.02 ,0.5 ,'PANDAS DATA 보고서',transform =ax .transAxes ,color ='black')#line:386
        ax .text (0.02 ,0.4 ,'업종:'+INDUSTRY ,transform =ax .transAxes ,color ='black')#line:388
        ax .text (0.02 ,0.3 ,PRODUCT ,transform =ax .transAxes ,color ='black')#line:390
        ax .text (0.02 ,0.2 ,BEGIN ,transform =ax .transAxes ,color ='black')#line:392
        ax .text (0.02 ,0.1 ,HOMEPAGE ,transform =ax .transAxes ,color ='black')#line:394
        ax .set_axis_off ()#line:395
        plt .subplot (222 )#line:397
        ax =plt .subplot (222 )#line:398
        ax .text (0.7 ,0.8 ,'PANDAS DATA',transform =ax .transAxes ,color ='gray',alpha =0.5 ,fontsize =12.5 )#line:400
        ax .text (0.02 ,0.5 ,'섹터 보고서',transform =ax .transAxes ,color ='black',wrap =True )#line:402
        ax .text (0.02 ,0.3 ,'섹터정보 : '+asdfdsa .values ,transform =ax .transAxes ,color ='black',wrap =True )#line:404
        ax .text (0.02 ,0.1 ,'동일섹터 종목정보 : '+gtbfd .values ,transform =ax .transAxes ,color ='black',wrap =True )#line:406
        ax .set_axis_off ()#line:407
        plt .subplot (223 )#line:409
        ax =plt .subplot (223 )#line:410
        plt .plot (high ,'bs',label ='세력동향(상)')#line:413
        plt .plot (low ,'g^',label ='세력동향(하)')#line:414
        bbox =dict (boxstyle ='round',color ='gray',alpha =0 )#line:419
        arrowprops =dict (facecolor ='black',shrink =0.5 )#line:420
        atmos =s .index .value_counts ().head (1 ).values /2 #line:421
        fillx =np .arange (0 ,atmos *1.2 ,1 )#line:422
        xy =(atmos *0.1 ,Q )#line:423
        ax .annotate ('%.f(종)'%(Q ),xy =xy ,bbox =bbox )#line:424
        ax .axhline (Q ,ls ='dotted',color ='r')#line:425
        ax .axhline (i .median (),ls ='--',color ='y')#line:426
        ax .axhline (i .max (),ls ='--',color ='b')#line:427
        ax .axhline (i .min (),ls ='--',color ='g')#line:428
        xy =(atmos *0.3 ,i .median ())#line:429
        zq =(atmos *0.5 ,i .max ())#line:430
        mn =(atmos *0.5 ,i .min ())#line:431
        op =(atmos *0.1 ,Q -t /3 )#line:432
        ax .annotate ('%.f(중)'%(i .median ()),xy =xy ,bbox =bbox )#line:433
        ax .annotate ('%.f(고)'%(i .max ()),xy =zq ,bbox =bbox )#line:434
        ax .annotate ('%.f(저)'%(i .min ()),xy =mn ,bbox =bbox )#line:435
        atmosname =s .index .value_counts ().head (1 ).index .values #line:438
        atmos2 =i .size /2 #line:439
        plt .xlim (0 ,atmos )#line:440
        plt .xticks ()#line:441
        plt .ylim (setylimdata3 .min ().values *0.9 ,setylimdata3 .max ().values *1.1 )#line:442
        plt .yticks (rotation =45 )#line:443
        ax .axvline (atmos2 ,color ='cornflowerblue',linestyle ='-',linewidth =5 )#line:444
        ax .fill_between (fillx ,i .median (),i .min (),color ='tab:brown',alpha =0.3 ,label ='매집구간: %.f'%(((i .median ()-Q )/(i .median ()-i .min ()))*100 ).round (1 ),interpolate =True )#line:446
        plt .legend ()#line:447
        plt .xlabel ('Data Size: %.f'%(stockoneyou2 .shape [0 ])+'/%.f'%(stockoneyou .shape [0 ]))#line:449
        plt .ylabel ('원',rotation =45 )#line:450
        plt .text (atmos *0.7 ,i .median (),'{0:.2}'.format (float (expectation *10 )))#line:451
        plt .text (atmos *0.87 ,i .max (),'{0:.2}'.format (float (expectation2 *10 )))#line:452
        plt .subplot (224 )#line:455
        ax =plt .subplot (224 )#line:456
        ax .text (0.88 ,0.01 ,today ,transform =ax .transAxes ,color ='black')#line:459
        df_KS200 =stock .get_index_ohlcv (widthe ,today ,'1028')#line:461
        df_KS200 ['Close']=df_KS200 ['종가']#line:462
        df_KS200_plot =(df_KS200 ['Close']/df_KS200 ['Close'].iloc [0 ])*chart ['Close'].head (1 ).values #line:463
        df_KS200_plot .name ='KOSPI200'#line:464
        try :#line:465
            chart ['Close'].name =stocksellection #line:466
        except NameError :#line:467
            print ("\n유튜브 '판다스데이타' 좋아요 와 구독 꾹 ! (^^*)")#line:468
            pandasdataurl ="https://www.youtube.com/channel/UCCau8sE6Fiu20Z_1Y_4l0eA"#line:469
            chromedir ="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"#line:470
            new =2 #line:471
            webbrowser .get (chromedir ).open (pandasdataurl ,new =new )#line:472
        NEW_plot =pd .concat ([chart ['Close'],df_KS200_plot ],axis =1 )#line:473
        plt .plot (chart ['Close'],linewidth =4.5 ,label =chart ['Close'].name +'('+CODE +')')#line:475
        plt .plot (df_KS200_plot ,linewidth =4.5 ,label =df_KS200_plot .name )#line:476
        rate =(chart ['Close'].tail (1 ).values -chart ['Close'].head (1 ).values )/(NEW_plot ['KOSPI200'].tail (1 ).values -NEW_plot ['KOSPI200'].head (1 ).values )#line:477
        plt .ylim (setylimdata3 .min ().values *0.9 ,setylimdata3 .max ().values *1.1 )#line:478
        try :#line:479
            plt .fill_between (chart ['Close'].index ,chart ['Close'].values ,NEW_plot ['KOSPI200'].values ,where =(chart ['Close'].values >NEW_plot ['KOSPI200'].values ),color ='C0',alpha =0.3 ,label ='α',interpolate =True )#line:481
        except ValueError :#line:482
            print ("◇차트 안내◇\n해당종목의 경우 상장일로부터 1년이 경과하지 아니하여, α 는 표기되지 않음을 참조하여 주세요.")#line:483
        plt .axhline (i .median (),ls ='--',color ='y')#line:484
        plt .axhline (Q ,ls ='dotted',color ='r')#line:485
        plt .axhline (i .max (),ls ='--',color ='b')#line:486
        plt .axhline (i .min (),ls ='--',color ='g')#line:487
        plt .legend ()#line:490
        plt .xticks (rotation =45 )#line:492
        plt .text (chart ['Close'].idxmax (),chart ['Close'].max (),'%.f(고)'%(chart ['Close'].max ()))#line:493
        if chart ['Close'].max ()*1.3 <i .max ():#line:494
            plt .text (widthe ,i .max (),'◇투자유의!\n최근 권리락,배당락 여부를 확인하여 주세요!◇')#line:495
        plt .text (chart ['Close'].idxmin (),chart ['Close'].min (),'%.f(저)'%(chart ['Close'].min ()))#line:496
        bbox =dict (boxstyle ='round',fc ='0.9')#line:497
        axfreq =plt .axes ([0.25 ,0.1 ,0.65 ,0.03 ],facecolor =axcolor )#line:500
        axamp =plt .axes ([0.25 ,0.05 ,0.65 ,0.03 ],facecolor =axcolor )#line:501
        sfreq =Slider (axfreq ,'Portion',1.0 ,2.0 ,valinit =portion )#line:502
        samp =Slider (axamp ,'days',1 ,730 ,valinit =daydays )#line:503
        def update (O0O0O00O0O0OOO000 ):#line:505
            OOOO0O0O00O0000OO =samp .val #line:506
            O00O0OO00OO00OO00 =sfreq .val #line:507
        sfreq .on_changed (update )#line:509
        samp .on_changed (update )#line:510
        plt .show ()#line:512
        portion =sfreq .val #line:515
        daydays =int (samp .val )#line:516
        if portion <=1.0 :#line:518
            break #line:519
