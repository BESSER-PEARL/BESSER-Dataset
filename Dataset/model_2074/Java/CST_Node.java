





import java.util.List;
import java.util.ArrayList;

public class CST_Node  {

    private String kind;





    private CST_Node cst_node;




    private CST_Tree cst_tree;




    private List<CST_Node> cst_nodes;


    public CST_Node(
        String kind    ) {
        this.kind = kind;
        this.cst_nodes = new ArrayList<>();
    }

    public CST_Node(
        String kind        ArrayList<CST_Node> cst_nodes    ) {
        this.kind = kind;
        this.cst_nodes = cst_nodes;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public CST_Node getCst_node() {
        return cst_node;
    }

    public void setCst_node(CST_Node cst_node) {
        this.cst_node = cst_node;
    }
    public CST_Tree getCst_tree() {
        return cst_tree;
    }

    public void setCst_tree(CST_Tree cst_tree) {
        this.cst_tree = cst_tree;
    }
    public List<CST_Node> getCst_nodes() {
        return cst_nodes;
    }

    public void addCst_node(Cst_node cst_node) {
        this.cst_nodes.add(cst_node);
    }

}