





import java.util.List;
import java.util.ArrayList;

public class ecore_EOperation extends ETypedElement {






    private List<ecore_EClassifier> ecore_eclassifiers;




    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;


    public ecore_EOperation(
    ) {
        super(
        );
        this.ecore_eclassifiers = new ArrayList<>();
    }

    public ecore_EOperation(
        ArrayList<ecore_EClassifier> ecore_eclassifiers    ) {
        this.ecore_eclassifiers = ecore_eclassifiers;
    }


    public List<ecore_EClassifier> getEcore_eclassifiers() {
        return ecore_eclassifiers;
    }

    public void addEcore_eclassifier(Ecore_eclassifier ecore_eclassifier) {
        this.ecore_eclassifiers.add(ecore_eclassifier);
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
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }

}