





import java.util.List;
import java.util.ArrayList;

public class shape_Shape  {

    private String style;





    private shape_ShapeDefinition shape_shapedefinition;


    public shape_Shape(
        String style    ) {
        this.style = style;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public shape_ShapeDefinition getShape_shapedefinition() {
        return shape_shapedefinition;
    }

    public void setShape_shapedefinition(shape_ShapeDefinition shape_shapedefinition) {
        this.shape_shapedefinition = shape_shapedefinition;
    }

}