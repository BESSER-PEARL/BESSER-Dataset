





import java.util.List;
import java.util.ArrayList;

public class uml_Dependency extends DirectedRelationship, PackageableElement {






    private List<uml_NamedElement> uml_namedelements;


    public uml_Dependency(
    ) {
        super(
        );
        this.uml_namedelements = new ArrayList<>();
    }

    public uml_Dependency(
        ArrayList<uml_NamedElement> uml_namedelements    ) {
        this.uml_namedelements = uml_namedelements;
    }


    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }

}