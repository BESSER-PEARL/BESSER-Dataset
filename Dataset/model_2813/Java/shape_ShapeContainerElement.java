





import java.util.List;
import java.util.ArrayList;

public class shape_ShapeContainerElement  {

    private String style;
    private String name;





    private shape_ShapeContainer shape_shapecontainer;


    public shape_ShapeContainerElement(
        String style,        String name    ) {
        this.style = style;
        this.name = name;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public shape_ShapeContainer getShape_shapecontainer() {
        return shape_shapecontainer;
    }

    public void setShape_shapecontainer(shape_ShapeContainer shape_shapecontainer) {
        this.shape_shapecontainer = shape_shapecontainer;
    }

}