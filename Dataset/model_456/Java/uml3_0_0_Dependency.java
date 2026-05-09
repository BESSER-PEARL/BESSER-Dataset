





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Dependency extends PackageableElement, DirectedRelationship {






    private List<uml3_0_0_NamedElement> uml3_0_0_namedelements;




    private List<uml3_0_0_NamedElement> uml3_0_0_namedelements;




    private uml3_0_0_NamedElement uml3_0_0_namedelement;


    public uml3_0_0_Dependency(
    ) {
        super(
        );
        this.uml3_0_0_namedelements = new ArrayList<>();
        this.uml3_0_0_namedelements = new ArrayList<>();
    }

    public uml3_0_0_Dependency(
        ArrayList<uml3_0_0_NamedElement> uml3_0_0_namedelements,        ArrayList<uml3_0_0_NamedElement> uml3_0_0_namedelements    ) {
        this.uml3_0_0_namedelements = uml3_0_0_namedelements;
        this.uml3_0_0_namedelements = uml3_0_0_namedelements;
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
    public uml3_0_0_NamedElement getUml3_0_0_namedelement() {
        return uml3_0_0_namedelement;
    }

    public void setUml3_0_0_namedelement(uml3_0_0_NamedElement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelement = uml3_0_0_namedelement;
    }

}