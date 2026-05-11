





import java.util.List;
import java.util.ArrayList;

public class diagram_Lozenge extends NodeStyle {

    private String height;
    private String width;



    public diagram_Lozenge(
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