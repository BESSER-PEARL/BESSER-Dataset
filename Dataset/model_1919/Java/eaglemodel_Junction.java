





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Junction  {

    private float y;
    private float x;





    private eaglemodel_Segment eaglemodel_segment;


    public eaglemodel_Junction(
        float y,        float x    ) {
        this.y = y;
        this.x = x;
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

    public eaglemodel_Segment getEaglemodel_segment() {
        return eaglemodel_segment;
    }

    public void setEaglemodel_segment(eaglemodel_Segment eaglemodel_segment) {
        this.eaglemodel_segment = eaglemodel_segment;
    }

}