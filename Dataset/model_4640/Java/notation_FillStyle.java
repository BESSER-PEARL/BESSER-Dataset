





import java.util.List;
import java.util.ArrayList;

public class notation_FillStyle extends Style {

    private int transparency;
    private int fillColor;
    private String gradient;



    public notation_FillStyle(
        int transparency,        int fillColor,        String gradient    ) {
        super(
        );
        this.transparency = transparency;
        this.fillColor = fillColor;
        this.gradient = gradient;
    }


    public int getTransparency() {
        return transparency;
    }

    public void setTransparency(int transparency) {
        this.transparency = transparency;
    }
    public int getFillcolor() {
        return fillColor;
    }

    public void setFillcolor(int fillColor) {
        this.fillColor = fillColor;
    }
    public String getGradient() {
        return gradient;
    }

    public void setGradient(String gradient) {
        this.gradient = gradient;
    }


}