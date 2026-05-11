





import java.util.List;
import java.util.ArrayList;

public class shape_Description  {

    private String vAlign;
    private String style;
    private String hAlign;





    private shape_ShapeDefinition shape_shapedefinition;


    public shape_Description(
        String vAlign,        String style,        String hAlign    ) {
        this.vAlign = vAlign;
        this.style = style;
        this.hAlign = hAlign;
    }


    public String getValign() {
        return vAlign;
    }

    public void setValign(String vAlign) {
        this.vAlign = vAlign;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getHalign() {
        return hAlign;
    }

    public void setHalign(String hAlign) {
        this.hAlign = hAlign;
    }

    public shape_ShapeDefinition getShape_shapedefinition() {
        return shape_shapedefinition;
    }

    public void setShape_shapedefinition(shape_ShapeDefinition shape_shapedefinition) {
        this.shape_shapedefinition = shape_shapedefinition;
    }

}