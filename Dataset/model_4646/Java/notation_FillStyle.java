





import java.util.List;
import java.util.ArrayList;

public class notation_FillStyle extends Style {

    private String gradient;
    private int transparency;
    private int fillColor;



    public notation_FillStyle(
        String gradient,        int transparency,        int fillColor    ) {
        super(
        );
        this.gradient = gradient;
        this.transparency = transparency;
        this.fillColor = fillColor;
    }


    public String getGradient() {
        return gradient;
    }

    public void setGradient(String gradient) {
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


}