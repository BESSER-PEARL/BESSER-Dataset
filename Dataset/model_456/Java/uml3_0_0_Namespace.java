





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Namespace extends NamedElement {






    private List<uml3_0_0_NamedElement> uml3_0_0_namedelements;




    private List<uml3_0_0_NamedElement> uml3_0_0_namedelements;




    private List<uml3_0_0_PackageableElement> uml3_0_0_packageableelements;




    private uml3_0_0_NamedElement uml3_0_0_namedelement;




    private uml3_0_0_Constraint uml3_0_0_constraint;




    private List<uml3_0_0_Constraint> uml3_0_0_constraints;


    public uml3_0_0_Namespace(
    ) {
        super(
        );
        this.uml3_0_0_namedelements = new ArrayList<>();
        this.uml3_0_0_namedelements = new ArrayList<>();
        this.uml3_0_0_packageableelements = new ArrayList<>();
        this.uml3_0_0_constraints = new ArrayList<>();
    }

    public uml3_0_0_Namespace(
        ArrayList<uml3_0_0_NamedElement> uml3_0_0_namedelements,        ArrayList<uml3_0_0_NamedElement> uml3_0_0_namedelements,        ArrayList<uml3_0_0_PackageableElement> uml3_0_0_packageableelements,        ArrayList<uml3_0_0_Constraint> uml3_0_0_constraints    ) {
        this.uml3_0_0_namedelements = uml3_0_0_namedelements;
        this.uml3_0_0_namedelements = uml3_0_0_namedelements;
        this.uml3_0_0_packageableelements = uml3_0_0_packageableelements;
        this.uml3_0_0_constraints = uml3_0_0_constraints;
    }


    public List<uml3_0_0_NamedElement> getUml3_0_0_namedelements() {
        return uml3_0_0_namedelements;
    }

    public void addUml3_0_0_namedelement(Uml3_0_0_namedelement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelements.add(uml3_0_0_namedelement);
    }
    public List<uml3_0_0_NamedElement> getUml3_0_0_namedelements() {
        return uml3_0_0_namedelements;
    }

    public void addUml3_0_0_namedelement(Uml3_0_0_namedelement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelements.add(uml3_0_0_namedelement);
    }
    public List<uml3_0_0_PackageableElement> getUml3_0_0_packageableelements() {
        return uml3_0_0_packageableelements;
    }

    public void addUml3_0_0_packageableelement(Uml3_0_0_packageableelement uml3_0_0_packageableelement) {
        this.uml3_0_0_packageableelements.add(uml3_0_0_packageableelement);
    }
    public uml3_0_0_NamedElement getUml3_0_0_namedelement() {
        return uml3_0_0_namedelement;
    }

    public void setUml3_0_0_namedelement(uml3_0_0_NamedElement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelement = uml3_0_0_namedelement;
    }
    public uml3_0_0_Constraint getUml3_0_0_constraint() {
        return uml3_0_0_constraint;
    }

    public void setUml3_0_0_constraint(uml3_0_0_Constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraint = uml3_0_0_constraint;
    }
    public List<uml3_0_0_Constraint> getUml3_0_0_constraints() {
        return uml3_0_0_constraints;
    }

    public void addUml3_0_0_constraint(Uml3_0_0_constraint uml3_0_0_constraint) {
        this.uml3_0_0_constraints.add(uml3_0_0_constraint);
    }

}