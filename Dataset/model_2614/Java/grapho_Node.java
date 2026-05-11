





import java.util.List;
import java.util.ArrayList;

public class grapho_Node extends GraphElement {

    private String color;
    private String label;
    private String style;
    private String shape;





    private grapho_Edge grapho_edge;




    private grapho_Edge grapho_edge;


    public grapho_Node(
        String color,        String label,        String style,        String shape    ) {
        super(
        );
        this.color = color;
        this.label = label;
        this.style = style;
        this.shape = shape;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
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

    public grapho_Edge getGrapho_edge() {
        return grapho_edge;
    }

    public void setGrapho_edge(grapho_Edge grapho_edge) {
        this.grapho_edge = grapho_edge;
    }
    public grapho_Edge getGrapho_edge() {
        return grapho_edge;
    }

    public void setGrapho_edge(grapho_Edge grapho_edge) {
        this.grapho_edge = grapho_edge;
    }

}