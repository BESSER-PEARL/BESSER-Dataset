





import java.util.List;
import java.util.ArrayList;

public class UML2_InformationFlow extends PackageableElement, DirectedRelationship {






    private List<UML2_Classifier> uml2_classifiers;




    private List<UML2_Relationship> uml2_relationships;


    public UML2_InformationFlow(
    ) {
        super(
        );
        this.uml2_classifiers = new ArrayList<>();
        this.uml2_relationships = new ArrayList<>();
    }

    public UML2_InformationFlow(
        ArrayList<UML2_Classifier> uml2_classifiers,        ArrayList<UML2_Relationship> uml2_relationships    ) {
        this.uml2_classifiers = uml2_classifiers;
        this.uml2_relationships = uml2_relationships;
    }


    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }
    public List<UML2_Relationship> getUml2_relationships() {
        return uml2_relationships;
    }

    public void addUml2_relationship(Uml2_relationship uml2_relationship) {
        this.uml2_relationships.add(uml2_relationship);
    }

}