





import java.util.List;
import java.util.ArrayList;

public class styles_RGBColor extends Color {

    private int red;
    private int blue;
    private int green;



    public styles_RGBColor(
        int red,        int blue,        int green    ) {
        super(
        );
        this.red = red;
        this.blue = blue;
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
    public int getGreen() {
        return green;
    }

    public void setGreen(int green) {
        this.green = green;
    }


}