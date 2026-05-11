





import java.util.List;
import java.util.ArrayList;

public class umlTrace_uml_TracedNamespace extends TracedNamedElement {






    private List<uml_TracedElementImport> uml_tracedelementimports;




    private List<uml_TracedConstraint> uml_tracedconstraints;




    private List<uml_TracedNamedElement> uml_tracednamedelements;




    private List<uml_TracedNamedElement> uml_tracednamedelements;




    private List<uml_TracedPackageImport> uml_tracedpackageimports;


    public umlTrace_uml_TracedNamespace(
    ) {
        super(
        );
        this.uml_tracedelementimports = new ArrayList<>();
        this.uml_tracedconstraints = new ArrayList<>();
        this.uml_tracednamedelements = new ArrayList<>();
        this.uml_tracednamedelements = new ArrayList<>();
        this.uml_tracedpackageimports = new ArrayList<>();
    }

    public umlTrace_uml_TracedNamespace(
        ArrayList<uml_TracedElementImport> uml_tracedelementimports,        ArrayList<uml_TracedConstraint> uml_tracedconstraints,        ArrayList<uml_TracedNamedElement> uml_tracednamedelements,        ArrayList<uml_TracedNamedElement> uml_tracednamedelements,        ArrayList<uml_TracedPackageImport> uml_tracedpackageimports    ) {
        this.uml_tracedelementimports = uml_tracedelementimports;
        this.uml_tracedconstraints = uml_tracedconstraints;
        this.uml_tracednamedelements = uml_tracednamedelements;
        this.uml_tracednamedelements = uml_tracednamedelements;
        this.uml_tracedpackageimports = uml_tracedpackageimports;
    }


    public List<uml_TracedElementImport> getUml_tracedelementimports() {
        return uml_tracedelementimports;
    }

    public void addUml_tracedelementimport(Uml_tracedelementimport uml_tracedelementimport) {
        this.uml_tracedelementimports.add(uml_tracedelementimport);
    }
    public List<uml_TracedConstraint> getUml_tracedconstraints() {
        return uml_tracedconstraints;
    }

    public void addUml_tracedconstraint(Uml_tracedconstraint uml_tracedconstraint) {
        this.uml_tracedconstraints.add(uml_tracedconstraint);
    }
    public List<uml_TracedNamedElement> getUml_tracednamedelements() {
        return uml_tracednamedelements;
    }

    public void addUml_tracednamedelement(Uml_tracednamedelement uml_tracednamedelement) {
        this.uml_tracednamedelements.add(uml_tracednamedelement);
    }
    public List<uml_TracedNamedElement> getUml_tracednamedelements() {
        return uml_tracednamedelements;
    }

    public void addUml_tracednamedelement(Uml_tracednamedelement uml_tracednamedelement) {
        this.uml_tracednamedelements.add(uml_tracednamedelement);
    }
    public List<uml_TracedPackageImport> getUml_tracedpackageimports() {
        return uml_tracedpackageimports;
    }

    public void addUml_tracedpackageimport(Uml_tracedpackageimport uml_tracedpackageimport) {
        this.uml_tracedpackageimports.add(uml_tracedpackageimport);
    }

}