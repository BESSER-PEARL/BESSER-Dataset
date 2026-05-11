





import java.util.List;
import java.util.ArrayList;

public class geoff_Color extends Identifiable {

    private float alpha;
    private int blue;
    private int red;
    private int green;



    public geoff_Color(
        float alpha,        int blue,        int red,        int green    ) {
        super(
        );
        this.alpha = alpha;
        this.blue = blue;
        this.red = red;
        this.green = green;
    }


    public float getAlpha() {
        return alpha;
    }

    public void setAlpha(float alpha) {
        this.alpha = alpha;
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