





import java.util.List;
import java.util.ArrayList;

public class diagram_ShapeContainerStyle extends ContainerStyle {

    private String shape;
    private String backgroundColor;



    public diagram_ShapeContainerStyle(
        String shape,        String backgroundColor    ) {
        super(
        );
        this.shape = shape;
        this.backgroundColor = backgroundColor;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }


}