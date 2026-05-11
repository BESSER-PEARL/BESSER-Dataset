





import java.util.List;
import java.util.ArrayList;

public class tree_Node  {

    private int anAttribute3;
    private int anAttribute2;
    private String name;
    private int anAttribute4;
    private int anAttribute;





    private tree_Node tree_node;




    private List<tree_Node> tree_nodes;




    private tree_Node tree_node;




    private tree_Tree tree_tree;


    public tree_Node(
        int anAttribute3,        int anAttribute2,        String name,        int anAttribute4,        int anAttribute    ) {
        this.anAttribute3 = anAttribute3;
        this.anAttribute2 = anAttribute2;
        this.name = name;
        this.anAttribute4 = anAttribute4;
        this.anAttribute = anAttribute;
        this.tree_nodes = new ArrayList<>();
    }

    public tree_Node(
        int anAttribute3,        int anAttribute2,        String name,        int anAttribute4,        int anAttribute        ArrayList<tree_Node> tree_nodes    ) {
        this.anAttribute3 = anAttribute3;
        this.anAttribute2 = anAttribute2;
        this.name = name;
        this.anAttribute4 = anAttribute4;
        this.anAttribute = anAttribute;
        this.tree_nodes = tree_nodes;
    }

    public int getAnattribute3() {
        return anAttribute3;
    }

    public void setAnattribute3(int anAttribute3) {
        this.anAttribute3 = anAttribute3;
    }
    public int getAnattribute2() {
        return anAttribute2;
    }

    public void setAnattribute2(int anAttribute2) {
        this.anAttribute2 = anAttribute2;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getAnattribute4() {
        return anAttribute4;
    }

    public void setAnattribute4(int anAttribute4) {
        this.anAttribute4 = anAttribute4;
    }
    public int getAnattribute() {
        return anAttribute;
    }

    public void setAnattribute(int anAttribute) {
        this.anAttribute = anAttribute;
    }

    public tree_Node getTree_node() {
        return tree_node;
    }

    public void setTree_node(tree_Node tree_node) {
        this.tree_node = tree_node;
    }
    public List<tree_Node> getTree_nodes() {
        return tree_nodes;
    }

    public void addTree_node(Tree_node tree_node) {
        this.tree_nodes.add(tree_node);
    }
    public tree_Node getTree_node() {
        return tree_node;
    }

    public void setTree_node(tree_Node tree_node) {
        this.tree_node = tree_node;
    }
    public tree_Tree getTree_tree() {
        return tree_tree;
    }

    public void setTree_tree(tree_Tree tree_tree) {
        this.tree_tree = tree_tree;
    }

}