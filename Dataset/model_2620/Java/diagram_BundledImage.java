





import java.util.List;
import java.util.ArrayList;

public class diagram_BundledImage extends NodeStyle {

    private String shape;
    private String providedShapeID;
    private String color;



    public diagram_BundledImage(
        String shape,        String providedShapeID,        String color    ) {
        super(
        );
        this.shape = shape;
        this.providedShapeID = providedShapeID;
        this.color = color;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getProvidedshapeid() {
        return providedShapeID;
    }

    public void setProvidedshapeid(String providedShapeID) {
        this.providedShapeID = providedShapeID;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}