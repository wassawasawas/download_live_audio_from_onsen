Download a live audio from Onsen.ag Radio
===
Recently, onsen.ag has been changed streaming method.
So far, Changed from serveing static content to Amazon CloudFront media streaming(HLS format).
This script grab from a live audio source and convert a mp3 using ffmpeg.

## Prerequisites
* python 3.8
  * requests
* ffmpeg

## Specify the save data directory and installed ffmpeg path
```
DATA_DIR = '/var/data/mp3' # If not set, save a file in current directory.
ffmpeg_command_path = '/opt/ffmpeg/ffmpeg'
```

## Usage
About directory_name, Please select from the Streaming ID list below.
```
usage: download_live_audio_from_onsen.py [-h] [-i ID]

optional arguments:
  -h, --help      show this help message and exit
  -i ID, --ID ID  Set a directory_name you want.
```

Seeing outlog like this.
```
$ python download_live_audio_from_onsen.py -i shigohaji
[INFO]: Starting Download
{
    "id": 4,
    "directory_name": "shigohaji",
    "delivery_interval": "隔週月曜日配信",
    "title": "高橋李依・上田麗奈 仕事で会えないからラジオはじめました。",
    "chapter": "第79回",
    "delivery_date": "8/10"
}
[INFO] Successfully Downloaded

$ ls -la
-rw-r--r-- 1 XXX XXX 27689213 Aug 12 15:07 '高橋李依・上田麗奈 仕事で会えないからラジオはじめました。_第79回_20200810.mp3'
```

## Crontab
If you want to collect regularly, please register crontab.
```
sample)
0 18 * * 1 test $(expr $(date '+\%W') \% 2 ) -eq 0 && /{Python path}/python /{script path}/download_onsen_hsl.py -i shigohaji
0 18 * * 2 test $(expr $(date '+\%W') \% 2 ) -eq 0 && /{Python path}/python /{script path}/download_onsen_hsl.py -i who
0 0 22-28 * * [ "$(date '+\%w')" -eq 2 ] && /{Python path}/python /{script path}/download_onsen_hsl.py -i omimi
0 0 22-28 * * [ "$(date '+\%w')" -eq 1 ] && /{Python path}/python /{script path}/download_onsen_hsl.py -i rezero
0 18 * * 3 test $(expr $(date '+\%W') \% 2 ) -eq 1 && /{Python path}/python /{script path}/download_onsen_hsl.py -i yuukiyui

```

---
## Streaming ID list as of Aug 12th, 2020

