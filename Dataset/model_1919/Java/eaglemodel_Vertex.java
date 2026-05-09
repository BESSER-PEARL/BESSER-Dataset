





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Vertex  {

    private float y;
    private float x;
    private float curve;





    private eaglemodel_Polygon eaglemodel_polygon;


    public eaglemodel_Vertex(
        float y,        float x,        float curve    ) {
        this.y = y;
        this.x = x;
        this.curve = curve;
    }


    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getCurve() {
        return curve;
    }

    public void setCurve(float curve) {
        this.curve = curve;
    }

    public eaglemodel_Polygon getEaglemodel_polygon() {
        return eaglemodel_polygon;
    }

    public void setEaglemodel_polygon(eaglemodel_Polygon eaglemodel_polygon) {
        this.eaglemodel_polygon = eaglemodel_polygon;
    }

}