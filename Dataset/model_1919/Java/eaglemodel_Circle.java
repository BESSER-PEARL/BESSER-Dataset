





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Circle  {

    private int layer;
    private float x;
    private float width;
    private float radius;
    private float y;





    private eaglemodel_Package eaglemodel_package;




    private eaglemodel_Plain eaglemodel_plain;


    public eaglemodel_Circle(
        int layer,        float x,        float width,        float radius,        float y    ) {
        this.layer = layer;
        this.x = x;
        this.width = width;
        this.radius = radius;
        this.y = y;
    }


    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getRadius() {
        return radius;
    }

    public void setRadius(float radius) {
        this.radius = radius;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
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