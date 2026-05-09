





import java.util.List;
import java.util.ArrayList;

public class ecore_EOperation extends ETypedElement {






    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;




    private List<ecore_EGenericType> ecore_egenerictypes;




    private ecore_EClass ecore_eclass;


    public ecore_EOperation(
    ) {
        super(
        );
        this.ecore_egenerictypes = new ArrayList<>();
    }

    public ecore_EOperation(
        ArrayList<ecore_EGenericType> ecore_egenerictypes    ) {
        this.ecore_egenerictypes = ecore_egenerictypes;
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

}