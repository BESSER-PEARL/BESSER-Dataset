





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EGenericType extends EObject {






    private ecoreDiff_ETypeParameter ecorediff_etypeparameter;




    private ecoreDiff_ETypedElement ecorediff_etypedelement;




    private ecoreDiff_EGenericType ecorediff_egenerictype;




    private List<ecoreDiff_EGenericType> ecorediff_egenerictypes;




    private ecoreDiff_EClass ecorediff_eclass;




    private ecoreDiff_EOperation ecorediff_eoperation;




    private ecoreDiff_EClassifier ecorediff_eclassifier;




    private ecoreDiff_ETypeParameter ecorediff_etypeparameter;




    private ecoreDiff_ChangedEGenericType ecorediff_changedegenerictype;




    private ecoreDiff_EGenericType ecorediff_egenerictype;


    public ecoreDiff_EGenericType(
    ) {
        super(
        );
        this.ecorediff_egenerictypes = new ArrayList<>();
    }

    public ecoreDiff_EGenericType(
        ArrayList<ecoreDiff_EGenericType> ecorediff_egenerictypes    ) {
        this.ecorediff_egenerictypes = ecorediff_egenerictypes;
    }


    public ecoreDiff_ETypeParameter getEcorediff_etypeparameter() {
        return ecorediff_etypeparameter;
    }

    public void setEcorediff_etypeparameter(ecoreDiff_ETypeParameter ecorediff_etypeparameter) {
        this.ecorediff_etypeparameter = ecorediff_etypeparameter;
    }
    public ecoreDiff_ETypedElement getEcorediff_etypedelement() {
        return ecorediff_etypedelement;
    }

    public void setEcorediff_etypedelement(ecoreDiff_ETypedElement ecorediff_etypedelement) {
        this.ecorediff_etypedelement = ecorediff_etypedelement;
    }
    public ecoreDiff_EGenericType getEcorediff_egenerictype() {
        return ecorediff_egenerictype;
    }

    public void setEcorediff_egenerictype(ecoreDiff_EGenericType ecorediff_egenerictype) {
        this.ecorediff_egenerictype = ecorediff_egenerictype;
    }
    public List<ecoreDiff_EGenericType> getEcorediff_egenerictypes() {
        return ecorediff_egenerictypes;
    }

    public void addEcorediff_egenerictype(Ecorediff_egenerictype ecorediff_egenerictype) {
        this.ecorediff_egenerictypes.add(ecorediff_egenerictype);
    }
    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }
    public ecoreDiff_EOperation getEcorediff_eoperation() {
        return ecorediff_eoperation;
    }

    public void setEcorediff_eoperation(ecoreDiff_EOperation ecorediff_eoperation) {
        this.ecorediff_eoperation = ecorediff_eoperation;
    }
    public ecoreDiff_EClassifier getEcorediff_eclassifier() {
        return ecorediff_eclassifier;
    }

    public void setEcorediff_eclassifier(ecoreDiff_EClassifier ecorediff_eclassifier) {
        this.ecorediff_eclassifier = ecorediff_eclassifier;
    }
    public ecoreDiff_ETypeParameter getEcorediff_etypeparameter() {
        return ecorediff_etypeparameter;
    }

    public void setEcorediff_etypeparameter(ecoreDiff_ETypeParameter ecorediff_etypeparameter) {
        this.ecorediff_etypeparameter = ecorediff_etypeparameter;
    }
    public ecoreDiff_ChangedEGenericType getEcorediff_changedegenerictype() {
        return ecorediff_changedegenerictype;
    }

    public void setEcorediff_changedegenerictype(ecoreDiff_ChangedEGenericType ecorediff_changedegenerictype) {
        this.ecorediff_changedegenerictype = ecorediff_changedegenerictype;
    }
    public ecoreDiff_EGenericType getEcorediff_egenerictype() {
        return ecorediff_egenerictype;
    }

    public void setEcorediff_egenerictype(ecoreDiff_EGenericType ecorediff_egenerictype) {
        this.ecorediff_egenerictype = ecorediff_egenerictype;
    }

}