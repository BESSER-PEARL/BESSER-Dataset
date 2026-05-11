





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_ShapeContainerStyleDescription extends style_SizeComputationContainerStyleDescription, style_ContainerStyleDescription {

    private String shape;





    private ColorDescription colordescription;


    public viewpoint_style_ShapeContainerStyleDescription(
        String shape    ) {
        super(
        );
        this.shape = shape;
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