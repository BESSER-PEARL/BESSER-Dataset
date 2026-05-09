





import java.util.List;
import java.util.ArrayList;

public class ecoreO_EReference extends EStructuralFeature {

    private boolean container;
    private boolean resolveProxies;
    private boolean containment;





    private ecoreO_EClass ecoreo_eclass;




    private ecoreO_EClass ecoreo_eclass;




    private ecoreO_EReference ecoreo_ereference;




    private ecoreO_EClass ecoreo_eclass;




    private ecoreO_EClass ecoreo_eclass;




    private List<ecoreO_EAttribute> ecoreo_eattributes;


    public ecoreO_EReference(
        boolean container,        boolean resolveProxies,        boolean containment    ) {
        super(
        );
        this.container = container;
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.ecoreo_eattributes = new ArrayList<>();
    }

    public ecoreO_EReference(
        boolean container,        boolean resolveProxies,        boolean containment        ArrayList<ecoreO_EAttribute> ecoreo_eattributes    ) {
        this.container = container;
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.ecoreo_eattributes = ecoreo_eattributes;
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

    public ecoreO_EClass getEcoreo_eclass() {
        return ecoreo_eclass;
    }

    public void setEcoreo_eclass(ecoreO_EClass ecoreo_eclass) {
        this.ecoreo_eclass = ecoreo_eclass;
    }
    public ecoreO_EClass getEcoreo_eclass() {
        return ecoreo_eclass;
    }

    public void setEcoreo_eclass(ecoreO_EClass ecoreo_eclass) {
        this.ecoreo_eclass = ecoreo_eclass;
    }
    public ecoreO_EReference getEcoreo_ereference() {
        return ecoreo_ereference;
    }

    public void setEcoreo_ereference(ecoreO_EReference ecoreo_ereference) {
        this.ecoreo_ereference = ecoreo_ereference;
    }
    public ecoreO_EClass getEcoreo_eclass() {
        return ecoreo_eclass;
    }

    public void setEcoreo_eclass(ecoreO_EClass ecoreo_eclass) {
        this.ecoreo_eclass = ecoreo_eclass;
    }
    public ecoreO_EClass getEcoreo_eclass() {
        return ecoreo_eclass;
    }

    public void setEcoreo_eclass(ecoreO_EClass ecoreo_eclass) {
        this.ecoreo_eclass = ecoreo_eclass;
    }
    public List<ecoreO_EAttribute> getEcoreo_eattributes() {
        return ecoreo_eattributes;
    }

    public void addEcoreo_eattribute(Ecoreo_eattribute ecoreo_eattribute) {
        this.ecoreo_eattributes.add(ecoreo_eattribute);
    }

}