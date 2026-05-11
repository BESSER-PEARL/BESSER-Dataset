





import java.util.List;
import java.util.ArrayList;

public class eCoreContainemntTree_Node  {

    private String name;





    private eCoreContainemntTree_Node ecorecontainemnttree_node;




    private List<eCoreContainemntTree_Node> ecorecontainemnttree_nodes;




    private eCoreContainemntTree_Node ecorecontainemnttree_node;




    private eCoreContainemntTree_Node ecorecontainemnttree_node;


    public eCoreContainemntTree_Node(
        String name    ) {
        this.name = name;
        this.ecorecontainemnttree_nodes = new ArrayList<>();
    }

    public eCoreContainemntTree_Node(
        String name        ArrayList<eCoreContainemntTree_Node> ecorecontainemnttree_nodes    ) {
        this.name = name;
        this.ecorecontainemnttree_nodes = ecorecontainemnttree_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public eCoreContainemntTree_Node getEcorecontainemnttree_node() {
        return ecorecontainemnttree_node;
    }

    public void setEcorecontainemnttree_node(eCoreContainemntTree_Node ecorecontainemnttree_node) {
        this.ecorecontainemnttree_node = ecorecontainemnttree_node;
    }
    public List<eCoreContainemntTree_Node> getEcorecontainemnttree_nodes() {
        return ecorecontainemnttree_nodes;
    }

    public void addEcorecontainemnttree_node(Ecorecontainemnttree_node ecorecontainemnttree_node) {
        this.ecorecontainemnttree_nodes.add(ecorecontainemnttree_node);
    }
    public eCoreContainemntTree_Node getEcorecontainemnttree_node() {
        return ecorecontainemnttree_node;
    }

    public void setEcorecontainemnttree_node(eCoreContainemntTree_Node ecorecontainemnttree_node) {
        this.ecorecontainemnttree_node = ecorecontainemnttree_node;
    }
    public eCoreContainemntTree_Node getEcorecontainemnttree_node() {
        return ecorecontainemnttree_node;
    }

    public void setEcorecontainemnttree_node(eCoreContainemntTree_Node ecorecontainemnttree_node) {
        this.ecorecontainemnttree_node = ecorecontainemnttree_node;
    }

}