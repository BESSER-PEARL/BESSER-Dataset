





import java.util.List;
import java.util.ArrayList;

public class documentation_Width  {

    private String width;
    private String unit;





    private documentation_Image documentation_image;


    public documentation_Width(
        String width,        String unit    ) {
        this.width = width;
        this.unit = unit;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public documentation_Image getDocumentation_image() {
        return documentation_image;
    }

    public void setDocumentation_image(documentation_Image documentation_image) {
        this.documentation_image = documentation_image;
    }

}