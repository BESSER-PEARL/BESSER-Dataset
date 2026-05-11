





import java.util.List;
import java.util.ArrayList;

public class SimpleTree_NodeKind  {






    private List<SimpleTree_NodeKind> simpletree_nodekinds;


    public SimpleTree_NodeKind(
    ) {
        this.simpletree_nodekinds = new ArrayList<>();
    }

    public SimpleTree_NodeKind(
        ArrayList<SimpleTree_NodeKind> simpletree_nodekinds    ) {
        this.simpletree_nodekinds = simpletree_nodekinds;
    }


    public List<SimpleTree_NodeKind> getSimpletree_nodekinds() {
        return simpletree_nodekinds;
    }

    public void addSimpletree_nodekind(Simpletree_nodekind simpletree_nodekind) {
        this.simpletree_nodekinds.add(simpletree_nodekind);
    }

}