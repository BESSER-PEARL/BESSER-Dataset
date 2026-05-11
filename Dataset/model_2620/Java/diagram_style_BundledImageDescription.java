





import java.util.List;
import java.util.ArrayList;

public class diagram_style_BundledImageDescription extends NodeStyleDescription {

    private String shape;
    private String providedShapeID;





    private ColorDescription colordescription;


    public diagram_style_BundledImageDescription(
        String shape,        String providedShapeID    ) {
        super(
        );
        this.shape = shape;
        this.providedShapeID = providedShapeID;
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

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}