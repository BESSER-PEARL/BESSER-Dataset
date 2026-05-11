





import java.util.List;
import java.util.ArrayList;

public class grapho_Edge extends GraphElement {

    private boolean constraintRank;
    private String style;
    private String color;





    private grapho_Node grapho_node;




    private grapho_Node grapho_node;


    public grapho_Edge(
        boolean constraintRank,        String style,        String color    ) {
        super(
        );
        this.constraintRank = constraintRank;
        this.style = style;
        this.color = color;
    }


    public boolean getConstraintrank() {
        return constraintRank;
    }

    public void setConstraintrank(boolean constraintRank) {
        this.constraintRank = constraintRank;
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

    public grapho_Node getGrapho_node() {
        return grapho_node;
    }

    public void setGrapho_node(grapho_Node grapho_node) {
        this.grapho_node = grapho_node;
    }
    public grapho_Node getGrapho_node() {
        return grapho_node;
    }

    public void setGrapho_node(grapho_Node grapho_node) {
        this.grapho_node = grapho_node;
    }

}