





import java.util.List;
import java.util.ArrayList;

public class statesml_Edge  {

    private String name;





    private statesml_Node statesml_node;




    private List<statesml_Node> statesml_nodes;


    public statesml_Edge(
        String name    ) {
        this.name = name;
        this.statesml_nodes = new ArrayList<>();
    }

    public statesml_Edge(
        String name        ArrayList<statesml_Node> statesml_nodes    ) {
        this.name = name;
        this.statesml_nodes = statesml_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statesml_Node getStatesml_node() {
        return statesml_node;
    }

    public void setStatesml_node(statesml_Node statesml_node) {
        this.statesml_node = statesml_node;
    }
    public List<statesml_Node> getStatesml_nodes() {
        return statesml_nodes;
    }

    public void addStatesml_node(Statesml_node statesml_node) {
        this.statesml_nodes.add(statesml_node);
    }

}