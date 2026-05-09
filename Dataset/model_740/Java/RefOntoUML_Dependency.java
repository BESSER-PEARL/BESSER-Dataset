





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Dependency extends DirectedRelationship, PackageableElement {






    private List<RefOntoUML_NamedElement> refontouml_namedelements;




    private RefOntoUML_NamedElement refontouml_namedelement;




    private List<RefOntoUML_NamedElement> refontouml_namedelements;


    public RefOntoUML_Dependency(
    ) {
        super(
        );
        this.refontouml_namedelements = new ArrayList<>();
        this.refontouml_namedelements = new ArrayList<>();
    }

    public RefOntoUML_Dependency(
        ArrayList<RefOntoUML_NamedElement> refontouml_namedelements,        ArrayList<RefOntoUML_NamedElement> refontouml_namedelements    ) {
        this.refontouml_namedelements = refontouml_namedelements;
        this.refontouml_namedelements = refontouml_namedelements;
    }


    public List<RefOntoUML_NamedElement> getRefontouml_namedelements() {
        return refontouml_namedelements;
    }

    public void addRefontouml_namedelement(Refontouml_namedelement refontouml_namedelement) {
        this.refontouml_namedelements.add(refontouml_namedelement);
    }
    public RefOntoUML_NamedElement getRefontouml_namedelement() {
        return refontouml_namedelement;
    }

    public void setRefontouml_namedelement(RefOntoUML_NamedElement refontouml_namedelement) {
        this.refontouml_namedelement = refontouml_namedelement;
    }
    public List<RefOntoUML_NamedElement> getRefontouml_namedelements() {
        return refontouml_namedelements;
    }

    public void addRefontouml_namedelement(Refontouml_namedelement refontouml_namedelement) {
        this.refontouml_namedelements.add(refontouml_namedelement);
    }

}