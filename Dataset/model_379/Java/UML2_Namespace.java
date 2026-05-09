





import java.util.List;
import java.util.ArrayList;

public class UML2_Namespace extends NamedElement {






    private List<UML2_NamedElement> uml2_namedelements;


    public UML2_Namespace(
    ) {
        super(
        );
        this.uml2_namedelements = new ArrayList<>();
    }

    public UML2_Namespace(
        ArrayList<UML2_NamedElement> uml2_namedelements    ) {
        this.uml2_namedelements = uml2_namedelements;
    }


    public List<UML2_NamedElement> getUml2_namedelements() {
        return uml2_namedelements;
    }

    public void addUml2_namedelement(Uml2_namedelement uml2_namedelement) {
        this.uml2_namedelements.add(uml2_namedelement);
    }

}