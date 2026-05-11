





import java.util.List;
import java.util.ArrayList;

public class redblacktree2_Tree  {






    private redblacktree2_Node redblacktree2_node;




    private List<redblacktree2_Node> redblacktree2_nodes;


    public redblacktree2_Tree(
    ) {
        this.redblacktree2_nodes = new ArrayList<>();
    }

    public redblacktree2_Tree(
        ArrayList<redblacktree2_Node> redblacktree2_nodes    ) {
        this.redblacktree2_nodes = redblacktree2_nodes;
    }


    public redblacktree2_Node getRedblacktree2_node() {
        return redblacktree2_node;
    }

    public void setRedblacktree2_node(redblacktree2_Node redblacktree2_node) {
        this.redblacktree2_node = redblacktree2_node;
    }
    public List<redblacktree2_Node> getRedblacktree2_nodes() {
        return redblacktree2_nodes;
    }

    public void addRedblacktree2_node(Redblacktree2_node redblacktree2_node) {
        this.redblacktree2_nodes.add(redblacktree2_node);
    }

}