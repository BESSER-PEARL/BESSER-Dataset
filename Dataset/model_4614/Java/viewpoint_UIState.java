





import java.util.List;
import java.util.ArrayList;

public class viewpoint_UIState  {

    private boolean inverseSelectionOrder;





    private viewpoint_DRepresentation viewpoint_drepresentation;




    private List<viewpoint_EObject> viewpoint_eobjects;


    public viewpoint_UIState(
        boolean inverseSelectionOrder    ) {
        this.inverseSelectionOrder = inverseSelectionOrder;
        this.viewpoint_eobjects = new ArrayList<>();
    }

    public viewpoint_UIState(
        boolean inverseSelectionOrder        ArrayList<viewpoint_EObject> viewpoint_eobjects    ) {
        this.inverseSelectionOrder = inverseSelectionOrder;
        this.viewpoint_eobjects = viewpoint_eobjects;
    }

    public boolean getInverseselectionorder() {
        return inverseSelectionOrder;
    }

    public void setInverseselectionorder(boolean inverseSelectionOrder) {
        this.inverseSelectionOrder = inverseSelectionOrder;
    }

    public viewpoint_DRepresentation getViewpoint_drepresentation() {
        return viewpoint_drepresentation;
    }

    public void setViewpoint_drepresentation(viewpoint_DRepresentation viewpoint_drepresentation) {
        this.viewpoint_drepresentation = viewpoint_drepresentation;
    }
    public List<viewpoint_EObject> getViewpoint_eobjects() {
        return viewpoint_eobjects;
    }

    public void addViewpoint_eobject(Viewpoint_eobject viewpoint_eobject) {
        this.viewpoint_eobjects.add(viewpoint_eobject);
    }

}