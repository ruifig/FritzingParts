# FritzingParts

My custom Fritzing parts.
I use these just for Breadboard views so it makes it easier to design my projects. They are NOT fully functional/correct Fritzing parts.


# SVG files

To edit the SVG files, I use Inkscape (https://inkscape.org/).

Fritzing only accepts a limited number of fonts in the SVG file, so install these fonts in `3rdparty\fontsandtemplates.zip`

## Inkscape extension

I had some troubles getting those showing up correctly on Fritzing, especially test.
To solve that, I hacked a little Inkscape extension that converts everything to paths and saves as another file with the suffix `_fritzing`.
The extension is in the folder `com.crazygaze.inkscape.fritzing_export`, and the entire folder itself should be copied to `C:\Users\<USER>\AppData\Roaming\inkscape\extensions\`


# Random notes

* If a custom part shows up as red in the breadboard, it probably means not all the connectors are mapped in the parts editor.


