





import java.util.List;
import java.util.ArrayList;

public class Dot_Node extends GraphElement {

    private String style;
    private String shape;



    public Dot_Node(
        String style,        String shape    ) {
        super(
        );
        this.style = style;
        this.shape = shape;
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


}