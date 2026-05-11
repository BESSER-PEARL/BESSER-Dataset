





import java.util.List;
import java.util.ArrayList;

public class trees_Node  {






    private List<trees_Node> trees_nodes;


    public trees_Node(
    ) {
        this.trees_nodes = new ArrayList<>();
    }

    public trees_Node(
        ArrayList<trees_Node> trees_nodes    ) {
        this.trees_nodes = trees_nodes;
    }


    public List<trees_Node> getTrees_nodes() {
        return trees_nodes;
    }

    public void addTrees_node(Trees_node trees_node) {
        this.trees_nodes.add(trees_node);
    }

}