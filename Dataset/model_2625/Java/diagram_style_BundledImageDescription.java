





import java.util.List;
import java.util.ArrayList;

public class diagram_style_BundledImageDescription extends NodeStyleDescription {

    private String providedShapeID;
    private String shape;





    private ColorDescription colordescription;


    public diagram_style_BundledImageDescription(
        String providedShapeID,        String shape    ) {
        super(
        );
        this.providedShapeID = providedShapeID;
        this.shape = shape;
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

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}