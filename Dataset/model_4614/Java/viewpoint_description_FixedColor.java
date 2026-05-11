





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_FixedColor extends ColorDescription {

    private int blue;
    private int red;
    private int green;



    public viewpoint_description_FixedColor(
        int blue,        int red,        int green    ) {
        super(
        );
        this.blue = blue;
        this.red = red;
        this.green = green;
    }


    public int getBlue() {
        return blue;
    }

    public void setBlue(int blue) {
        this.blue = blue;
    }
    public int getRed() {
        return red;
    }

    public void setRed(int red) {
        this.red = red;
    }
    public int getGreen() {
        return green;
    }

    public void setGreen(int green) {
        this.green = green;
    }


}