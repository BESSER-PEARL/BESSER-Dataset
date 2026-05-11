





import java.util.List;
import java.util.ArrayList;

public class tree2talltree_Node2TallNode  {

    private String name;





    private tree2talltree_Node2TallNode tree2talltree_node2tallnode;




    private List<tree2talltree_Node2TallNode> tree2talltree_node2tallnodes;


    public tree2talltree_Node2TallNode(
        String name    ) {
        this.name = name;
        this.tree2talltree_node2tallnodes = new ArrayList<>();
    }

    public tree2talltree_Node2TallNode(
        String name        ArrayList<tree2talltree_Node2TallNode> tree2talltree_node2tallnodes    ) {
        this.name = name;
        this.tree2talltree_node2tallnodes = tree2talltree_node2tallnodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tree2talltree_Node2TallNode getTree2talltree_node2tallnode() {
        return tree2talltree_node2tallnode;
    }

    public void setTree2talltree_node2tallnode(tree2talltree_Node2TallNode tree2talltree_node2tallnode) {
        this.tree2talltree_node2tallnode = tree2talltree_node2tallnode;
    }
    public List<tree2talltree_Node2TallNode> getTree2talltree_node2tallnodes() {
        return tree2talltree_node2tallnodes;
    }

    public void addTree2talltree_node2tallnode(Tree2talltree_node2tallnode tree2talltree_node2tallnode) {
        this.tree2talltree_node2tallnodes.add(tree2talltree_node2tallnode);
    }

}