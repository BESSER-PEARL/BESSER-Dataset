





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DRepresentation extends description_DModelElement, DRefreshable, description_DocumentedElement {

    private String name;





    private viewpoint_DRepresentationDescriptor viewpoint_drepresentationdescriptor;


    public viewpoint_DRepresentation(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public viewpoint_DRepresentationDescriptor getViewpoint_drepresentationdescriptor() {
        return viewpoint_drepresentationdescriptor;
    }

    public void setViewpoint_drepresentationdescriptor(viewpoint_DRepresentationDescriptor viewpoint_drepresentationdescriptor) {
        this.viewpoint_drepresentationdescriptor = viewpoint_drepresentationdescriptor;
    }

}