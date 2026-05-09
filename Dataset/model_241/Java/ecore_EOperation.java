





import java.util.List;
import java.util.ArrayList;

public class ecore_EOperation extends ETypedElement {






    private List<ecore_EClassifier> ecore_eclassifiers;




    private List<ecore_EGenericType> ecore_egenerictypes;




    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;




    private List<ecore_ETypeParameter> ecore_etypeparameters;




    private ecore_EClass ecore_eclass;


    public ecore_EOperation(
    ) {
        super(
        );
        this.ecore_eclassifiers = new ArrayList<>();
        this.ecore_egenerictypes = new ArrayList<>();
        this.ecore_etypeparameters = new ArrayList<>();
    }

    public ecore_EOperation(
        ArrayList<ecore_EClassifier> ecore_eclassifiers,        ArrayList<ecore_EGenericType> ecore_egenerictypes,        ArrayList<ecore_ETypeParameter> ecore_etypeparameters    ) {
        this.ecore_eclassifiers = ecore_eclassifiers;
        this.ecore_egenerictypes = ecore_egenerictypes;
        this.ecore_etypeparameters = ecore_etypeparameters;
    }


    public List<ecore_EClassifier> getEcore_eclassifiers() {
        return ecore_eclassifiers;
    }

    public void addEcore_eclassifier(Ecore_eclassifier ecore_eclassifier) {
        this.ecore_eclassifiers.add(ecore_eclassifier);
    }
    public List<ecore_EGenericType> getEcore_egenerictypes() {
        return ecore_egenerictypes;
    }

    public void addEcore_egenerictype(Ecore_egenerictype ecore_egenerictype) {
        this.ecore_egenerictypes.add(ecore_egenerictype);
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
    public List<ecore_ETypeParameter> getEcore_etypeparameters() {
        return ecore_etypeparameters;
    }

    public void addEcore_etypeparameter(Ecore_etypeparameter ecore_etypeparameter) {
        this.ecore_etypeparameters.add(ecore_etypeparameter);
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }

}