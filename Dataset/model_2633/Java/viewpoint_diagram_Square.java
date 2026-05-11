





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_Square extends NodeStyle {

    private String height;
    private String width;



    public viewpoint_diagram_Square(
        String height,        String width    ) {
        super(
        );
        this.height = height;
        this.width = width;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}