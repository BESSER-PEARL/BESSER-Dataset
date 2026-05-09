





import java.util.List;
import java.util.ArrayList;

public class RefUML_Dependency extends PackageableElement, DirectedRelationship {






    private List<RefUML_NamedElement> refuml_namedelements;




    private List<RefUML_NamedElement> refuml_namedelements;




    private RefUML_NamedElement refuml_namedelement;


    public RefUML_Dependency(
    ) {
        super(
        );
        this.refuml_namedelements = new ArrayList<>();
        this.refuml_namedelements = new ArrayList<>();
    }

    public RefUML_Dependency(
        ArrayList<RefUML_NamedElement> refuml_namedelements,        ArrayList<RefUML_NamedElement> refuml_namedelements    ) {
        this.refuml_namedelements = refuml_namedelements;
        this.refuml_namedelements = refuml_namedelements;
    }


    public List<RefUML_NamedElement> getRefuml_namedelements() {
        return refuml_namedelements;
    }

    public void addRefuml_namedelement(Refuml_namedelement refuml_namedelement) {
        this.refuml_namedelements.add(refuml_namedelement);
    }
    public List<RefUML_NamedElement> getRefuml_namedelements() {
        return refuml_namedelements;
    }

    public void addRefuml_namedelement(Refuml_namedelement refuml_namedelement) {
        this.refuml_namedelements.add(refuml_namedelement);
    }
    public RefUML_NamedElement getRefuml_namedelement() {
        return refuml_namedelement;
    }

    public void setRefuml_namedelement(RefUML_NamedElement refuml_namedelement) {
        this.refuml_namedelement = refuml_namedelement;
    }

}