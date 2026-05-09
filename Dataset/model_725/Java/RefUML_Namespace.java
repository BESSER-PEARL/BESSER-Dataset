





import java.util.List;
import java.util.ArrayList;

public class RefUML_Namespace extends NamedElement {






    private List<RefUML_Constraintx> refuml_constraintxs;




    private List<RefUML_PackageableElement> refuml_packageableelements;




    private RefUML_NamedElement refuml_namedelement;




    private RefUML_Constraintx refuml_constraintx;




    private List<RefUML_NamedElement> refuml_namedelements;




    private List<RefUML_NamedElement> refuml_namedelements;


    public RefUML_Namespace(
    ) {
        super(
        );
        this.refuml_constraintxs = new ArrayList<>();
        this.refuml_packageableelements = new ArrayList<>();
        this.refuml_namedelements = new ArrayList<>();
        this.refuml_namedelements = new ArrayList<>();
    }

    public RefUML_Namespace(
        ArrayList<RefUML_Constraintx> refuml_constraintxs,        ArrayList<RefUML_PackageableElement> refuml_packageableelements,        ArrayList<RefUML_NamedElement> refuml_namedelements,        ArrayList<RefUML_NamedElement> refuml_namedelements    ) {
        this.refuml_constraintxs = refuml_constraintxs;
        this.refuml_packageableelements = refuml_packageableelements;
        this.refuml_namedelements = refuml_namedelements;
        this.refuml_namedelements = refuml_namedelements;
    }


    public List<RefUML_Constraintx> getRefuml_constraintxs() {
        return refuml_constraintxs;
    }

    public void addRefuml_constraintx(Refuml_constraintx refuml_constraintx) {
        this.refuml_constraintxs.add(refuml_constraintx);
    }
    public List<RefUML_PackageableElement> getRefuml_packageableelements() {
        return refuml_packageableelements;
    }

    public void addRefuml_packageableelement(Refuml_packageableelement refuml_packageableelement) {
        this.refuml_packageableelements.add(refuml_packageableelement);
    }
    public RefUML_NamedElement getRefuml_namedelement() {
        return refuml_namedelement;
    }

    public void setRefuml_namedelement(RefUML_NamedElement refuml_namedelement) {
        this.refuml_namedelement = refuml_namedelement;
    }
    public RefUML_Constraintx getRefuml_constraintx() {
        return refuml_constraintx;
    }

    public void setRefuml_constraintx(RefUML_Constraintx refuml_constraintx) {
        this.refuml_constraintx = refuml_constraintx;
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

}