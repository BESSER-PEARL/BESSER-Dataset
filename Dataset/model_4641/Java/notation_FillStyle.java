





import java.util.List;
import java.util.ArrayList;

public class notation_FillStyle extends Style {

    private String gradient;
    private int fillColor;
    private int transparency;



    public notation_FillStyle(
        String gradient,        int fillColor,        int transparency    ) {
        super(
        );
        this.gradient = gradient;
        this.fillColor = fillColor;
        this.transparency = transparency;
    }


    public String getGradient() {
        return gradient;
    }

    public void setGradient(String gradient) {
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


}