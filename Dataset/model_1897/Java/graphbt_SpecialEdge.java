





import java.util.List;
import java.util.ArrayList;

public class graphbt_SpecialEdge  {

    private String type;
    private int destination;





    private graphbt_Node graphbt_node;


    public graphbt_SpecialEdge(
        String type,        int destination    ) {
        this.type = type;
        this.destination = destination;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getDestination() {
        return destination;
    }

    public void setDestination(int destination) {
        this.destination = destination;
    }

    public graphbt_Node getGraphbt_node() {
        return graphbt_node;
    }

    public void setGraphbt_node(graphbt_Node graphbt_node) {
        this.graphbt_node = graphbt_node;
    }

}