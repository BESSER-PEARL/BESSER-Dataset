





import java.util.List;
import java.util.ArrayList;

public class diagram_Square extends NodeStyle {

    private String height;
    private String color;
    private String width;



    public diagram_Square(
        String height,        String color,        String width    ) {
        super(
        );
        this.height = height;
        this.color = color;
        this.width = width;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}