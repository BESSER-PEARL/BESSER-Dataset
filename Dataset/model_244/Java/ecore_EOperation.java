





import java.util.List;
import java.util.ArrayList;

public class ecore_EOperation extends ETypedElement {






    private EClass eclass;




    private List<EClassifier> eclassifiers;




    private List<ETypeParameter> etypeparameters;




    private List<EGenericType> egenerictypes;


    public ecore_EOperation(
    ) {
        super(
        );
        this.eclassifiers = new ArrayList<>();
        this.etypeparameters = new ArrayList<>();
        this.egenerictypes = new ArrayList<>();
    }

    public ecore_EOperation(
        ArrayList<EClassifier> eclassifiers,        ArrayList<ETypeParameter> etypeparameters,        ArrayList<EGenericType> egenerictypes    ) {
        this.eclassifiers = eclassifiers;
        this.etypeparameters = etypeparameters;
        this.egenerictypes = egenerictypes;
    }


    public EClass getEclass() {
        return eclass;
    }

    public void setEclass(EClass eclass) {
        this.eclass = eclass;
    }
    public List<EClassifier> getEclassifiers() {
        return eclassifiers;
    }

    public void addEclassifier(Eclassifier eclassifier) {
        this.eclassifiers.add(eclassifier);
    }
    public List<ETypeParameter> getEtypeparameters() {
        return etypeparameters;
    }

    public void addEtypeparameter(Etypeparameter etypeparameter) {
        this.etypeparameters.add(etypeparameter);
    }
    public List<EGenericType> getEgenerictypes() {
        return egenerictypes;
    }

    public void addEgenerictype(Egenerictype egenerictype) {
        this.egenerictypes.add(egenerictype);
    }

}