





import java.util.List;
import java.util.ArrayList;

public class Ecore_EOperation extends ETypedElement {






    private List<Ecore_EClassifier> ecore_eclassifiers;




    private Ecore_EClass ecore_eclass;




    private Ecore_EClass ecore_eclass;




    private Ecore_EClass ecore_eclass;


    public Ecore_EOperation(
    ) {
        super(
        );
        this.ecore_eclassifiers = new ArrayList<>();
    }

    public Ecore_EOperation(
        ArrayList<Ecore_EClassifier> ecore_eclassifiers    ) {
        this.ecore_eclassifiers = ecore_eclassifiers;
    }


    public List<Ecore_EClassifier> getEcore_eclassifiers() {
        return ecore_eclassifiers;
    }

    public void addEcore_eclassifier(Ecore_eclassifier ecore_eclassifier) {
        this.ecore_eclassifiers.add(ecore_eclassifier);
    }
    public Ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(Ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public Ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(Ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public Ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(Ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }

}