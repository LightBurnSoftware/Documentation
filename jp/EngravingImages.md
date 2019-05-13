[Return to main page](README.md)

----

# イメージの彫刻

[Supported Image Files](#supported)

[Engraving Configuration](#configuration)

-----

![Engraving Image](img/EngravingImage.PNG)

LightBurnでは画像を彫刻することが出来ます

<a name="supported"></a>
## サポートする拡張子

* bmp (Bitmap)
* jpg、jpeg (Joint Photographic Exports Group)
* png (Portable Network Graphics) 
* gif (Graphics Interchange Format)
* tga (Truevision)

<a name="configuration"></a>
## 彫刻設定

カットウィンドウの中のレイヤーをダブルクリックするとカット設定エディターが立ち上がります。

![Engraving Options](/img/EngravingOptions.PNG)

### Speed

こちらをご確認ください [Speed](/Operations.md#speed) 

### 最大パワー

漆黒を彫る際の最大パワー。この値を小さくすると、黒を彫る際の出力が弱くなります。 



***TODO: Reword the next section***

*最大パワーの注意:* もしイメージの中に漆黒がない場合、最大値で出力することはありません。 

### モード

ラスタ画像では使えません。

### 双方向スキャン

こちらをご確認ください [Bi-Directional Scanning](/Operations.md#bidirectional) 

### ネガティブイメージ

明るい部分を暗い部分を反転させてます

### オーバースキャン

こちらをご確認ください [Overscanning](/Operations.md#overscanning) 

### Line Interval

こちらをご確認ください [Line Interval](/Operations.md#lineinterval) 

### スキャン角度

こちらをご確認ください [Scan Angle](/Operations.md#scanangle) 

### 1インチあたりの線数

出力の線量を調整します - 1インチ内でどれだけ線数で彫刻するかを決定します。

### イメージモード

モードを変えることによって彫刻するアルゴリズムを変更します

オリジナル画像 (Madrid truck):

![MadridTruck-Original](img/MadridTruck-Original.png)

しきい値:

![MadridTruck-Threshold](img/MadridTruck-Threshold.png)

オーダード:

![MadridTruck-Ordered](img/MadridTruck-Ordered.png)

ディザ:

![MadridTruck-Dithered](img/MadridTruck-Dithered.png)



#### ディザでの限界

Dithering is attempting to use 2 colors (black and white) to approximate continuous shading, and it has its limits. Diffusion dithering works by remembering how "off" a given pixel was, and smearing (diffusing) that difference around over neighboring pixels. When those neighbors are computed, that error amount is factored in. If you have an image with large areas of solid black or white, there's nowhere for this error amount to get absorbed (black and white are always exact), so it keeps pushing it further and further, and you sometimes end up with strange lines or tendrils in your picture. Ordered dithering does not have this issue, so it works better for "solid filled" images, like cartoons or logos.

LightBurnのアイコンをDiffusionとOrderedでディザリングした結果です

![Logo-DithersCompared](img/Logo-DithersCompared.png)

### パスの数

彫刻の周回を行う回数

