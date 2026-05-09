





import java.util.List;
import java.util.ArrayList;

public class presentation_TableTreeViewer extends AbstractTreeViewer {

    private String group5;





    private List<presentation_TableTree> presentation_tabletrees;


    public presentation_TableTreeViewer(
        String group5    ) {
        super(
        );
        this.group5 = group5;
        this.presentation_tabletrees = new ArrayList<>();
    }

    public presentation_TableTreeViewer(
        String group5        ArrayList<presentation_TableTree> presentation_tabletrees    ) {
        this.group5 = group5;
        this.presentation_tabletrees = presentation_tabletrees;
    }

    public String getGroup5() {
        return group5;
    }

    public void setGroup5(String group5) {
        this.group5 = group5;
    }

    public List<presentation_TableTree> getPresentation_tabletrees() {
        return presentation_tabletrees;
    }

    public void addPresentation_tabletree(Presentation_tabletree presentation_tabletree) {
        this.presentation_tabletrees.add(presentation_tabletree);
    }

}