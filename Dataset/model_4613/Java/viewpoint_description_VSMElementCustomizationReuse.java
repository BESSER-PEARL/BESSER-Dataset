





import java.util.List;
import java.util.ArrayList;

public class viewpoint_description_VSMElementCustomizationReuse extends IVSMElementCustomization {






    private List<EStructuralFeatureCustomization> estructuralfeaturecustomizations;




    private List<description_viewpoint_EObject> description_viewpoint_eobjects;


    public viewpoint_description_VSMElementCustomizationReuse(
    ) {
        super(
        );
        this.estructuralfeaturecustomizations = new ArrayList<>();
        this.description_viewpoint_eobjects = new ArrayList<>();
    }

    public viewpoint_description_VSMElementCustomizationReuse(
        ArrayList<EStructuralFeatureCustomization> estructuralfeaturecustomizations,        ArrayList<description_viewpoint_EObject> description_viewpoint_eobjects    ) {
        this.estructuralfeaturecustomizations = estructuralfeaturecustomizations;
        this.description_viewpoint_eobjects = description_viewpoint_eobjects;
    }


    public List<EStructuralFeatureCustomization> getEstructuralfeaturecustomizations() {
        return estructuralfeaturecustomizations;
    }

    public void addEstructuralfeaturecustomization(Estructuralfeaturecustomization estructuralfeaturecustomization) {
        this.estructuralfeaturecustomizations.add(estructuralfeaturecustomization);
    }
    public List<description_viewpoint_EObject> getDescription_viewpoint_eobjects() {
        return description_viewpoint_eobjects;
    }

    public void addDescription_viewpoint_eobject(Description_viewpoint_eobject description_viewpoint_eobject) {
        this.description_viewpoint_eobjects.add(description_viewpoint_eobject);
    }

}