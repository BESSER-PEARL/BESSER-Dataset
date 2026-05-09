





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Dimension  {

    private float extwidth;
    private float extoffset;
    private float width;
    private float x3;
    private float extlength;
    private boolean visible;
    private int textratio;
    private float x1;
    private String dtype;
    private int precision;
    private float textsize;
    private float y1;
    private float x2;
    private float y2;
    private int layer;
    private float y3;
    private String unit;





    private eaglemodel_Plain eaglemodel_plain;




    private eaglemodel_Package eaglemodel_package;


    public eaglemodel_Dimension(
        float extwidth,        float extoffset,        float width,        float x3,        float extlength,        boolean visible,        int textratio,        float x1,        String dtype,        int precision,        float textsize,        float y1,        float x2,        float y2,        int layer,        float y3,        String unit    ) {
        this.extwidth = extwidth;
        this.extoffset = extoffset;
        this.width = width;
        this.x3 = x3;
        this.extlength = extlength;
        this.visible = visible;
        this.textratio = textratio;
        this.x1 = x1;
        this.dtype = dtype;
        this.precision = precision;
        this.textsize = textsize;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
        this.layer = layer;
        this.y3 = y3;
        this.unit = unit;
    }


    public float getExtwidth() {
        return extwidth;
    }

    public void setExtwidth(float extwidth) {
        this.extwidth = extwidth;
    }
    public float getExtoffset() {
        return extoffset;
    }

    public void setExtoffset(float extoffset) {
        this.extoffset = extoffset;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getX3() {
        return x3;
    }

    public void setX3(float x3) {
        this.x3 = x3;
    }
    public float getExtlength() {
        return extlength;
    }

    public void setExtlength(float extlength) {
        this.extlength = extlength;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public int getTextratio() {
        return textratio;
    }

    public void setTextratio(int textratio) {
        this.textratio = textratio;
    }
    public float getX1() {
        return x1;
    }

    public void setX1(float x1) {
        this.x1 = x1;
    }
    public String getDtype() {
        return dtype;
    }

    public void setDtype(String dtype) {
        this.dtype = dtype;
    }
    public int getPrecision() {
        return precision;
    }

    public void setPrecision(int precision) {
        this.precision = precision;
    }
    public float getTextsize() {
        return textsize;
    }

    public void setTextsize(float textsize) {
        this.textsize = textsize;
    }
    public float getY1() {
        return y1;
    }

    public void setY1(float y1) {
        this.y1 = y1;
    }
    public float getX2() {
        return x2;
    }

    public void setX2(float x2) {
        this.x2 = x2;
    }
    public float getY2() {
        return y2;
    }

    public void setY2(float y2) {
        this.y2 = y2;
    }
    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }
    public float getY3() {
        return y3;
    }

    public void setY3(float y3) {
        this.y3 = y3;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public eaglemodel_Plain getEaglemodel_plain() {
        return eaglemodel_plain;
    }

    public void setEaglemodel_plain(eaglemodel_Plain eaglemodel_plain) {
        this.eaglemodel_plain = eaglemodel_plain;
    }
    public eaglemodel_Package getEaglemodel_package() {
        return eaglemodel_package;
    }

    public void setEaglemodel_package(eaglemodel_Package eaglemodel_package) {
        this.eaglemodel_package = eaglemodel_package;
    }

}