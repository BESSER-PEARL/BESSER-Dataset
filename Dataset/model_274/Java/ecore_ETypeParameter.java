





import java.util.List;
import java.util.ArrayList;

public class ecore_ETypeParameter extends ENamedElement {






    private ecore_EGenericType ecore_egenerictype;




    private List<ecore_EGenericType> ecore_egenerictypes;


    public ecore_ETypeParameter(
    ) {
        super(
        );
        this.ecore_egenerictypes = new ArrayList<>();
    }

    public ecore_ETypeParameter(
        ArrayList<ecore_EGenericType> ecore_egenerictypes    ) {
        this.ecore_egenerictypes = ecore_egenerictypes;
    }


    public ecore_EGenericType getEcore_egenerictype() {
        return ecore_egenerictype;
    }

    public void setEcore_egenerictype(ecore_EGenericType ecore_egenerictype) {
        this.ecore_egenerictype = ecore_egenerictype;
    }
    public List<ecore_EGenericType> getEcore_egenerictypes() {
        return ecore_egenerictypes;
    }

    public void addEcore_egenerictype(Ecore_egenerictype ecore_egenerictype) {
        this.ecore_egenerictypes.add(ecore_egenerictype);
    }

}