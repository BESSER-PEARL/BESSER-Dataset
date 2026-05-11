





import java.util.List;
import java.util.ArrayList;

public class diagram_AbstractDNode extends DDiagramElement {

    private String arrangeConstraints;





    private List<diagram_DNode> diagram_dnodes;


    public diagram_AbstractDNode(
        String arrangeConstraints    ) {
        super(
        );
        this.arrangeConstraints = arrangeConstraints;
        this.diagram_dnodes = new ArrayList<>();
    }

    public diagram_AbstractDNode(
        String arrangeConstraints        ArrayList<diagram_DNode> diagram_dnodes    ) {
        this.arrangeConstraints = arrangeConstraints;
        this.diagram_dnodes = diagram_dnodes;
    }

    public String getArrangeconstraints() {
        return arrangeConstraints;
    }

    public void setArrangeconstraints(String arrangeConstraints) {
        this.arrangeConstraints = arrangeConstraints;
    }

    public List<diagram_DNode> getDiagram_dnodes() {
        return diagram_dnodes;
    }

    public void addDiagram_dnode(Diagram_dnode diagram_dnode) {
        this.diagram_dnodes.add(diagram_dnode);
    }

}