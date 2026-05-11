





import java.util.List;
import java.util.ArrayList;

public class diagram_style_ShapeContainerStyleDescription extends style_ContainerStyleDescription, style_SizeComputationContainerStyleDescription {

    private String shape;



    public diagram_style_ShapeContainerStyleDescription(
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


}