





import java.util.List;
import java.util.ArrayList;

public class SimpleTree_NodeKind  {






    private SimpleTree_Tree simpletree_tree;




    private List<SimpleTree_NodeKind> simpletree_nodekinds;


    public SimpleTree_NodeKind(
    ) {
        this.simpletree_nodekinds = new ArrayList<>();
    }

    public SimpleTree_NodeKind(
        ArrayList<SimpleTree_NodeKind> simpletree_nodekinds    ) {
        this.simpletree_nodekinds = simpletree_nodekinds;
    }


    public SimpleTree_Tree getSimpletree_tree() {
        return simpletree_tree;
    }

    public void setSimpletree_tree(SimpleTree_Tree simpletree_tree) {
        this.simpletree_tree = simpletree_tree;
    }
    public List<SimpleTree_NodeKind> getSimpletree_nodekinds() {
        return simpletree_nodekinds;
    }

    public void addSimpletree_nodekind(Simpletree_nodekind simpletree_nodekind) {
        this.simpletree_nodekinds.add(simpletree_nodekind);
    }

}