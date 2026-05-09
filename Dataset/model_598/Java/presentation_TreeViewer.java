





import java.util.List;
import java.util.ArrayList;

public class presentation_TreeViewer extends AbstractTreeViewer {

    private String group5;





    private List<presentation_Tree> presentation_trees;


    public presentation_TreeViewer(
        String group5    ) {
        super(
        );
        this.group5 = group5;
        this.presentation_trees = new ArrayList<>();
    }

    public presentation_TreeViewer(
        String group5        ArrayList<presentation_Tree> presentation_trees    ) {
        this.group5 = group5;
        this.presentation_trees = presentation_trees;
    }

    public String getGroup5() {
        return group5;
    }

    public void setGroup5(String group5) {
        this.group5 = group5;
    }

    public List<presentation_Tree> getPresentation_trees() {
        return presentation_trees;
    }

    public void addPresentation_tree(Presentation_tree presentation_tree) {
        this.presentation_trees.add(presentation_tree);
    }

}