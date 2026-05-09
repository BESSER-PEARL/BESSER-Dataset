





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Namespace extends NamedElement, Element {






    private List<UML2WithID_NamedElement> uml2withid_namedelements;


    public UML2WithID_Namespace(
    ) {
        super(
        );
        this.uml2withid_namedelements = new ArrayList<>();
    }

    public UML2WithID_Namespace(
        ArrayList<UML2WithID_NamedElement> uml2withid_namedelements    ) {
        this.uml2withid_namedelements = uml2withid_namedelements;
    }


    public List<UML2WithID_NamedElement> getUml2withid_namedelements() {
        return uml2withid_namedelements;
    }

    public void addUml2withid_namedelement(Uml2withid_namedelement uml2withid_namedelement) {
        this.uml2withid_namedelements.add(uml2withid_namedelement);
    }

}