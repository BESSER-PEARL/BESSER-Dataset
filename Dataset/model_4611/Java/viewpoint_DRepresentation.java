





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DRepresentation extends DRefreshable, IdentifiedElement, description_DModelElement {

    private String documentation;
    private String name;





    private List<viewpoint_DRepresentationElement> viewpoint_drepresentationelements;




    private List<viewpoint_DRepresentationElement> viewpoint_drepresentationelements;


    public viewpoint_DRepresentation(
        String documentation,        String name    ) {
        super(
        );
        this.documentation = documentation;
        this.name = name;
        this.viewpoint_drepresentationelements = new ArrayList<>();
        this.viewpoint_drepresentationelements = new ArrayList<>();
    }

    public viewpoint_DRepresentation(
        String documentation,        String name        ArrayList<viewpoint_DRepresentationElement> viewpoint_drepresentationelements,        ArrayList<viewpoint_DRepresentationElement> viewpoint_drepresentationelements    ) {
        this.documentation = documentation;
        this.name = name;
        this.viewpoint_drepresentationelements = viewpoint_drepresentationelements;
        this.viewpoint_drepresentationelements = viewpoint_drepresentationelements;
    }

    public String getDocumentation() {
        return documentation;
    }

    public void setDocumentation(String documentation) {
        this.documentation = documentation;
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
    public List<viewpoint_DRepresentationElement> getViewpoint_drepresentationelements() {
        return viewpoint_drepresentationelements;
    }

    public void addViewpoint_drepresentationelement(Viewpoint_drepresentationelement viewpoint_drepresentationelement) {
        this.viewpoint_drepresentationelements.add(viewpoint_drepresentationelement);
    }

}