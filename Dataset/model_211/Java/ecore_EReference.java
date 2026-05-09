





import java.util.List;
import java.util.ArrayList;

public class ecore_EReference extends EStructuralFeature {

    private boolean resolveProxies;
    private boolean container;
    private boolean containment;





    private ecore_EReference ecore_ereference;




    private ecore_EClass ecore_eclass;




    private List<ecore_EAttribute> ecore_eattributes;




    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;


    public ecore_EReference(
        boolean resolveProxies,        boolean container,        boolean containment    ) {
        super(
        );
        this.resolveProxies = resolveProxies;
        this.container = container;
        this.containment = containment;
        this.ecore_eattributes = new ArrayList<>();
    }

    public ecore_EReference(
        boolean resolveProxies,        boolean container,        boolean containment        ArrayList<ecore_EAttribute> ecore_eattributes    ) {
        this.resolveProxies = resolveProxies;
        this.container = container;
        this.containment = containment;
        this.ecore_eattributes = ecore_eattributes;
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
    public boolean getContainment() {
        return containment;
    }

    public void setContainment(boolean containment) {
        this.containment = containment;
    }

    public ecore_EReference getEcore_ereference() {
        return ecore_ereference;
    }

    public void setEcore_ereference(ecore_EReference ecore_ereference) {
        this.ecore_ereference = ecore_ereference;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public List<ecore_EAttribute> getEcore_eattributes() {
        return ecore_eattributes;
    }

    public void addEcore_eattribute(Ecore_eattribute ecore_eattribute) {
        this.ecore_eattributes.add(ecore_eattribute);
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }

}