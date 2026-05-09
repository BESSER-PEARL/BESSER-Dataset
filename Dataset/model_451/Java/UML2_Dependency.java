





import java.util.List;
import java.util.ArrayList;

public class UML2_Dependency extends PackageableElement, DirectedRelationship {






    private List<UML2_NamedElement> uml2_namedelements;




    private List<UML2_NamedElement> uml2_namedelements;




    private UML2_NamedElement uml2_namedelement;




    private UML2_CollaborationOccurrence uml2_collaborationoccurrence;


    public UML2_Dependency(
    ) {
        super(
        );
        this.uml2_namedelements = new ArrayList<>();
        this.uml2_namedelements = new ArrayList<>();
    }

    public UML2_Dependency(
        ArrayList<UML2_NamedElement> uml2_namedelements,        ArrayList<UML2_NamedElement> uml2_namedelements    ) {
        this.uml2_namedelements = uml2_namedelements;
        this.uml2_namedelements = uml2_namedelements;
    }


    public List<UML2_NamedElement> getUml2_namedelements() {
        return uml2_namedelements;
    }

    public void addUml2_namedelement(Uml2_namedelement uml2_namedelement) {
        this.uml2_namedelements.add(uml2_namedelement);
    }
    public List<UML2_NamedElement> getUml2_namedelements() {
        return uml2_namedelements;
    }

    public void addUml2_namedelement(Uml2_namedelement uml2_namedelement) {
        this.uml2_namedelements.add(uml2_namedelement);
    }
    public UML2_NamedElement getUml2_namedelement() {
        return uml2_namedelement;
    }

    public void setUml2_namedelement(UML2_NamedElement uml2_namedelement) {
        this.uml2_namedelement = uml2_namedelement;
    }
    public UML2_CollaborationOccurrence getUml2_collaborationoccurrence() {
        return uml2_collaborationoccurrence;
    }

    public void setUml2_collaborationoccurrence(UML2_CollaborationOccurrence uml2_collaborationoccurrence) {
        this.uml2_collaborationoccurrence = uml2_collaborationoccurrence;
    }

}