





import java.util.List;
import java.util.ArrayList;

public class ecore_EGenericType extends EObject {






    private ecore_EClassifier ecore_eclassifier;




    private ecore_EClass ecore_eclass;




    private ecore_EGenericType ecore_egenerictype;




    private ecore_ETypeParameter ecore_etypeparameter;




    private ecore_ETypeParameter ecore_etypeparameter;




    private ecore_EClass ecore_eclass;




    private ecore_ETypedElement ecore_etypedelement;




    private ecore_EOperation ecore_eoperation;




    private List<ecore_EGenericType> ecore_egenerictypes;




    private ecore_EGenericType ecore_egenerictype;




    private ecore_EClassifier ecore_eclassifier;


    public ecore_EGenericType(
    ) {
        super(
        );
        this.ecore_egenerictypes = new ArrayList<>();
    }

    public ecore_EGenericType(
        ArrayList<ecore_EGenericType> ecore_egenerictypes    ) {
        this.ecore_egenerictypes = ecore_egenerictypes;
    }


    public ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }
    public ecore_ETypeParameter getEcore_etypeparameter() {
        return ecore_etypeparameter;
    }

    public void setEcore_etypeparameter(ecore_ETypeParameter ecore_etypeparameter) {
        this.ecore_etypeparameter = ecore_etypeparameter;
    }
    public ecore_ETypeParameter getEcore_etypeparameter() {
        return ecore_etypeparameter;
    }

    public void setEcore_etypeparameter(ecore_ETypeParameter ecore_etypeparameter) {
        this.ecore_etypeparameter = ecore_etypeparameter;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public ecore_ETypedElement getEcore_etypedelement() {
        return ecore_etypedelement;
    }

    public void setEcore_etypedelement(ecore_ETypedElement ecore_etypedelement) {
        this.ecore_etypedelement = ecore_etypedelement;
    }
    public ecore_EOperation getEcore_eoperation() {
        return ecore_eoperation;
    }

    public void setEcore_eoperation(ecore_EOperation ecore_eoperation) {
        this.ecore_eoperation = ecore_eoperation;
    }
    public List<ecore_EGenericType> getEcore_egenerictypes() {
        return ecore_egenerictypes;
    }

    public void addEcore_egenerictype(Ecore_egenerictype ecore_egenerictype) {
        this.ecore_egenerictypes.add(ecore_egenerictype);
    }
    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }
    public ecore_EClassifier getEcore_eclassifier() {
        return ecore_eclassifier;
    }

    public void setEcore_eclassifier(ecore_EClassifier ecore_eclassifier) {
        this.ecore_eclassifier = ecore_eclassifier;
    }

}