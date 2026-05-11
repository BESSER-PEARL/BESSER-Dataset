





import java.util.List;
import java.util.ArrayList;

public class gmfgraph_RGBColor extends Color {

    private int blue;
    private int green;
    private int red;



    public gmfgraph_RGBColor(
        int blue,        int green,        int red    ) {
        super(
        );
        this.blue = blue;
        this.green = green;
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
    public int getRed() {
        return red;
    }

    public void setRed(int red) {
        this.red = red;
    }


}