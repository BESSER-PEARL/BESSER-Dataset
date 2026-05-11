





import java.util.List;
import java.util.ArrayList;

public class notation_FillStyle extends Style {

    private int fillColor;
    private int transparency;



    public notation_FillStyle(
        int fillColor,        int transparency    ) {
        super(
        );
        this.fillColor = fillColor;
        this.transparency = transparency;
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