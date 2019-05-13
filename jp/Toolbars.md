[Return to main page](README.md)

----

<a name="Top"></a>
## ツールバーとツールウィンドウ

簡単にデータの編集が出来るようたくさんのツールバーとウィンドウをご用意しています。トップバーで右クリックするかメニューからウィンドウを選ぶとリストが表示されます。

![Toolbars](/img/Toolbars.PNG)



### ツールウィンドウとタブ

ツールウィンドウはドラグして動かすことが出来ます。縮小/最大ボタンでも独立させることが出来ます。

ドラグして右側に戻すと元に戻せます。

他のウィンドウの上に落とすと、タブとして追加されます。

Xボタンを押すかと閉じることが出来ます。

タブは掴んで動かすと順番を変更出来ます。

[Return to Top](#Top)

#### ツールウィンドウでは多くのツール機能があります

* [Cuts](#cuts)
* [File List](#filelist)
* [Laser](#laser)
* [Move](#move)
* [Shape Properties](#shapeproperties)
* [Console](#console)  

#### ツールバーはツールウィンドウに似ていますが、アイコンでまとめられています。

* [Tools](#Tools)
* [Arrange](#Arrange)
* [Numeric Edits](#Numeric)
* [Text Edits](#Text)

[Return to Top](#Top)

<a name="cuts"></a>
### カット

カットツールでは大抵のジョブを設定出来ます。レイヤのカットの順序やマシンの設定があります。詳細はこちらをご参照ください[Operations](Operations.md)

![Cut Tool WIndow](/img/CutsToolBox.PNG)

* レイヤの上で右クリックをすると対象が点滅します
* ダブルクリックをすると、レイヤのフル設定画面が出ます
* モード、Output、出力のオプションを変更出来ます
* カット情報で基本的なパラメーターの設定が出来ます
* 右の上下の矢印で選択しているレイヤーの優先度を変更出来ます。

[Return to Top](#Top)

<a name="filelist"></a>
### File List

Ruidaコントローラーのみに対応

![FileListWindow](/img/FileListWindow.png)

Refreshボタンを押してホストファイルに追加します。ファイルを選択してStartを押してカットを開始します。Deleteを押すと削除、Downloadで保存が出来ます。Uploadでファイルを選んでアップロード出来ます。全てのファイルを削除するボタンに気をつけてください。

[Return to Top](#Top)

<a name="laser"></a>
### レーザー



![Laser Tool Window](/img/LaserToolBox.PNG)

レーザーの設定を行います。詳しくは対象の説明をご参照ください。

*開始場所*についてはこちらをご確認ください[Coordinates and Origin](CoordinatesOrigin.md)

[Return to Top](#Top)

<a name="move"></a>
### Move

Moveのツールウィンドウは主にJobとホーム機能用です

![Move Tool Window](/img/MoveToolBox.PNG)

矢印でレーザーヘッドを動かせ、レーザーのスピードやパワーを入力することが出来ます。 

自分で原点を設定することも出来ます。

[Return to Top](#Top)

<a name="shapeproperties"></a>
### Shape Properties

Shape propertiesでは同じレイヤ上の異なるシェープにそれぞれのシェープ用の出力値を設定することが出来ます。これはテストパターンを作成する時などに便利です。 [LightBurn progress demo #9 - Power Scaling](https://www.youtube.com/watch?v=ZiUAOv4tAGY) 
またどちらの方向にカットするかも設定出来ます。

![Shape Properties Tool Window](/img/ShapePropertiesToolBox.PNG)

[Return to Top](#Top)

<a name="console"></a>
### Console

Ruidaマシン以外ではコンソールが利用出来ます。コマンドを直接入力して作業が可能です。 
Ruidaを含めいくつか利用になれない機器があります。

![Console Tool Window](/img/ConsoleToolBox.PNG)

[Return to Top](#Top)

<a name="workspace"></a>
## メインツールバー


LightBurnのX & Y position, width, height, scale, interval entry boxesでは計算式にたいおうしています。

mmモードで1/2inとタイプすると12.7になります。ft, cm, in, mmや基本的な数式やカッコにも対応しています。(1/2in + 3mm) * 2.5 + 1ftといった入力が可能です。1/300inとinterval boxに入力すると"300 lines per inch"に変換します。

[Return to Top](#Top)

<a name="Tools"></a>
## ツール ツールバー

左側に位置するツール用ツールバーではアイコンを使って入力をすぐに変更出来ます:

### 選択

ワークスペースの形状を選択したり、メニューやツールバーにアクセス出来ます。

### 線を描写

ラインを引きます。
"Ctrl + L"

### 四角形ツール

四角形を作成します。
"Ctrl + R"

### 楕円ツール

楕円を作成します
"Ctrl + E"

### ノードを編集

ノードの編集を行います。
"Ctrl + ~"

### テキストを編集

テキストを編集します。
"Ctrl + T"

### レーザーポジション
レーザーをクリックした場所に移動します
### オフセット形状

オフセットを利用した新しい形状を作成します。

[Return to Top](#Top)

<a name="Arrange"></a>
## 調整ツールバー

[Return to Top](#Top)

<a name="Numeric"></a>

## 数字編集ツールバー

[Return to Top](#Top)

<a name="Text"></a>

## テキストオプションツールバー

You can select the font, size, and also Bold or Italic options here.


[Return to Top](#Top)


