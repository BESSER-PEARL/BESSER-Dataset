





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EReference extends EStructuralFeature {

    private boolean resolveProxies;
    private boolean containment;
    private boolean container;





    private ecoreDiff_EClass ecorediff_eclass;




    private ecoreDiff_EClass ecorediff_eclass;




    private List<ecoreDiff_EAttribute> ecorediff_eattributes;




    private ecoreDiff_EClass ecorediff_eclass;




    private ecoreDiff_EClass ecorediff_eclass;




    private ecoreDiff_EReference ecorediff_ereference;


    public ecoreDiff_EReference(
        boolean resolveProxies,        boolean containment,        boolean container    ) {
        super(
        );
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.container = container;
        this.ecorediff_eattributes = new ArrayList<>();
    }

    public ecoreDiff_EReference(
        boolean resolveProxies,        boolean containment,        boolean container        ArrayList<ecoreDiff_EAttribute> ecorediff_eattributes    ) {
        this.resolveProxies = resolveProxies;
        this.containment = containment;
        this.container = container;
        this.ecorediff_eattributes = ecorediff_eattributes;
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

    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }
    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }
    public List<ecoreDiff_EAttribute> getEcorediff_eattributes() {
        return ecorediff_eattributes;
    }

    public void addEcorediff_eattribute(Ecorediff_eattribute ecorediff_eattribute) {
        this.ecorediff_eattributes.add(ecorediff_eattribute);
    }
    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }
    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }
    public ecoreDiff_EReference getEcorediff_ereference() {
        return ecorediff_ereference;
    }

    public void setEcorediff_ereference(ecoreDiff_EReference ecorediff_ereference) {
        this.ecorediff_ereference = ecorediff_ereference;
    }

}