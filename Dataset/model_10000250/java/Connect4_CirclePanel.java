





import java.util.List;
import java.util.ArrayList;

public class Connect4_CirclePanel  {

    private int colorIndex;
    private String color;



    public Connect4_CirclePanel(
        int colorIndex,        String color    ) {
        this.colorIndex = colorIndex;
        this.color = color;
    }


    public int getColorindex() {
        return colorIndex;
    }

    public void setColorindex(int colorIndex) {
        this.colorIndex = colorIndex;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}