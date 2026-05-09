





import java.util.List;
import java.util.ArrayList;

public class ecorer_EReference extends EStructuralFeature {

    private boolean containment;
    private boolean container;
    private boolean resolveProxies;





    private ecorer_EReference ecorer_ereference;




    private List<ecorer_EAttribute> ecorer_eattributes;


    public ecorer_EReference(
        boolean containment,        boolean container,        boolean resolveProxies    ) {
        super(
        );
        this.containment = containment;
        this.container = container;
        this.resolveProxies = resolveProxies;
        this.ecorer_eattributes = new ArrayList<>();
    }

    public ecorer_EReference(
        boolean containment,        boolean container,        boolean resolveProxies        ArrayList<ecorer_EAttribute> ecorer_eattributes    ) {
        this.containment = containment;
        this.container = container;
        this.resolveProxies = resolveProxies;
        this.ecorer_eattributes = ecorer_eattributes;
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
    public boolean getResolveproxies() {
        return resolveProxies;
    }

    public void setResolveproxies(boolean resolveProxies) {
        this.resolveProxies = resolveProxies;
    }

    public ecorer_EReference getEcorer_ereference() {
        return ecorer_ereference;
    }

    public void setEcorer_ereference(ecorer_EReference ecorer_ereference) {
        this.ecorer_ereference = ecorer_ereference;
    }
    public List<ecorer_EAttribute> getEcorer_eattributes() {
        return ecorer_eattributes;
    }

    public void addEcorer_eattribute(Ecorer_eattribute ecorer_eattribute) {
        this.ecorer_eattributes.add(ecorer_eattribute);
    }

}