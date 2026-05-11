





import java.util.List;
import java.util.ArrayList;

public class diagram_ShapeContainerStyle extends ContainerStyle {

    private String backgroundColor;
    private String shape;



    public diagram_ShapeContainerStyle(
        String backgroundColor,        String shape    ) {
        super(
        );
        this.backgroundColor = backgroundColor;
        this.shape = shape;
    }


    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }


}