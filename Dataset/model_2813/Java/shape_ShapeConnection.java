





import java.util.List;
import java.util.ArrayList;

public class shape_ShapeConnection  {

    private String style;





    private shape_PlacingDefinition shape_placingdefinition;


    public shape_ShapeConnection(
        String style    ) {
        this.style = style;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }

    public shape_PlacingDefinition getShape_placingdefinition() {
        return shape_placingdefinition;
    }

    public void setShape_placingdefinition(shape_PlacingDefinition shape_placingdefinition) {
        this.shape_placingdefinition = shape_placingdefinition;
    }

}