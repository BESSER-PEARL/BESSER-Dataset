





import java.util.List;
import java.util.ArrayList;

public class RepresentationGraph_Rhombus extends ContainerElement {

    private String height;
    private String width;



    public RepresentationGraph_Rhombus(
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