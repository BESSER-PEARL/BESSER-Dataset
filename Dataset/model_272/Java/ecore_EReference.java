





import java.util.List;
import java.util.ArrayList;

public class ecore_EReference extends EStructuralFeature {

    private boolean containment;
    private boolean resolveProxies;
    private boolean container;





    private ecore_EReference ecore_ereference;




    private List<ecore_EAttribute> ecore_eattributes;


    public ecore_EReference(
        boolean containment,        boolean resolveProxies,        boolean container    ) {
        super(
        );
        this.containment = containment;
        this.resolveProxies = resolveProxies;
        this.container = container;
        this.ecore_eattributes = new ArrayList<>();
    }

    public ecore_EReference(
        boolean containment,        boolean resolveProxies,        boolean container        ArrayList<ecore_EAttribute> ecore_eattributes    ) {
        this.containment = containment;
        this.resolveProxies = resolveProxies;
        this.container = container;
        this.ecore_eattributes = ecore_eattributes;
    }

    public boolean getContainment() {
        return containment;
    }

    public void setContainment(boolean containment) {
        this.containment = containment;
    }
    public boolean getResolveproxies() {
        return resolveProxies;
    }

    public void setResolveproxies(boolean resolveProxies) {
        this.resolveProxies = resolveProxies;
    }
    public boolean getContainer() {
        return container;
    }

    public void setContainer(boolean container) {
        this.container = container;
    }

    public ecore_EReference getEcore_ereference() {
        return ecore_ereference;
    }

    public void setEcore_ereference(ecore_EReference ecore_ereference) {
        this.ecore_ereference = ecore_ereference;
    }
    public List<ecore_EAttribute> getEcore_eattributes() {
        return ecore_eattributes;
    }

    public void addEcore_eattribute(Ecore_eattribute ecore_eattribute) {
        this.ecore_eattributes.add(ecore_eattribute);
    }

}