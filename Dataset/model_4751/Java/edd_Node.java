





import java.util.List;
import java.util.ArrayList;

public class edd_Node extends TreeElement {






    private List<edd_TreeElement> edd_treeelements;


    public edd_Node(
    ) {
        super(
        );
        this.edd_treeelements = new ArrayList<>();
    }

    public edd_Node(
        ArrayList<edd_TreeElement> edd_treeelements    ) {
        this.edd_treeelements = edd_treeelements;
    }


    public List<edd_TreeElement> getEdd_treeelements() {
        return edd_treeelements;
    }

    public void addEdd_treeelement(Edd_treeelement edd_treeelement) {
        this.edd_treeelements.add(edd_treeelement);
    }

}