





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EReference extends EStructuralFeature {

    private boolean resolveProxies;
    private boolean containment;





    private ecoreDiff_EReference ecorediff_ereference;




    private ecoreDiff_ChangedEReference ecorediff_changedereference;


    public ecoreDiff_EReference(
        boolean resolveProxies,        boolean containment    ) {
        super(
        );
        this.resolveProxies = resolveProxies;
        this.containment = containment;
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

    public ecoreDiff_EReference getEcorediff_ereference() {
        return ecorediff_ereference;
    }

    public void setEcorediff_ereference(ecoreDiff_EReference ecorediff_ereference) {
        this.ecorediff_ereference = ecorediff_ereference;
    }
    public ecoreDiff_ChangedEReference getEcorediff_changedereference() {
        return ecorediff_changedereference;
    }

    public void setEcorediff_changedereference(ecoreDiff_ChangedEReference ecorediff_changedereference) {
        this.ecorediff_changedereference = ecorediff_changedereference;
    }

}