





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_InformationFlow extends PackageableElement, DirectedRelationship {






    private List<uml3_0_0_Classifier> uml3_0_0_classifiers;




    private List<uml3_0_0_NamedElement> uml3_0_0_namedelements;




    private List<uml3_0_0_Relationship> uml3_0_0_relationships;




    private List<uml3_0_0_NamedElement> uml3_0_0_namedelements;


    public uml3_0_0_InformationFlow(
    ) {
        super(
        );
        this.uml3_0_0_classifiers = new ArrayList<>();
        this.uml3_0_0_namedelements = new ArrayList<>();
        this.uml3_0_0_relationships = new ArrayList<>();
        this.uml3_0_0_namedelements = new ArrayList<>();
    }

    public uml3_0_0_InformationFlow(
        ArrayList<uml3_0_0_Classifier> uml3_0_0_classifiers,        ArrayList<uml3_0_0_NamedElement> uml3_0_0_namedelements,        ArrayList<uml3_0_0_Relationship> uml3_0_0_relationships,        ArrayList<uml3_0_0_NamedElement> uml3_0_0_namedelements    ) {
        this.uml3_0_0_classifiers = uml3_0_0_classifiers;
        this.uml3_0_0_namedelements = uml3_0_0_namedelements;
        this.uml3_0_0_relationships = uml3_0_0_relationships;
        this.uml3_0_0_namedelements = uml3_0_0_namedelements;
    }


    public List<uml3_0_0_Classifier> getUml3_0_0_classifiers() {
        return uml3_0_0_classifiers;
    }

    public void addUml3_0_0_classifier(Uml3_0_0_classifier uml3_0_0_classifier) {
        this.uml3_0_0_classifiers.add(uml3_0_0_classifier);
    }
    public List<uml3_0_0_NamedElement> getUml3_0_0_namedelements() {
        return uml3_0_0_namedelements;
    }

    public void addUml3_0_0_namedelement(Uml3_0_0_namedelement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelements.add(uml3_0_0_namedelement);
    }
    public List<uml3_0_0_Relationship> getUml3_0_0_relationships() {
        return uml3_0_0_relationships;
    }

    public void addUml3_0_0_relationship(Uml3_0_0_relationship uml3_0_0_relationship) {
        this.uml3_0_0_relationships.add(uml3_0_0_relationship);
    }
    public List<uml3_0_0_NamedElement> getUml3_0_0_namedelements() {
        return uml3_0_0_namedelements;
    }

    public void addUml3_0_0_namedelement(Uml3_0_0_namedelement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelements.add(uml3_0_0_namedelement);
    }

}