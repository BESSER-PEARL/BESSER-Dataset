





import java.util.List;
import java.util.ArrayList;

public class encore_EReference extends EStructuralFeature {

    private boolean containment;
    private boolean resolveProxies;
    private boolean container;





    private encore_EReference encore_ereference;




    private List<encore_EAttribute> encore_eattributes;


    public encore_EReference(
        boolean containment,        boolean resolveProxies,        boolean container    ) {
        super(
        );
        this.containment = containment;
        this.resolveProxies = resolveProxies;
        this.container = container;
        this.encore_eattributes = new ArrayList<>();
    }

    public encore_EReference(
        boolean containment,        boolean resolveProxies,        boolean container        ArrayList<encore_EAttribute> encore_eattributes    ) {
        this.containment = containment;
        this.resolveProxies = resolveProxies;
        this.container = container;
        this.encore_eattributes = encore_eattributes;
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

    public encore_EReference getEncore_ereference() {
        return encore_ereference;
    }

    public void setEncore_ereference(encore_EReference encore_ereference) {
        this.encore_ereference = encore_ereference;
    }
    public List<encore_EAttribute> getEncore_eattributes() {
        return encore_eattributes;
    }

    public void addEncore_eattribute(Encore_eattribute encore_eattribute) {
        this.encore_eattributes.add(encore_eattribute);
    }

}