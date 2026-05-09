





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Hole  {

    private float drill;
    private float y;
    private float x;





    private eaglemodel_Plain eaglemodel_plain;




    private eaglemodel_Package eaglemodel_package;


    public eaglemodel_Hole(
        float drill,        float y,        float x    ) {
        this.drill = drill;
        this.y = y;
        this.x = x;
    }


    public float getDrill() {
        return drill;
    }

    public void setDrill(float drill) {
        this.drill = drill;
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