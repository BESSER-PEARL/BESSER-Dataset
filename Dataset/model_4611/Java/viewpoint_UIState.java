





import java.util.List;
import java.util.ArrayList;

public class viewpoint_UIState  {

    private String decorationImage;
    private boolean inverseSelectionOrder;
    private String subDiagramDecorationDescriptors;





    private List<viewpoint_EObject> viewpoint_eobjects;




    private viewpoint_DRepresentation viewpoint_drepresentation;


    public viewpoint_UIState(
        String decorationImage,        boolean inverseSelectionOrder,        String subDiagramDecorationDescriptors    ) {
        this.decorationImage = decorationImage;
        this.inverseSelectionOrder = inverseSelectionOrder;
        this.subDiagramDecorationDescriptors = subDiagramDecorationDescriptors;
        this.viewpoint_eobjects = new ArrayList<>();
    }

    public viewpoint_UIState(
        String decorationImage,        boolean inverseSelectionOrder,        String subDiagramDecorationDescriptors        ArrayList<viewpoint_EObject> viewpoint_eobjects    ) {
        this.decorationImage = decorationImage;
        this.inverseSelectionOrder = inverseSelectionOrder;
        this.subDiagramDecorationDescriptors = subDiagramDecorationDescriptors;
        this.viewpoint_eobjects = viewpoint_eobjects;
    }

    public String getDecorationimage() {
        return decorationImage;
    }

    public void setDecorationimage(String decorationImage) {
        this.decorationImage = decorationImage;
    }
    public boolean getInverseselectionorder() {
        return inverseSelectionOrder;
    }

    public void setInverseselectionorder(boolean inverseSelectionOrder) {
        this.inverseSelectionOrder = inverseSelectionOrder;
    }
    public String getSubdiagramdecorationdescriptors() {
        return subDiagramDecorationDescriptors;
    }

    public void setSubdiagramdecorationdescriptors(String subDiagramDecorationDescriptors) {
        this.subDiagramDecorationDescriptors = subDiagramDecorationDescriptors;
    }

    public List<viewpoint_EObject> getViewpoint_eobjects() {
        return viewpoint_eobjects;
    }

    public void addViewpoint_eobject(Viewpoint_eobject viewpoint_eobject) {
        this.viewpoint_eobjects.add(viewpoint_eobject);
    }
    public viewpoint_DRepresentation getViewpoint_drepresentation() {
        return viewpoint_drepresentation;
    }

    public void setViewpoint_drepresentation(viewpoint_DRepresentation viewpoint_drepresentation) {
        this.viewpoint_drepresentation = viewpoint_drepresentation;
    }

}