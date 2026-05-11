





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DRepresentation extends description_DocumentedElement, description_DModelElement, DRefreshable {

    private String name;





    private List<viewpoint_DRepresentationElement> viewpoint_drepresentationelements;




    private viewpoint_DView viewpoint_dview;




    private List<viewpoint_DRepresentationElement> viewpoint_drepresentationelements;


    public viewpoint_DRepresentation(
        String name    ) {
        super(
        );
        this.name = name;
        this.viewpoint_drepresentationelements = new ArrayList<>();
        this.viewpoint_drepresentationelements = new ArrayList<>();
    }

    public viewpoint_DRepresentation(
        String name        ArrayList<viewpoint_DRepresentationElement> viewpoint_drepresentationelements,        ArrayList<viewpoint_DRepresentationElement> viewpoint_drepresentationelements    ) {
        this.name = name;
        this.viewpoint_drepresentationelements = viewpoint_drepresentationelements;
        this.viewpoint_drepresentationelements = viewpoint_drepresentationelements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<viewpoint_DRepresentationElement> getViewpoint_drepresentationelements() {
        return viewpoint_drepresentationelements;
    }

    public void addViewpoint_drepresentationelement(Viewpoint_drepresentationelement viewpoint_drepresentationelement) {
        this.viewpoint_drepresentationelements.add(viewpoint_drepresentationelement);
    }
    public viewpoint_DView getViewpoint_dview() {
        return viewpoint_dview;
    }

    public void setViewpoint_dview(viewpoint_DView viewpoint_dview) {
        this.viewpoint_dview = viewpoint_dview;
    }
    public List<viewpoint_DRepresentationElement> getViewpoint_drepresentationelements() {
        return viewpoint_drepresentationelements;
    }

    public void addViewpoint_drepresentationelement(Viewpoint_drepresentationelement viewpoint_drepresentationelement) {
        this.viewpoint_drepresentationelements.add(viewpoint_drepresentationelement);
    }

}