





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DRepresentationElement extends DRefreshable, DMappingBased, DSemanticDecorator, DLabelled, DStylizable {

    private String name;





    private viewpoint_DRepresentation viewpoint_drepresentation;




    private List<viewpoint_EObject> viewpoint_eobjects;




    private viewpoint_DRepresentation viewpoint_drepresentation;


    public viewpoint_DRepresentationElement(
        String name    ) {
        super(
        );
        this.name = name;
        this.viewpoint_eobjects = new ArrayList<>();
    }

    public viewpoint_DRepresentationElement(
        String name        ArrayList<viewpoint_EObject> viewpoint_eobjects    ) {
        this.name = name;
        this.viewpoint_eobjects = viewpoint_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public viewpoint_DRepresentation getViewpoint_drepresentation() {
        return viewpoint_drepresentation;
    }

    public void setViewpoint_drepresentation(viewpoint_DRepresentation viewpoint_drepresentation) {
        this.viewpoint_drepresentation = viewpoint_drepresentation;
    }

}