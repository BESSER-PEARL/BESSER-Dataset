





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_DNodeContainer extends DDiagramElementContainer {

    private String childrenPresentation;





    private List<DDiagramElement> ddiagramelements;


    public viewpoint_diagram_DNodeContainer(
        String childrenPresentation    ) {
        super(
        );
        this.childrenPresentation = childrenPresentation;
        this.ddiagramelements = new ArrayList<>();
    }

    public viewpoint_diagram_DNodeContainer(
        String childrenPresentation        ArrayList<DDiagramElement> ddiagramelements    ) {
        this.childrenPresentation = childrenPresentation;
        this.ddiagramelements = ddiagramelements;
    }

    public String getChildrenpresentation() {
        return childrenPresentation;
    }

    public void setChildrenpresentation(String childrenPresentation) {
        this.childrenPresentation = childrenPresentation;
    }

    public List<DDiagramElement> getDdiagramelements() {
        return ddiagramelements;
    }

    public void addDdiagramelement(Ddiagramelement ddiagramelement) {
        this.ddiagramelements.add(ddiagramelement);
    }

}