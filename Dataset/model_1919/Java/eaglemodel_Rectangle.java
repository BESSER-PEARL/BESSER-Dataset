





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Rectangle  {

    private int layer;
    private float y2;
    private float y1;
    private float x2;
    private float x1;
    private int rot;





    private eaglemodel_Package eaglemodel_package;




    private eaglemodel_Plain eaglemodel_plain;


    public eaglemodel_Rectangle(
        int layer,        float y2,        float y1,        float x2,        float x1,        int rot    ) {
        this.layer = layer;
        this.y2 = y2;
        this.y1 = y1;
        this.x2 = x2;
        this.x1 = x1;
        this.rot = rot;
    }


    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }
    public float getY2() {
        return y2;
    }

    public void setY2(float y2) {
        this.y2 = y2;
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
    public float getX1() {
        return x1;
    }

    public void setX1(float x1) {
        this.x1 = x1;
    }
    public int getRot() {
        return rot;
    }

    public void setRot(int rot) {
        this.rot = rot;
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