





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EClass extends EClassifier {

    private boolean interface;
    private boolean abstract;





    private RefinementsEcore_EAttribute refinementsecore_eattribute;




    private RefinementsEcore_EReference refinementsecore_ereference;




    private List<RefinementsEcore_EStructuralFeature> refinementsecore_estructuralfeatures;




    private List<RefinementsEcore_EAttribute> refinementsecore_eattributes;




    private RefinementsEcore_EStructuralFeature refinementsecore_estructuralfeature;




    private List<RefinementsEcore_EClass> refinementsecore_eclasss;




    private List<RefinementsEcore_EReference> refinementsecore_ereferences;


    public RefinementsEcore_EClass(
        boolean interface,        boolean abstract    ) {
        super(
        );
        this.interface = interface;
        this.abstract = abstract;
        this.refinementsecore_estructuralfeatures = new ArrayList<>();
        this.refinementsecore_eattributes = new ArrayList<>();
        this.refinementsecore_eclasss = new ArrayList<>();
        this.refinementsecore_ereferences = new ArrayList<>();
    }

    public RefinementsEcore_EClass(
        boolean interface,        boolean abstract        ArrayList<RefinementsEcore_EStructuralFeature> refinementsecore_estructuralfeatures,        ArrayList<RefinementsEcore_EAttribute> refinementsecore_eattributes,        ArrayList<RefinementsEcore_EClass> refinementsecore_eclasss,        ArrayList<RefinementsEcore_EReference> refinementsecore_ereferences    ) {
        this.interface = interface;
        this.abstract = abstract;
        this.refinementsecore_estructuralfeatures = refinementsecore_estructuralfeatures;
        this.refinementsecore_eattributes = refinementsecore_eattributes;
        this.refinementsecore_eclasss = refinementsecore_eclasss;
        this.refinementsecore_ereferences = refinementsecore_ereferences;
    }

    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }

    public RefinementsEcore_EAttribute getRefinementsecore_eattribute() {
        return refinementsecore_eattribute;
    }

    public void setRefinementsecore_eattribute(RefinementsEcore_EAttribute refinementsecore_eattribute) {
        this.refinementsecore_eattribute = refinementsecore_eattribute;
    }
    public RefinementsEcore_EReference getRefinementsecore_ereference() {
        return refinementsecore_ereference;
    }

    public void setRefinementsecore_ereference(RefinementsEcore_EReference refinementsecore_ereference) {
        this.refinementsecore_ereference = refinementsecore_ereference;
    }
    public List<RefinementsEcore_EStructuralFeature> getRefinementsecore_estructuralfeatures() {
        return refinementsecore_estructuralfeatures;
    }

    public void addRefinementsecore_estructuralfeature(Refinementsecore_estructuralfeature refinementsecore_estructuralfeature) {
        this.refinementsecore_estructuralfeatures.add(refinementsecore_estructuralfeature);
    }
    public List<RefinementsEcore_EAttribute> getRefinementsecore_eattributes() {
        return refinementsecore_eattributes;
    }

    public void addRefinementsecore_eattribute(Refinementsecore_eattribute refinementsecore_eattribute) {
        this.refinementsecore_eattributes.add(refinementsecore_eattribute);
    }
    public RefinementsEcore_EStructuralFeature getRefinementsecore_estructuralfeature() {
        return refinementsecore_estructuralfeature;
    }

    public void setRefinementsecore_estructuralfeature(RefinementsEcore_EStructuralFeature refinementsecore_estructuralfeature) {
        this.refinementsecore_estructuralfeature = refinementsecore_estructuralfeature;
    }
    public List<RefinementsEcore_EClass> getRefinementsecore_eclasss() {
        return refinementsecore_eclasss;
    }

    public void addRefinementsecore_eclass(Refinementsecore_eclass refinementsecore_eclass) {
        this.refinementsecore_eclasss.add(refinementsecore_eclass);
    }
    public List<RefinementsEcore_EReference> getRefinementsecore_ereferences() {
        return refinementsecore_ereferences;
    }

    public void addRefinementsecore_ereference(Refinementsecore_ereference refinementsecore_ereference) {
        this.refinementsecore_ereferences.add(refinementsecore_ereference);
    }

}