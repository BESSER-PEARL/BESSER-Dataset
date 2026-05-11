





import java.util.List;
import java.util.ArrayList;

public class uppaal_visuals_ColoredElement  {

    private String colorCode;
    private String color;



    public uppaal_visuals_ColoredElement(
        String colorCode,        String color    ) {
        this.colorCode = colorCode;
        this.color = color;
    }


    public String getColorcode() {
        return colorCode;
    }

    public void setColorcode(String colorCode) {
        this.colorCode = colorCode;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}