





import java.util.List;
import java.util.ArrayList;

public class notation_FillStyle extends Style {

    private int fillColor;
    private int transparency;
    private String gradient;



    public notation_FillStyle(
        int fillColor,        int transparency,        String gradient    ) {
        super(
        );
        this.fillColor = fillColor;
        this.transparency = transparency;
        this.gradient = gradient;
    }


    public int getFillcolor() {
        return fillColor;
    }

    public void setFillcolor(int fillColor) {
        this.fillColor = fillColor;
    }
    public int getTransparency() {
        return transparency;
    }

    public void setTransparency(int transparency) {
        this.transparency = transparency;
    }
    public String getGradient() {
        return gradient;
    }

    public void setGradient(String gradient) {
        this.gradient = gradient;
    }


}