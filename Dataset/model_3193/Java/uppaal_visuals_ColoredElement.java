





import java.util.List;
import java.util.ArrayList;

public class uppaal_visuals_ColoredElement  {

    private String color;
    private String colorCode;



    public uppaal_visuals_ColoredElement(
        String color,        String colorCode    ) {
        this.color = color;
        this.colorCode = colorCode;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getColorcode() {
        return colorCode;
    }

    public void setColorcode(String colorCode) {
        this.colorCode = colorCode;
    }


}