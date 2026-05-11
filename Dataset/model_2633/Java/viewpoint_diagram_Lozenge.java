





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_Lozenge extends NodeStyle {

    private String width;
    private String height;



    public viewpoint_diagram_Lozenge(
        String width,        String height    ) {
        super(
        );
        this.width = width;
        this.height = height;
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


}