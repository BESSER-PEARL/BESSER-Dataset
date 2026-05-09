





import java.util.List;
import java.util.ArrayList;

public class RepresentationGraph_Rectangle extends ContainerElement {

    private String width;
    private String height;



    public RepresentationGraph_Rectangle(
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