





import java.util.List;
import java.util.ArrayList;

public class grapho_Node extends GraphElement {

    private String label;
    private String style;
    private String shape;
    private String color;



    public grapho_Node(
        String label,        String style,        String shape,        String color    ) {
        super(
        );
        this.label = label;
        this.style = style;
        this.shape = shape;
        this.color = color;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
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