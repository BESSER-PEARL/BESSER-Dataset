





import java.util.List;
import java.util.ArrayList;

public class diagram_DNodeContainer extends DDiagramElementContainer {

    private String childrenPresentation;





    private List<diagram_DDiagramElement> diagram_ddiagramelements;


    public diagram_DNodeContainer(
        String childrenPresentation    ) {
        super(
        );
        this.childrenPresentation = childrenPresentation;
        this.diagram_ddiagramelements = new ArrayList<>();
    }

    public diagram_DNodeContainer(
        String childrenPresentation        ArrayList<diagram_DDiagramElement> diagram_ddiagramelements    ) {
        this.childrenPresentation = childrenPresentation;
        this.diagram_ddiagramelements = diagram_ddiagramelements;
    }

    public String getChildrenpresentation() {
        return childrenPresentation;
    }

    public void setChildrenpresentation(String childrenPresentation) {
        this.childrenPresentation = childrenPresentation;
    }

    public List<diagram_DDiagramElement> getDiagram_ddiagramelements() {
        return diagram_ddiagramelements;
    }

    public void addDiagram_ddiagramelement(Diagram_ddiagramelement diagram_ddiagramelement) {
        this.diagram_ddiagramelements.add(diagram_ddiagramelement);
    }

}