





import java.util.List;
import java.util.ArrayList;

public class swt_RGBColor extends Color {

    private int green;
    private int blue;
    private int red;



    public swt_RGBColor(
        int green,        int blue,        int red    ) {
        super(
        );
        this.green = green;
        this.blue = blue;
        this.red = red;
    }


    public int getGreen() {
        return green;
    }

    public void setGreen(int green) {
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


}