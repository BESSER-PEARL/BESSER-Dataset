





import java.util.List;
import java.util.ArrayList;

public class Connect4_CirclePanel  {

    private String color;
    private int colorIndex;



    public Connect4_CirclePanel(
        String color,        int colorIndex    ) {
        this.color = color;
        this.colorIndex = colorIndex;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public int getColorindex() {
        return colorIndex;
    }

    public void setColorindex(int colorIndex) {
        this.colorIndex = colorIndex;
    }


}