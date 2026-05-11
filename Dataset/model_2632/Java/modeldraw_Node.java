





import java.util.List;
import java.util.ArrayList;

public class modeldraw_Node extends NamedItem {

    private String style;
    private String color;
    private String type;
    private String shape;



    public modeldraw_Node(
        String style,        String color,        String type,        String shape    ) {
        super(
        );
        this.style = style;
        this.color = color;
        this.type = type;
        this.shape = shape;
    }


    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }


}