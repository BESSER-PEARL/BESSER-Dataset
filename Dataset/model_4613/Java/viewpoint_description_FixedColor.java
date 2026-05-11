





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_FixedColor extends ColorDescription {

    private int green;
    private int red;
    private int blue;



    public viewpoint_description_FixedColor(
        int green,        int red,        int blue    ) {
        super(
        );
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


}