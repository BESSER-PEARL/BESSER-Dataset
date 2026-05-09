





import java.util.List;
import java.util.ArrayList;

public class ecoreO_EOperation extends ETypedElement {






    private ecoreO_EClass ecoreo_eclass;




    private ecoreO_EClass ecoreo_eclass;




    private List<ecoreO_EGenericType> ecoreo_egenerictypes;




    private List<ecoreO_EClassifier> ecoreo_eclassifiers;




    private ecoreO_EClass ecoreo_eclass;




    private List<ecoreO_ETypeParameter> ecoreo_etypeparameters;


    public ecoreO_EOperation(
    ) {
        super(
        );
        this.ecoreo_egenerictypes = new ArrayList<>();
        this.ecoreo_eclassifiers = new ArrayList<>();
        this.ecoreo_etypeparameters = new ArrayList<>();
    }

    public ecoreO_EOperation(
        ArrayList<ecoreO_EGenericType> ecoreo_egenerictypes,        ArrayList<ecoreO_EClassifier> ecoreo_eclassifiers,        ArrayList<ecoreO_ETypeParameter> ecoreo_etypeparameters    ) {
        this.ecoreo_egenerictypes = ecoreo_egenerictypes;
        this.ecoreo_eclassifiers = ecoreo_eclassifiers;
        this.ecoreo_etypeparameters = ecoreo_etypeparameters;
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
    public List<ecoreO_EGenericType> getEcoreo_egenerictypes() {
        return ecoreo_egenerictypes;
    }

    public void addEcoreo_egenerictype(Ecoreo_egenerictype ecoreo_egenerictype) {
        this.ecoreo_egenerictypes.add(ecoreo_egenerictype);
    }
    public List<ecoreO_EClassifier> getEcoreo_eclassifiers() {
        return ecoreo_eclassifiers;
    }

    public void addEcoreo_eclassifier(Ecoreo_eclassifier ecoreo_eclassifier) {
        this.ecoreo_eclassifiers.add(ecoreo_eclassifier);
    }
    public ecoreO_EClass getEcoreo_eclass() {
        return ecoreo_eclass;
    }

    public void setEcoreo_eclass(ecoreO_EClass ecoreo_eclass) {
        this.ecoreo_eclass = ecoreo_eclass;
    }
    public List<ecoreO_ETypeParameter> getEcoreo_etypeparameters() {
        return ecoreo_etypeparameters;
    }

    public void addEcoreo_etypeparameter(Ecoreo_etypeparameter ecoreo_etypeparameter) {
        this.ecoreo_etypeparameters.add(ecoreo_etypeparameter);
    }

}