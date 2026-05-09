





import java.util.List;
import java.util.ArrayList;

public class ecore_EReference extends EStructuralFeature {

    private boolean container;
    private boolean containment;
    private boolean resolveProxies;





    private ecore_EReference ecore_ereference;


    public ecore_EReference(
        boolean container,        boolean containment,        boolean resolveProxies    ) {
        super(
        );
        this.container = container;
        this.containment = containment;
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
    public boolean getResolveproxies() {
        return resolveProxies;
    }

    public void setResolveproxies(boolean resolveProxies) {
        this.resolveProxies = resolveProxies;
    }

    public ecore_EReference getEcore_ereference() {
        return ecore_ereference;
    }

    public void setEcore_ereference(ecore_EReference ecore_ereference) {
        this.ecore_ereference = ecore_ereference;
    }

}