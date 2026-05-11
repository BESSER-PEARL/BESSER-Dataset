





import java.util.List;
import java.util.ArrayList;

public class cmof_Namespace extends NamedElement {






    private List<cmof_NamedElement> cmof_namedelements;




    private List<cmof_Constraint> cmof_constraints;




    private List<cmof_PackageableElement> cmof_packageableelements;




    private cmof_Constraint cmof_constraint;




    private cmof_Constraint cmof_constraint;


    public cmof_Namespace(
    ) {
        super(
        );
        this.cmof_namedelements = new ArrayList<>();
        this.cmof_constraints = new ArrayList<>();
        this.cmof_packageableelements = new ArrayList<>();
    }

    public cmof_Namespace(
        ArrayList<cmof_NamedElement> cmof_namedelements,        ArrayList<cmof_Constraint> cmof_constraints,        ArrayList<cmof_PackageableElement> cmof_packageableelements    ) {
        this.cmof_namedelements = cmof_namedelements;
        this.cmof_constraints = cmof_constraints;
        this.cmof_packageableelements = cmof_packageableelements;
    }


    public List<cmof_NamedElement> getCmof_namedelements() {
        return cmof_namedelements;
    }

    public void addCmof_namedelement(Cmof_namedelement cmof_namedelement) {
        this.cmof_namedelements.add(cmof_namedelement);
    }
    public List<cmof_Constraint> getCmof_constraints() {
        return cmof_constraints;
    }

    public void addCmof_constraint(Cmof_constraint cmof_constraint) {
        this.cmof_constraints.add(cmof_constraint);
    }
    public List<cmof_PackageableElement> getCmof_packageableelements() {
        return cmof_packageableelements;
    }

    public void addCmof_packageableelement(Cmof_packageableelement cmof_packageableelement) {
        this.cmof_packageableelements.add(cmof_packageableelement);
    }
    public cmof_Constraint getCmof_constraint() {
        return cmof_constraint;
    }

    public void setCmof_constraint(cmof_Constraint cmof_constraint) {
        this.cmof_constraint = cmof_constraint;
    }
    public cmof_Constraint getCmof_constraint() {
        return cmof_constraint;
    }

    public void setCmof_constraint(cmof_Constraint cmof_constraint) {
        this.cmof_constraint = cmof_constraint;
    }

}