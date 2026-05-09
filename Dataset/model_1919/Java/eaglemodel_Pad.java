





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Pad  {

    private String name;
    private boolean thermals;
    private String shape;
    private boolean stop;
    private float drill;
    private int rot;
    private float x;
    private boolean first;
    private float y;
    private float diameter;





    private eaglemodel_Package eaglemodel_package;


    public eaglemodel_Pad(
        String name,        boolean thermals,        String shape,        boolean stop,        float drill,        int rot,        float x,        boolean first,        float y,        float diameter    ) {
        this.name = name;
        this.thermals = thermals;
        this.shape = shape;
        this.stop = stop;
        this.drill = drill;
        this.rot = rot;
        this.x = x;
        this.first = first;
        this.y = y;
        this.diameter = diameter;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getThermals() {
        return thermals;
    }

    public void setThermals(boolean thermals) {
        this.thermals = thermals;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public boolean getStop() {
        return stop;
    }

    public void setStop(boolean stop) {
        this.stop = stop;
    }
    public float getDrill() {
        return drill;
    }

    public void setDrill(float drill) {
        this.drill = drill;
    }
    public int getRot() {
        return rot;
    }

    public void setRot(int rot) {
        this.rot = rot;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public boolean getFirst() {
        return first;
    }

    public void setFirst(boolean first) {
        this.first = first;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getDiameter() {
        return diameter;
    }

    public void setDiameter(float diameter) {
        this.diameter = diameter;
    }

    public eaglemodel_Package getEaglemodel_package() {
        return eaglemodel_package;
    }

    public void setEaglemodel_package(eaglemodel_Package eaglemodel_package) {
        this.eaglemodel_package = eaglemodel_package;
    }

}