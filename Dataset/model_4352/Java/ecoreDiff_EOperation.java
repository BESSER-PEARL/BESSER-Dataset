





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EOperation extends ETypedElement {






    private List<ecoreDiff_ETypeParameter> ecorediff_etypeparameters;




    private ecoreDiff_ChangedEOperation ecorediff_changedeoperation;




    private List<ecoreDiff_EClassifier> ecorediff_eclassifiers;




    private ecoreDiff_EObject ecorediff_eobject;




    private ecoreDiff_EClass ecorediff_eclass;


    public ecoreDiff_EOperation(
    ) {
        super(
        );
        this.ecorediff_etypeparameters = new ArrayList<>();
        this.ecorediff_eclassifiers = new ArrayList<>();
    }

    public ecoreDiff_EOperation(
        ArrayList<ecoreDiff_ETypeParameter> ecorediff_etypeparameters,        ArrayList<ecoreDiff_EClassifier> ecorediff_eclassifiers    ) {
        this.ecorediff_etypeparameters = ecorediff_etypeparameters;
        this.ecorediff_eclassifiers = ecorediff_eclassifiers;
    }


    public List<ecoreDiff_ETypeParameter> getEcorediff_etypeparameters() {
        return ecorediff_etypeparameters;
    }

    public void addEcorediff_etypeparameter(Ecorediff_etypeparameter ecorediff_etypeparameter) {
        this.ecorediff_etypeparameters.add(ecorediff_etypeparameter);
    }
    public ecoreDiff_ChangedEOperation getEcorediff_changedeoperation() {
        return ecorediff_changedeoperation;
    }

    public void setEcorediff_changedeoperation(ecoreDiff_ChangedEOperation ecorediff_changedeoperation) {
        this.ecorediff_changedeoperation = ecorediff_changedeoperation;
    }
    public List<ecoreDiff_EClassifier> getEcorediff_eclassifiers() {
        return ecorediff_eclassifiers;
    }

    public void addEcorediff_eclassifier(Ecorediff_eclassifier ecorediff_eclassifier) {
        this.ecorediff_eclassifiers.add(ecorediff_eclassifier);
    }
    public ecoreDiff_EObject getEcorediff_eobject() {
        return ecorediff_eobject;
    }

    public void setEcorediff_eobject(ecoreDiff_EObject ecorediff_eobject) {
        this.ecorediff_eobject = ecorediff_eobject;
    }
    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }

}