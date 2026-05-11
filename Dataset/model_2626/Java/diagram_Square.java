





import java.util.List;
import java.util.ArrayList;

public class diagram_Square extends NodeStyle {

    private String width;
    private String color;
    private String height;



    public diagram_Square(
        String width,        String color,        String height    ) {
        super(
        );
        this.width = width;
        this.color = color;
        this.height = height;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }


}