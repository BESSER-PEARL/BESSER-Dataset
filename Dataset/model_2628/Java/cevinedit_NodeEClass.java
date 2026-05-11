





import java.util.List;
import java.util.ArrayList;

public class cevinedit_NodeEClass extends PersonalizedElement {

    private String labelFontStyle;
    private int borderWidth;
    private String borderTexture;
    private String size;
    private String label;
    private String listPointsPolygon;
    private String backgroundColor;
    private String labelPlacement;
    private boolean resizable;
    private String brightness;
    private String borderColor;
    private String imagePath;
    private String figure;



    public cevinedit_NodeEClass(
        String labelFontStyle,        int borderWidth,        String borderTexture,        String size,        String label,        String listPointsPolygon,        String backgroundColor,        String labelPlacement,        boolean resizable,        String brightness,        String borderColor,        String imagePath,        String figure    ) {
        super(
        );
        this.labelFontStyle = labelFontStyle;
        this.borderWidth = borderWidth;
        this.borderTexture = borderTexture;
        this.size = size;
        this.label = label;
        this.listPointsPolygon = listPointsPolygon;
        this.backgroundColor = backgroundColor;
        this.labelPlacement = labelPlacement;
        this.resizable = resizable;
        this.brightness = brightness;
        this.borderColor = borderColor;
        this.imagePath = imagePath;
        this.figure = figure;
    }


    public String getLabelfontstyle() {
        return labelFontStyle;
    }

    public void setLabelfontstyle(String labelFontStyle) {
        this.labelFontStyle = labelFontStyle;
    }
    public int getBorderwidth() {
        return borderWidth;
    }

    public void setBorderwidth(int borderWidth) {
        this.borderWidth = borderWidth;
    }
    public String getBordertexture() {
        return borderTexture;
    }

    public void setBordertexture(String borderTexture) {
        this.borderTexture = borderTexture;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getListpointspolygon() {
        return listPointsPolygon;
    }

    public void setListpointspolygon(String listPointsPolygon) {
        this.listPointsPolygon = listPointsPolygon;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getLabelplacement() {
        return labelPlacement;
    }

    public void setLabelplacement(String labelPlacement) {
        this.labelPlacement = labelPlacement;
    }
    public boolean getResizable() {
        return resizable;
    }

    public void setResizable(boolean resizable) {
        this.resizable = resizable;
    }
    public String getBrightness() {
        return brightness;
    }

    public void setBrightness(String brightness) {
        this.brightness = brightness;
    }
    public String getBordercolor() {
        return borderColor;
    }

    public void setBordercolor(String borderColor) {
        this.borderColor = borderColor;
    }
    public String getImagepath() {
        return imagePath;
    }

    public void setImagepath(String imagePath) {
        this.imagePath = imagePath;
    }
    public String getFigure() {
        return figure;
    }

    public void setFigure(String figure) {
        this.figure = figure;
    }


}