





import java.util.List;
import java.util.ArrayList;

public class VisualInterface_Position  {

    private float x;
    private float y;





    private VisualInterface_XYChild visualinterface_xychild;




    private VisualInterface_Line visualinterface_line;


    public VisualInterface_Position(
        float x,        float y    ) {
        this.x = x;
        this.y = y;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }

    public VisualInterface_XYChild getVisualinterface_xychild() {
        return visualinterface_xychild;
    }

    public void setVisualinterface_xychild(VisualInterface_XYChild visualinterface_xychild) {
        this.visualinterface_xychild = visualinterface_xychild;
    }
    public VisualInterface_Line getVisualinterface_line() {
        return visualinterface_line;
    }

    public void setVisualinterface_line(VisualInterface_Line visualinterface_line) {
        this.visualinterface_line = visualinterface_line;
    }

}