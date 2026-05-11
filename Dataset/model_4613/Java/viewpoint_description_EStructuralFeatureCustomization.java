





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_EStructuralFeatureCustomization  {

    private boolean applyOnAll;





    private List<description_viewpoint_EObject> description_viewpoint_eobjects;


    public viewpoint_description_EStructuralFeatureCustomization(
        boolean applyOnAll    ) {
        this.applyOnAll = applyOnAll;
        this.description_viewpoint_eobjects = new ArrayList<>();
    }

    public viewpoint_description_EStructuralFeatureCustomization(
        boolean applyOnAll        ArrayList<description_viewpoint_EObject> description_viewpoint_eobjects    ) {
        this.applyOnAll = applyOnAll;
        this.description_viewpoint_eobjects = description_viewpoint_eobjects;
    }

    public boolean getApplyonall() {
        return applyOnAll;
    }

    public void setApplyonall(boolean applyOnAll) {
        this.applyOnAll = applyOnAll;
    }

    public List<description_viewpoint_EObject> getDescription_viewpoint_eobjects() {
        return description_viewpoint_eobjects;
    }

    public void addDescription_viewpoint_eobject(Description_viewpoint_eobject description_viewpoint_eobject) {
        this.description_viewpoint_eobjects.add(description_viewpoint_eobject);
    }

}