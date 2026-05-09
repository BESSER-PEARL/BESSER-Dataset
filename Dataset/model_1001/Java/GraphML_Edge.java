





import java.util.List;
import java.util.ArrayList;

public class GraphML_Edge extends Element {

    private String directed;



    public GraphML_Edge(
        String directed    ) {
        super(
        );
        this.directed = directed;
    }


    public String getDirected() {
        return directed;
    }

    public void setDirected(String directed) {
        this.directed = directed;
    }


}