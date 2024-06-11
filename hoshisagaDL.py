import webbrowser

'''
実行の前に以下を済ませること
・既定のブラウザ設定（GoogleChrome推奨）
・http://hoshisaga.jp/のサイト設定から安全でないコンテンツを許可に変更
'''

num = int(input('星探のシリーズ番号(半角数字)'))
stg = int(input('ステージ総数(半角数字)'))

main = input('メインをダウンロードしますか(y/n)')
if (main == 'y'):
    url = 'http://hoshisaga.jp/hoshi' + str(num) + '/main.swf'
    webbrowser.open(url, new=0, autoraise=True)

for i in range(stg):
    url = 'http://hoshisaga.jp/hoshi' + str(num) + '/stg' + str(i+1) + '.swf'
    webbrowser.open(url, new=0, autoraise=True)
