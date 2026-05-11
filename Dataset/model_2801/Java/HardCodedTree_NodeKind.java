





import java.util.List;
import java.util.ArrayList;

public class HardCodedTree_NodeKind  {






    private List<HardCodedTree_NodeKind> hardcodedtree_nodekinds;


    public HardCodedTree_NodeKind(
    ) {
        this.hardcodedtree_nodekinds = new ArrayList<>();
    }

    public HardCodedTree_NodeKind(
        ArrayList<HardCodedTree_NodeKind> hardcodedtree_nodekinds    ) {
        this.hardcodedtree_nodekinds = hardcodedtree_nodekinds;
    }


    public List<HardCodedTree_NodeKind> getHardcodedtree_nodekinds() {
        return hardcodedtree_nodekinds;
    }

    public void addHardcodedtree_nodekind(Hardcodedtree_nodekind hardcodedtree_nodekind) {
        this.hardcodedtree_nodekinds.add(hardcodedtree_nodekind);
    }

}