





import java.util.List;
import java.util.ArrayList;

public class simpleGraph_Label extends Position {

    private String value;





    private simpleGraph_Edge simplegraph_edge;




    private simpleGraph_Node simplegraph_node;


    public simpleGraph_Label(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public simpleGraph_Edge getSimplegraph_edge() {
        return simplegraph_edge;
    }

    public void setSimplegraph_edge(simpleGraph_Edge simplegraph_edge) {
        this.simplegraph_edge = simplegraph_edge;
    }
    public simpleGraph_Node getSimplegraph_node() {
        return simplegraph_node;
    }

    public void setSimplegraph_node(simpleGraph_Node simplegraph_node) {
        this.simplegraph_node = simplegraph_node;
    }

}