





import java.util.List;
import java.util.ArrayList;

public class ecore_EGenericType  {






    private List<EGenericType> egenerictypes;




    private EGenericType egenerictype;




    private EClassifier eclassifier;




    private EGenericType egenerictype;




    private ETypeParameter etypeparameter;




    private EClassifier eclassifier;


    public ecore_EGenericType(
    ) {
        this.egenerictypes = new ArrayList<>();
    }

    public ecore_EGenericType(
        ArrayList<EGenericType> egenerictypes    ) {
        this.egenerictypes = egenerictypes;
    }


    public List<EGenericType> getEgenerictypes() {
        return egenerictypes;
    }

    public void addEgenerictype(Egenerictype egenerictype) {
        this.egenerictypes.add(egenerictype);
    }
    public EGenericType getEgenerictype() {
        return egenerictype;
    }

    public void setEgenerictype(EGenericType egenerictype) {
        this.egenerictype = egenerictype;
    }
    public EClassifier getEclassifier() {
        return eclassifier;
    }

    public void setEclassifier(EClassifier eclassifier) {
        this.eclassifier = eclassifier;
    }
    public EGenericType getEgenerictype() {
        return egenerictype;
    }

    public void setEgenerictype(EGenericType egenerictype) {
        this.egenerictype = egenerictype;
    }
    public ETypeParameter getEtypeparameter() {
        return etypeparameter;
    }

    public void setEtypeparameter(ETypeParameter etypeparameter) {
        this.etypeparameter = etypeparameter;
    }
    public EClassifier getEclassifier() {
        return eclassifier;
    }

    public void setEclassifier(EClassifier eclassifier) {
        this.eclassifier = eclassifier;
    }

}