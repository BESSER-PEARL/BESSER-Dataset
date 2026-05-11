





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EReference extends EStructuralFeature {

    private boolean resolveProxies;
    private boolean containment;
    private boolean container;





    private List<RefinementsEcore_EAttribute> refinementsecore_eattributes;




    private RefinementsEcore_EReference refinementsecore_ereference;




    private RefinementsEcore_EReference refinementsecore_ereference;


    public RefinementsEcore_EReference(
        boolean resolveProxies,        boolean containment,        boolean container    ) {
        super(
        );
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.container = container;
        this.refinementsecore_eattributes = new ArrayList<>();
    }

    public RefinementsEcore_EReference(
        boolean resolveProxies,        boolean containment,        boolean container        ArrayList<RefinementsEcore_EAttribute> refinementsecore_eattributes    ) {
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.container = container;
        this.refinementsecore_eattributes = refinementsecore_eattributes;
    }

    public boolean getResolveproxies() {
        return resolveProxies;
    }

    public void setResolveproxies(boolean resolveProxies) {
        this.resolveProxies = resolveProxies;
    }
    public boolean getContainment() {
        return containment;
    }

    public void setContainment(boolean containment) {
        this.containment = containment;
    }
    public boolean getContainer() {
        return container;
    }

    public void setContainer(boolean container) {
        this.container = container;
    }

    public List<RefinementsEcore_EAttribute> getRefinementsecore_eattributes() {
        return refinementsecore_eattributes;
    }

    public void addRefinementsecore_eattribute(Refinementsecore_eattribute refinementsecore_eattribute) {
        this.refinementsecore_eattributes.add(refinementsecore_eattribute);
    }
    public RefinementsEcore_EReference getRefinementsecore_ereference() {
        return refinementsecore_ereference;
    }

    public void setRefinementsecore_ereference(RefinementsEcore_EReference refinementsecore_ereference) {
        this.refinementsecore_ereference = refinementsecore_ereference;
    }
    public RefinementsEcore_EReference getRefinementsecore_ereference() {
        return refinementsecore_ereference;
    }

    public void setRefinementsecore_ereference(RefinementsEcore_EReference refinementsecore_ereference) {
        this.refinementsecore_ereference = refinementsecore_ereference;
    }

}