





import java.util.List;
import java.util.ArrayList;

public class diagram_Lozenge extends NodeStyle {

    private String width;
    private String height;
    private String color;



    public diagram_Lozenge(
        String width,        String height,        String color    ) {
        super(
        );
        this.width = width;
        this.height = height;
        this.color = color;
    }


    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
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


}