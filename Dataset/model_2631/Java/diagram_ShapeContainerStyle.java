





import java.util.List;
import java.util.ArrayList;

public class diagram_ShapeContainerStyle extends ContainerStyle {

    private String shape;





    private diagram_RGBValues diagram_rgbvalues;


    public diagram_ShapeContainerStyle(
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

    public diagram_RGBValues getDiagram_rgbvalues() {
        return diagram_rgbvalues;
    }

    public void setDiagram_rgbvalues(diagram_RGBValues diagram_rgbvalues) {
        this.diagram_rgbvalues = diagram_rgbvalues;
    }

}