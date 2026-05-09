





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Text  {

    private float y;
    private String font;
    private int rot;
    private int ratio;
    private String align;
    private String value;
    private float x;
    private int distance;
    private float size;
    private int layer;





    private eaglemodel_Package eaglemodel_package;




    private eaglemodel_Plain eaglemodel_plain;


    public eaglemodel_Text(
        float y,        String font,        int rot,        int ratio,        String align,        String value,        float x,        int distance,        float size,        int layer    ) {
        this.y = y;
        this.font = font;
        this.rot = rot;
        this.ratio = ratio;
        this.align = align;
        this.value = value;
        this.x = x;
        this.distance = distance;
        this.size = size;
        this.layer = layer;
    }


    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public String getFont() {
        return font;
    }

    public void setFont(String font) {
        this.font = font;
    }
    public int getRot() {
        return rot;
    }

    public void setRot(int rot) {
        this.rot = rot;
    }
    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }
    public String getAlign() {
        return align;
    }

    public void setAlign(String align) {
        this.align = align;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public int getDistance() {
        return distance;
    }

    public void setDistance(int distance) {
        this.distance = distance;
    }
    public float getSize() {
        return size;
    }

    public void setSize(float size) {
        this.size = size;
    }
    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }

    public eaglemodel_Package getEaglemodel_package() {
        return eaglemodel_package;
    }

    public void setEaglemodel_package(eaglemodel_Package eaglemodel_package) {
        this.eaglemodel_package = eaglemodel_package;
    }
    public eaglemodel_Plain getEaglemodel_plain() {
        return eaglemodel_plain;
    }

    public void setEaglemodel_plain(eaglemodel_Plain eaglemodel_plain) {
        this.eaglemodel_plain = eaglemodel_plain;
    }

}