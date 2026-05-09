





import java.util.List;
import java.util.ArrayList;

public class ecore_EOperation extends ETypedElement {






    private List<ETypeParameter> etypeparameters;




    private List<EGenericType> egenerictypes;




    private EClass eclass;




    private List<EClassifier> eclassifiers;


    public ecore_EOperation(
    ) {
        super(
        );
        this.etypeparameters = new ArrayList<>();
        this.egenerictypes = new ArrayList<>();
        this.eclassifiers = new ArrayList<>();
    }

    public ecore_EOperation(
        ArrayList<ETypeParameter> etypeparameters,        ArrayList<EGenericType> egenerictypes,        ArrayList<EClassifier> eclassifiers    ) {
        this.etypeparameters = etypeparameters;
        this.egenerictypes = egenerictypes;
        this.eclassifiers = eclassifiers;
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

}