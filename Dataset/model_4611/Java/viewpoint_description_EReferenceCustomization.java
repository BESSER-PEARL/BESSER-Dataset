





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_EReferenceCustomization extends EStructuralFeatureCustomization {

    private String referenceName;





    private description_viewpoint_EObject description_viewpoint_eobject;


    public viewpoint_description_EReferenceCustomization(
        String referenceName    ) {
        super(
        );
        this.referenceName = referenceName;
    }


    public String getReferencename() {
        return referenceName;
    }

    public void setReferencename(String referenceName) {
        this.referenceName = referenceName;
    }

    public description_viewpoint_EObject getDescription_viewpoint_eobject() {
        return description_viewpoint_eobject;
    }

    public void setDescription_viewpoint_eobject(description_viewpoint_EObject description_viewpoint_eobject) {
        this.description_viewpoint_eobject = description_viewpoint_eobject;
    }

}