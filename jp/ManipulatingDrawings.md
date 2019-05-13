[Return to main page](README.md)

----

# 描写の調整

#### スケーリングとサイジング

##### スケールとサイズを理解する

ツールバーとドラグではスケールを調整。Shape Propertiesではサイズを調整します。 これは理解しにくいですが需要なポイントです。

例を見てみましょう

![Size vs Scale](/img/Size-Vs-Scale.png)

ダイヤの形が今回の例には最適な形状です。上部のツールバーの値とShape Propertiesの値が異なっています。このダイヤは50 x 50ですが、フットプリントでは 70 x 70になっています。もしツールバーやドラグで調整するとリサイズしたように見せますが、実際には伸縮をしているだけです。本当のダイヤモンド50 x 50です。 

corner radiusを設定する際にはこれは非常に重要です。ツールバーやドラグで調整すると、元々設定したcorner radiusでは描写されません。正しい値を残すにはShape Propertiesで調整してください。



##### ドラグでスケールを変更する

描写を選択すると8つのポイントが表示されます。この点をクリックしてドラグするとサイズを調整できます。サイズを変更するとツールバーの値も変更します。 

![Scale with Drag Handles](/img/Scale-Drag-Handles.png)

##### ツールバーでスケールを変更する

描写を選択してからツールバーに値を入れると、正確なサイズの調整をすることが出来ます。

![Toolbar Width Height](/img/Scale-Width-Height.png)

##### Shape Propertiesでリサイズする

Shape Propertiesではリサイズを行えます(スケーリングとは異なる) これを利用するとcorner radiusの値は変更さません。

![Scale Shape Properties](/img/Scale-Shape-Properties.PNG)

-----------

#### 回転

##### ツールバーで回転

描写を選択してRotateに回転させてい角度を入力する

![Rotate Toolbar](img/Rotate-Toolbar.png)

##### ドラグで回転

ポイントを掴んで回転させることが出来ます

![Rotate Drag Handles](img/Rotate-Drag-Handle.png)

-------------------

#### Corner Radius

##### Shape Properties

Shape Propertiesのcorner radiusで設定出来ます。widthとheightに合わせて形が変更されます。ツールバーやドラグでイメージのスケールを変えると、角の形もそれに応じて変更されます。当初の値を残すにはShape Propertiesでサイズを変更してください。

![Corner Radius](/img/Corner-Radius.png)

---------------

#### Placement

##### ツールバー

対象物を素早く指定の場所に置くことが出来ます。移動したいイメージを選択後にツールバーから移動のアイコンを選んで指定の場所を選んでください。

![Image Placement](/img/Image-Placement.png)

