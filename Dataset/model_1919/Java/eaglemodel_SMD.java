





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_SMD  {

    private boolean stop;
    private boolean cream;
    private float dx;
    private float y;
    private float x;
    private int roundness;
    private String name;
    private int layer;
    private boolean thermals;
    private int rot;
    private float dy;





    private eaglemodel_Package eaglemodel_package;


    public eaglemodel_SMD(
        boolean stop,        boolean cream,        float dx,        float y,        float x,        int roundness,        String name,        int layer,        boolean thermals,        int rot,        float dy    ) {
        this.stop = stop;
        this.cream = cream;
        this.dx = dx;
        this.y = y;
        this.x = x;
        this.roundness = roundness;
        this.name = name;
        this.layer = layer;
        this.thermals = thermals;
        this.rot = rot;
        this.dy = dy;
    }


    public boolean getStop() {
        return stop;
    }

    public void setStop(boolean stop) {
        this.stop = stop;
    }
    public boolean getCream() {
        return cream;
    }

    public void setCream(boolean cream) {
        this.cream = cream;
    }
    public float getDx() {
        return dx;
    }

    public void setDx(float dx) {
        this.dx = dx;
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
    public int getRoundness() {
        return roundness;
    }

    public void setRoundness(int roundness) {
        this.roundness = roundness;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLayer() {
        return layer;
    }

    public void setLayer(int layer) {
        this.layer = layer;
    }
    public boolean getThermals() {
        return thermals;
    }

    public void setThermals(boolean thermals) {
        this.thermals = thermals;
    }
    public int getRot() {
        return rot;
    }

    public void setRot(int rot) {
        this.rot = rot;
    }
    public float getDy() {
        return dy;
    }

    public void setDy(float dy) {
        this.dy = dy;
    }

    public eaglemodel_Package getEaglemodel_package() {
        return eaglemodel_package;
    }

    public void setEaglemodel_package(eaglemodel_Package eaglemodel_package) {
        this.eaglemodel_package = eaglemodel_package;
    }

}