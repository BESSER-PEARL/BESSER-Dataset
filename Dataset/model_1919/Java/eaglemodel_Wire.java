





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Wire  {

    private float y2;
    private float x2;
    private String extent;
    private int layer;
    private String cap;
    private float x1;
    private float curve;
    private float width;
    private float y1;
    private String style;





    private eaglemodel_Plain eaglemodel_plain;




    private eaglemodel_Package eaglemodel_package;


    public eaglemodel_Wire(
        float y2,        float x2,        String extent,        int layer,        String cap,        float x1,        float curve,        float width,        float y1,        String style    ) {
        this.y2 = y2;
        this.x2 = x2;
        this.extent = extent;
        this.layer = layer;
        this.cap = cap;
        this.x1 = x1;
        this.curve = curve;
        this.width = width;
        this.y1 = y1;
        this.style = style;
    }


    public float getY2() {
        return y2;
    }

    public void setY2(float y2) {
        this.y2 = y2;
    }
    public float getX2() {
        return x2;
    }

    public void setX2(float x2) {
        this.x2 = x2;
    }
    public String getExtent() {
        return extent;
    }

    public void setExtent(String extent) {
        this.extent = extent;
    }
    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }
    public String getCap() {
        return cap;
    }

    public void setCap(String cap) {
        this.cap = cap;
    }
    public float getX1() {
        return x1;
    }

    public void setX1(float x1) {
        this.x1 = x1;
    }
    public float getCurve() {
        return curve;
    }

    public void setCurve(float curve) {
        this.curve = curve;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getY1() {
        return y1;
    }

    public void setY1(float y1) {
        this.y1 = y1;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
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