





import java.util.List;
import java.util.ArrayList;

public class Ecore_EReference extends EStructuralFeature {

    private boolean container;
    private boolean resolveProxies;
    private boolean containment;





    private List<Ecore_EAttribute> ecore_eattributes;




    private Ecore_EReference ecore_ereference;


    public Ecore_EReference(
        boolean container,        boolean resolveProxies,        boolean containment    ) {
        super(
        );
        this.container = container;
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.ecore_eattributes = new ArrayList<>();
    }

    public Ecore_EReference(
        boolean container,        boolean resolveProxies,        boolean containment        ArrayList<Ecore_EAttribute> ecore_eattributes    ) {
        this.container = container;
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.ecore_eattributes = ecore_eattributes;
    }

    public boolean getContainer() {
        return container;
    }

    public void setContainer(boolean container) {
        this.container = container;
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

    public List<Ecore_EAttribute> getEcore_eattributes() {
        return ecore_eattributes;
    }

    public void addEcore_eattribute(Ecore_eattribute ecore_eattribute) {
        this.ecore_eattributes.add(ecore_eattribute);
    }
    public Ecore_EReference getEcore_ereference() {
        return ecore_ereference;
    }

    public void setEcore_ereference(Ecore_EReference ecore_ereference) {
        this.ecore_ereference = ecore_ereference;
    }

}