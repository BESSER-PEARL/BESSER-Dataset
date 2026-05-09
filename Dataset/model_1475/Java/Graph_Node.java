





import java.util.List;
import java.util.ArrayList;

public class Graph_Node extends GraphElement {

    private String shape;
    private String style;



    public Graph_Node(
        String shape,        String style    ) {
        super(
        );
        this.shape = shape;
        this.style = style;
    }


    public String getShape() {
        return shape;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}