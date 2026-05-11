





import java.util.List;
import java.util.ArrayList;

public class farrusco_Filho  {






    private List<farrusco_Node> farrusco_nodes;


    public farrusco_Filho(
    ) {
        this.farrusco_nodes = new ArrayList<>();
    }

    public farrusco_Filho(
        ArrayList<farrusco_Node> farrusco_nodes    ) {
        this.farrusco_nodes = farrusco_nodes;
    }


    public List<farrusco_Node> getFarrusco_nodes() {
        return farrusco_nodes;
    }

    public void addFarrusco_node(Farrusco_node farrusco_node) {
        this.farrusco_nodes.add(farrusco_node);
    }

}