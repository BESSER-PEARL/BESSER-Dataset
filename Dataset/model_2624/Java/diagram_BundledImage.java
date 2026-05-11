





import java.util.List;
import java.util.ArrayList;

public class diagram_BundledImage extends NodeStyle {

    private String providedShapeID;
    private String shape;
    private String color;



    public diagram_BundledImage(
        String providedShapeID,        String shape,        String color    ) {
        super(
        );
        this.providedShapeID = providedShapeID;
        this.shape = shape;
        this.color = color;
    }


    public String getProvidedshapeid() {
        return providedShapeID;
    }

    public void setProvidedshapeid(String providedShapeID) {
        this.providedShapeID = providedShapeID;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}