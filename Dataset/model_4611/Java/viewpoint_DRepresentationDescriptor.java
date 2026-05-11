





import java.util.List;
import java.util.ArrayList;

public class viewpoint_DRepresentationDescriptor extends IdentifiedElement, description_DModelElement, description_DocumentedElement {

    private String name;
    private String repPath;
    private String changeId;





    private viewpoint_DRepresentation viewpoint_drepresentation;




    private viewpoint_DView viewpoint_dview;


    public viewpoint_DRepresentationDescriptor(
        String name,        String repPath,        String changeId    ) {
        super(
        );
        this.name = name;
        this.repPath = repPath;
        this.changeId = changeId;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReppath() {
        return repPath;
    }

    public void setReppath(String repPath) {
        this.repPath = repPath;
    }
    public String getChangeid() {
        return changeId;
    }

    public void setChangeid(String changeId) {
        this.changeId = changeId;
    }

    public viewpoint_DRepresentation getViewpoint_drepresentation() {
        return viewpoint_drepresentation;
    }

    public void setViewpoint_drepresentation(viewpoint_DRepresentation viewpoint_drepresentation) {
        this.viewpoint_drepresentation = viewpoint_drepresentation;
    }
    public viewpoint_DView getViewpoint_dview() {
        return viewpoint_dview;
    }

    public void setViewpoint_dview(viewpoint_DView viewpoint_dview) {
        this.viewpoint_dview = viewpoint_dview;
    }

}