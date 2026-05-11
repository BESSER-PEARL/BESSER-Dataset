





import java.util.List;
import java.util.ArrayList;

public class viewpoint_RGBValues  {

    private int green;
    private int red;
    private int blue;





    private viewpoint_BasicLabelStyle viewpoint_basiclabelstyle;


    public viewpoint_RGBValues(
        int green,        int red,        int blue    ) {
        this.green = green;
        this.red = red;
        this.blue = blue;
    }


    public int getGreen() {
        return green;
    }

    public void setGreen(int green) {
        this.green = green;
    }
    public int getRed() {
        return red;
    }

    public void setRed(int red) {
        this.red = red;
    }
    public int getBlue() {
        return blue;
    }

    public void setBlue(int blue) {
        this.blue = blue;
    }

    public viewpoint_BasicLabelStyle getViewpoint_basiclabelstyle() {
        return viewpoint_basiclabelstyle;
    }

    public void setViewpoint_basiclabelstyle(viewpoint_BasicLabelStyle viewpoint_basiclabelstyle) {
        this.viewpoint_basiclabelstyle = viewpoint_basiclabelstyle;
    }

}