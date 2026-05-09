





import java.util.List;
import java.util.ArrayList;

public class UML2_Namespace extends NamedElement {






    private List<UML2_PackageImport> uml2_packageimports;




    private UML2_Constraint uml2_constraint;




    private List<UML2_ElementImport> uml2_elementimports;




    private UML2_PackageImport uml2_packageimport;




    private UML2_Constraint uml2_constraint;




    private List<UML2_Constraint> uml2_constraints;




    private UML2_ElementImport uml2_elementimport;


    public UML2_Namespace(
    ) {
        super(
        );
        this.uml2_packageimports = new ArrayList<>();
        this.uml2_elementimports = new ArrayList<>();
        this.uml2_constraints = new ArrayList<>();
    }

    public UML2_Namespace(
        ArrayList<UML2_PackageImport> uml2_packageimports,        ArrayList<UML2_ElementImport> uml2_elementimports,        ArrayList<UML2_Constraint> uml2_constraints    ) {
        this.uml2_packageimports = uml2_packageimports;
        this.uml2_elementimports = uml2_elementimports;
        this.uml2_constraints = uml2_constraints;
    }


    public List<UML2_PackageImport> getUml2_packageimports() {
        return uml2_packageimports;
    }

    public void addUml2_packageimport(Uml2_packageimport uml2_packageimport) {
        this.uml2_packageimports.add(uml2_packageimport);
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }
    public List<UML2_ElementImport> getUml2_elementimports() {
        return uml2_elementimports;
    }

    public void addUml2_elementimport(Uml2_elementimport uml2_elementimport) {
        this.uml2_elementimports.add(uml2_elementimport);
    }
    public UML2_PackageImport getUml2_packageimport() {
        return uml2_packageimport;
    }

    public void setUml2_packageimport(UML2_PackageImport uml2_packageimport) {
        this.uml2_packageimport = uml2_packageimport;
    }
    public UML2_Constraint getUml2_constraint() {
        return uml2_constraint;
    }

    public void setUml2_constraint(UML2_Constraint uml2_constraint) {
        this.uml2_constraint = uml2_constraint;
    }
    public List<UML2_Constraint> getUml2_constraints() {
        return uml2_constraints;
    }

    public void addUml2_constraint(Uml2_constraint uml2_constraint) {
        this.uml2_constraints.add(uml2_constraint);
    }
    public UML2_ElementImport getUml2_elementimport() {
        return uml2_elementimport;
    }

    public void setUml2_elementimport(UML2_ElementImport uml2_elementimport) {
        this.uml2_elementimport = uml2_elementimport;
    }

}