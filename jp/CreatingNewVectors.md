[Return to main page](README.md)

----

# LightBurnでVectorを作る

LightBurnには基本的な形を作成することに出来るツールが備わっています。これらはToolメニューもしくは画面左側にあるツールバーから利用することが出来ます。

## 基本的な形の作成

### Pen Tool ![Pen Tool Icon](/img/PenTool.PNG) 
[Video Tutorial #2: Pen Tool](https://www.youtube.com/watch?v=uzFsrUwONbw#t=6m26s)

* ラインを引くことが出来ます。
* ラインは自動的にすでに描かれている形の頂点や真ん中にスナップします
* スナップしたくない時はCtrl (![Command icon](/img/key-command-16.png)on Mac)を押しながらラインを引いてください

### 四角と円形 ![Rectangle Tool Icon](img/RectangleTool.PNG) ![Ellipse Tool Icon](/img/EllipseTool.PNG)
[Video Tutorial #2: Rectangle and Ellipse](https://www.youtube.com/watch?v=uzFsrUwONbw#t=8m38s)

* 四角と円形を描くことが出来ます
* Shiftを押しながら描くと正方形や正円を描くことが出来ます
* Ctrl (![Command icon](/img/key-command-16.png)on Mac)を押しながら描くと中心部から描かれます

#### 角の丸い四角を描く
角を丸くしたい四角を選択してツールボックスからウィンドウ -> Shape Propertiesを選んでShape Propertiesウィンドウを開きます。その中のCorner Radiousを変更すると角を丸くすることが出来ます。

### ポリゴンツール ![Polygon Tool](img/PolygonTool.png)

ポリゴンツールで描いた図形は、多面体に変更することが出来ます。ポリゴンツールで描いた画像を選択して、Shape Propertiesを開きます。Sidesの中に希望の数字を入力するとその数の面の図形に変形します。

![PolygonSides](/img/PolygonSides.png)




### ノード編集ツール ![Node Tool Icon](/img/NodeTool.PNG)

[Video Tutorial #2: Node Editing](https://www.youtube.com/watch?v=uzFsrUwONbw#t=9m15s)

* 選択した図形の点を動かすことが出来ます
* Sキーを押しながら点の上にカーソルを持っていくと、滑らかな曲線に変わります。変形用のラインも引かれるので、それを使って曲線を変えることも出来ます。
* Sキーを押しながらラインの上にカーソルと持っていくと、ラインを曲線に変えることの出来る点が現れ、それを引っ張ることで曲線に変形できます。
* Lキーを押しながら曲線の上にカーソルと持っていくと、元の直線に戻します。
* Cキーを押しながら点の上にカーソルと持っていくとコーナーに変更して、両辺を独立して操作出来るようになります。
* Dキーを押しながら点の上にカーソルと持っていくと、その点を削除して両端に繋がっている点を繋げます。
* Dキーを押しながらラインの上にカーソルと持っていくと、ラインを削除してそのままか図形を割ります。 
* Iキーを押しながらラインか曲線の上にカーソルと持っていくと、新しい点を挿入します。

### テキストツール ![Text Tool Icon](/img/TextTool.PNG)
[Video Tutorial #2: Text Tool](https://www.youtube.com/watch?v=uzFsrUwONbw#t=9m45s)

* 新たにテキストを作成したり、既存のテキストを編集出来ます
* フォントやフォントサイズを変更出来ます
* アライメントを変更出来ます (左揃え, 右揃え, 上揃え, 下揃え, 中央揃え).

## オフセットツール ![Offset Tool Icon](/img/OffsetTool.PNG)

[Video Tutorial #2: Offset Tool](https://www.youtube.com/watch?v=uzFsrUwONbw#t=10m49s)

![Offset Dialog](/img/OffsetDialog.png)



* 選択した図形の周りにオフセットラインを作成します
* オフセットの距離を増減することが出来ます
* 角のスタイルをラウンド、ベベル、コーナーから選択出来ます
* オプションとして元のオブジェクトの削除、結果オブジェクトの選択、結果を最適化/簡略化があります
* 残った形状は自動的にグループ化されます
* 不必要な部分はグループ化を解いて削除出来ます
* 残った形状は自動的にスプラインに変換出来ます
* 元の図形を自動消去することも出来ます
* Ctrlキー (![Command icon](/img/key-command-16.png)on Mac) を押しながらオフセットボタンを押すと最後に行ったオプションを実行します
* オフセットはオープンベクターや閉じた図形にも使えます

## ブーリエンオプション

ベクターで作成した図形は [Boolean Tools](Boolean.md)で変更することが出来ます

## テキスト自動接続
スクリプトフォントを使っている場合、Lightburnは自動的に文字を接続させます
