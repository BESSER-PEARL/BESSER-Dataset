





import java.util.List;
import java.util.ArrayList;

public class RefOntoUML_Namespace extends NamedElement {






    private List<RefOntoUML_NamedElement> refontouml_namedelements;




    private RefOntoUML_Constraintx refontouml_constraintx;




    private RefOntoUML_NamedElement refontouml_namedelement;




    private List<RefOntoUML_Constraintx> refontouml_constraintxs;




    private List<RefOntoUML_NamedElement> refontouml_namedelements;


    public RefOntoUML_Namespace(
    ) {
        super(
        );
        this.refontouml_namedelements = new ArrayList<>();
        this.refontouml_constraintxs = new ArrayList<>();
        this.refontouml_namedelements = new ArrayList<>();
    }

    public RefOntoUML_Namespace(
        ArrayList<RefOntoUML_NamedElement> refontouml_namedelements,        ArrayList<RefOntoUML_Constraintx> refontouml_constraintxs,        ArrayList<RefOntoUML_NamedElement> refontouml_namedelements    ) {
        this.refontouml_namedelements = refontouml_namedelements;
        this.refontouml_constraintxs = refontouml_constraintxs;
        this.refontouml_namedelements = refontouml_namedelements;
    }


    public List<RefOntoUML_NamedElement> getRefontouml_namedelements() {
        return refontouml_namedelements;
    }

    public void addRefontouml_namedelement(Refontouml_namedelement refontouml_namedelement) {
        this.refontouml_namedelements.add(refontouml_namedelement);
    }
    public RefOntoUML_Constraintx getRefontouml_constraintx() {
        return refontouml_constraintx;
    }

    public void setRefontouml_constraintx(RefOntoUML_Constraintx refontouml_constraintx) {
        this.refontouml_constraintx = refontouml_constraintx;
    }
    public RefOntoUML_NamedElement getRefontouml_namedelement() {
        return refontouml_namedelement;
    }

    public void setRefontouml_namedelement(RefOntoUML_NamedElement refontouml_namedelement) {
        this.refontouml_namedelement = refontouml_namedelement;
    }
    public List<RefOntoUML_Constraintx> getRefontouml_constraintxs() {
        return refontouml_constraintxs;
    }

    public void addRefontouml_constraintx(Refontouml_constraintx refontouml_constraintx) {
        this.refontouml_constraintxs.add(refontouml_constraintx);
    }
    public List<RefOntoUML_NamedElement> getRefontouml_namedelements() {
        return refontouml_namedelements;
    }

    public void addRefontouml_namedelement(Refontouml_namedelement refontouml_namedelement) {
        this.refontouml_namedelements.add(refontouml_namedelement);
    }

}