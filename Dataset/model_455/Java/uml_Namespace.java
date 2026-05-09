





import java.util.List;
import java.util.ArrayList;

public class uml_Namespace extends NamedElement {






    private List<uml_PackageableElement> uml_packageableelements;




    private List<uml_Constraint> uml_constraints;




    private uml_PackageImport uml_packageimport;




    private uml_Constraint uml_constraint;




    private List<uml_ElementImport> uml_elementimports;




    private uml_ElementImport uml_elementimport;




    private uml_NamedElement uml_namedelement;




    private List<uml_PackageImport> uml_packageimports;




    private List<uml_NamedElement> uml_namedelements;




    private List<uml_NamedElement> uml_namedelements;


    public uml_Namespace(
    ) {
        super(
        );
        this.uml_packageableelements = new ArrayList<>();
        this.uml_constraints = new ArrayList<>();
        this.uml_elementimports = new ArrayList<>();
        this.uml_packageimports = new ArrayList<>();
        this.uml_namedelements = new ArrayList<>();
        this.uml_namedelements = new ArrayList<>();
    }

    public uml_Namespace(
        ArrayList<uml_PackageableElement> uml_packageableelements,        ArrayList<uml_Constraint> uml_constraints,        ArrayList<uml_ElementImport> uml_elementimports,        ArrayList<uml_PackageImport> uml_packageimports,        ArrayList<uml_NamedElement> uml_namedelements,        ArrayList<uml_NamedElement> uml_namedelements    ) {
        this.uml_packageableelements = uml_packageableelements;
        this.uml_constraints = uml_constraints;
        this.uml_elementimports = uml_elementimports;
        this.uml_packageimports = uml_packageimports;
        this.uml_namedelements = uml_namedelements;
        this.uml_namedelements = uml_namedelements;
    }


    public List<uml_PackageableElement> getUml_packageableelements() {
        return uml_packageableelements;
    }

    public void addUml_packageableelement(Uml_packageableelement uml_packageableelement) {
        this.uml_packageableelements.add(uml_packageableelement);
    }
    public List<uml_Constraint> getUml_constraints() {
        return uml_constraints;
    }

    public void addUml_constraint(Uml_constraint uml_constraint) {
        this.uml_constraints.add(uml_constraint);
    }
    public uml_PackageImport getUml_packageimport() {
        return uml_packageimport;
    }

    public void setUml_packageimport(uml_PackageImport uml_packageimport) {
        this.uml_packageimport = uml_packageimport;
    }
    public uml_Constraint getUml_constraint() {
        return uml_constraint;
    }

    public void setUml_constraint(uml_Constraint uml_constraint) {
        this.uml_constraint = uml_constraint;
    }
    public List<uml_ElementImport> getUml_elementimports() {
        return uml_elementimports;
    }

    public void addUml_elementimport(Uml_elementimport uml_elementimport) {
        this.uml_elementimports.add(uml_elementimport);
    }
    public uml_ElementImport getUml_elementimport() {
        return uml_elementimport;
    }

    public void setUml_elementimport(uml_ElementImport uml_elementimport) {
        this.uml_elementimport = uml_elementimport;
    }
    public uml_NamedElement getUml_namedelement() {
        return uml_namedelement;
    }

    public void setUml_namedelement(uml_NamedElement uml_namedelement) {
        this.uml_namedelement = uml_namedelement;
    }
    public List<uml_PackageImport> getUml_packageimports() {
        return uml_packageimports;
    }

    public void addUml_packageimport(Uml_packageimport uml_packageimport) {
        this.uml_packageimports.add(uml_packageimport);
    }
    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }
    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }

}