|  directory_name  |  Streaming Title  |
| ---- | ---- |
| grepre | GREAT PRETENDER ～詐欺師の宴～ |
| kumagami | くまがみ珈琲店～プレミアムブレンド～ |
| shigohaji | 高橋李依・上田麗奈 仕事で会えないからラジオはじめました。 |
| gashitai | 風音と桜川未央と桃井いちごの女子会ノリでラジオがしたい！ |
| ippo | 釘宮理恵のいつだって、はじめのいっぽ |
| yuukiyui | ゆうきとゆいのラジオで２人暮らし♡ |
| kanryo | 木村良平の感度は良好！ |
| ishimigaki | 石谷春貴、ラジオで磨く。 |
| matuokasan | 松岡ハンバーグ |
| aya-uchida | 内田彩の今夜一献傾けて |
| fujita | 藤田茜シーズン1 |
| tsbase | 立花ベース in 初台 |
| tsudaken | 普通に津田健次郎 |
| marika | 高野麻里佳のスーパーマリカクラブ |
| gurepap | 鷲崎健・藤田茜のグレパラジオP |
| mikizirushi | 三木眞一郎の三木印 |
| oshitai | 瀬戸麻沙美と日高里菜のお（を）したい！ |
| tane | Salon de Tanedaへようこそ♪ |
| henshindanshi | 汐谷・浦尾の変身☆男子 |
| shizakura | 清桜～ラジオはじめました～ |
| sasamori | ゆうときょうかの「あつまれ！ささもり！」 |
| maoh | 魔王学院の不適合者　～史上最強の魔王の始祖、転生して子孫たちのラジオに出る～ |
| matsui | 松井恵理子のにじらじっ！ |
| nkm | のむこがみなみ |
| togari | 相坂優歌と前田玲奈のトガリズム２ |
| who | だれ？らじ |
| gugl | 6-シックス-のゲラゲラジオ |
| tsukinone | 大原さやか朗読ラジオ　月の音色～radio for your pleasure tomorrow～ |
| battle | 佐藤日向・小泉萌香のバトってダイナソー☆ |
| aina | 鈴木愛奈のring A radio |
| mogucomi | ゆみりと愛奈のモグモグ・コミュニケーションズ |
| kamihime | 民安ともえ と 青葉りんごの神プロRADIO |
| uzakichan | 宇崎ちゃんは遊びたい！　SUGOI RADIO ～先輩が可愛そうなんで一緒に喋ってあげるッス！～ |
| saisuki | 村上奈津実・伊藤彩沙　最近、好きになりました |
| kotopan | 吉岡茉祐と山下七海の ことだま☆パンケーキ |
| jks | 会沢紗弥と花井美春の「まったく、女子高生は最高だぜ！！」 |
| frasta | 笠間淳・梶原岳人のふらっと紀行！ ～…え？スタジオからは出られないんですか？～ |
| gochiusabloom | ご注文はラジオですか？BLOOM |
| teibo | 放課後ていぼうラジオ |
| tomoradi | 楠木ともりのともりるきゃんどる |
| ai | ファイルーズあいの“愛”・ルーズ・Fight！ |
| survey | 富田美憂・前田佳織里の“調査のご依頼、お待ちしてます！” |
| yurucamp | らじキャン△～ゆるキャン△情報局～ |
| coral | 稗田寧々 鈴代紗弓のコーラルマイク |
| railgun_t | とあるラジオの超電磁砲Ｔ　常盤台放送部 |
| cheerkyubu | Cheer球部！全校応援ラジオ　ちあたま、さくよ！🌸 |
| koihime | 風音と遥そらの恋姫らじお |
| festa | ComicFesta Radio　ユステイル種族集会 |
| gridman | アニメGRIDMAN ラジオ とりあえずUNION |
| shachibato | 社長、ラジオの時間です！シャチラジ！ |
| mon_isha | モンスター娘のお医者さんスペシャルラジオ　グレンとサーフェ、ドキドキ診療中！ |
| plunderer | プランダラジオ |
| ongeki | オンゲキ ～ドはオンゲキのド スペシャル～ |
| koitate | 恋する乙女と守護の楯 Re:boot The "SHIELD-9"～アイギスラジオ～ |
| oda-shinamon | 群雄割局！ 織田シナモン信長ワンだふるラジ尾 |
| ore-ski | 俺たちを好きなのはリスナーだけかよ |
| gugl_kiku | 菊一文字のヤングタウンEX |
| toriradi | 広瀬裕也と宮本侑芽のとりあえずRADIO |
| frb | ファンタジア・リビルド　エンデと理乃の「愛した世界を紡ぐラジオ」 |
| rezero | Re：ゼロから始める異世界ラジオ生活 |
| tate | 普通にラジオをお届けしたいラフタリアとフィーロ |
| dosukoi | Summer Pockets Radio～鳴瀬家の食卓 ～ |
| miabyss | ラジオインアビス ～リコとレグとナナチの探窟ラジオ |
| nonpetit | MoeMiののんびりプティフール |
| rezelos | Re:ゼロから始める異世界生活 Lost in Memories　～ルグニカ王国伝令局～　リゼロス通信 |
| llss | ラブライブ！サンシャイン!! Aqours浦の星女学院RADIO!!! |
| moa | 美少女ゲームMUSIC ON AIR! |
| dialogue | DIALOGUE＋ONLINE |
| friend | 天﨑滉平・大塚剛央の「僕たちもう、フレンドですよね？」 |
| toshitai | セブン-イレブン presents 佐倉としたい大西 |
| kakazu | かかずゆみの超輝け！やまと魂！！ |
| cr | チェンクロ公式WEBラジオ「ちぇんらじ」 |
| kamo | 名塚佳織のかもさん學園 |
| mnh | HELIOS Rising Heroes ラジオ マンデーナイトヒーロー |
| azusta | アズレン すて～しょん♪ |
| watahana | PsyChe（プシュケ）の私花。らじお! |
| lnaf | 連盟空軍広報局公式放送　LNAF.OA.ラジオワールドウィッチーズ |
| ff | 南條愛乃・エオルゼアより愛をこめて |
| fate-sndigest | 劇場版「Fate/stay night [Heaven's Feel]～もし、わたしがラジオをやったら、許せませんか？～Ⅲ ダイジェスト |
| bullet | デート・ア・バレット ラジオ　時崎狂三の時間 |
| sukebe | 羽多野渉・佐藤拓也のScat Babys Show！！ |
| fate-sn | 劇場版「Fate/stay night [Heaven's Feel]～もし、わたしがラジオをやったら、許せませんか？～Ⅲ |
| hanayume | 花とゆめ　男子会!?らじお |
| hxeros | -NEWS- ド級編隊エグゼロス |
| zzradio | 千田と日笠のゾイドワイルド ZEROラジオ |
| gurepa | 鷲崎健・藤田茜のグレパラジオ |
| appare | 「天晴爛漫！」Radio Here we go!!!!! |
| otomain | オトメ＊ドメイン　RADIO＊MAIDEN |
| project_red | レッドプライドオブエデンプレゼンツ『エデン大陸放送局』！ |
| mimikaki | 耳かきマッドサイエンティスト伊ヶ崎がダミヘで世界征服を目論むラジオ |
| dolls | 東京ドールズRADIO！―国土調査院放送局― |
| mahouritsu | ムヒョとロージーの魔法律相談事務所　～ムヒョロジラジオ～ |
| kokuradio | 告RADIO 2020 |
| vac | ラジオ　VOICE ACTRESS CONCERTO! |
| yyyi | ラジオ「結城友奈は勇者である 花結いのきらめき」勇者部活動報告 |
| onsenking | 音泉キング「下野紘」のラジオ きみはもちろん、＜音泉＞ファミリーだよね？ |
| radista | あんさんぶるスターズ！！『ALKALOID』&『Crazy:B』のラジオスクエア！！ |
| iine | 天津向のためになるらじお |
| nashiradio | はくばく Presents 高森奈津美・三澤紗千香の山梨応援ラジオ |
| kimetsu | TVアニメ「鬼滅の刃」公式WEBラジオ　鬼滅ラヂヲ |
| stb | ストブらじお 雪菜と凪沙のおとなり放送局 |
| omimi | イヤホンズの三平方の定理 |
| ntrj | ネットという無数の声雄が割拠する世界から、最新最強の武器バイノーラルマイクを駆使し、ファンのみんなに癒しと感動を与える声優を、とにかく！全力を尽くして熱く応援するラジオ |
| anime | 檜山修之のあにめじ湯 |
| rst | Re:ステージ！Chain of RADIO |
| bakumatsu | 恋愛幕末カレシ～時の彼方で花咲く恋～WEBラジオ「イキザマラジオ恋」 |
| hanadi | 檜山修之とやまけんのただ座して噺すのみ！ラヂオ。 |
| euphonium | 響け！ユーフォラジオ |
| rst2 | Re:ステージ！Chain of TV |
| tojinomiko | 本渡楓のとじらじ！ |
| sega_girls | セガ ガールズ通信　広報宣伝ラジオ |
| heroaca_amn | 僕のヒーローアカデミア　ラジオ　オールマイトニッポン |
| mhr3 | モンハンラジオ 良三の部屋 |
| same | ガールズ＆パンツァーRADIO　サメさんチーム、よーそろー！ |
| lump | Lump of Sugar放送部