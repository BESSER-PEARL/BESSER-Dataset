





import java.util.List;
import java.util.ArrayList;

public class uml_InformationFlow extends DirectedRelationship, PackageableElement {






    private List<uml_NamedElement> uml_namedelements;




    private List<uml_Relationship> uml_relationships;




    private List<uml_NamedElement> uml_namedelements;


    public uml_InformationFlow(
    ) {
        super(
        );
        this.uml_namedelements = new ArrayList<>();
        this.uml_relationships = new ArrayList<>();
        this.uml_namedelements = new ArrayList<>();
    }

    public uml_InformationFlow(
        ArrayList<uml_NamedElement> uml_namedelements,        ArrayList<uml_Relationship> uml_relationships,        ArrayList<uml_NamedElement> uml_namedelements    ) {
        this.uml_namedelements = uml_namedelements;
        this.uml_relationships = uml_relationships;
        this.uml_namedelements = uml_namedelements;
    }


    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }
    public List<uml_Relationship> getUml_relationships() {
        return uml_relationships;
    }

    public void addUml_relationship(Uml_relationship uml_relationship) {
        this.uml_relationships.add(uml_relationship);
    }
    public List<uml_NamedElement> getUml_namedelements() {
        return uml_namedelements;
    }

    public void addUml_namedelement(Uml_namedelement uml_namedelement) {
        this.uml_namedelements.add(uml_namedelement);
    }

}