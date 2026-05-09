





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_InformationFlow extends DirectedRelationship, PackageableElement {






    private List<UML2WithID_Relationship> uml2withid_relationships;




    private List<UML2WithID_Classifier> uml2withid_classifiers;


    public UML2WithID_InformationFlow(
    ) {
        super(
        );
        this.uml2withid_relationships = new ArrayList<>();
        this.uml2withid_classifiers = new ArrayList<>();
    }

    public UML2WithID_InformationFlow(
        ArrayList<UML2WithID_Relationship> uml2withid_relationships,        ArrayList<UML2WithID_Classifier> uml2withid_classifiers    ) {
        this.uml2withid_relationships = uml2withid_relationships;
        this.uml2withid_classifiers = uml2withid_classifiers;
    }


    public List<UML2WithID_Relationship> getUml2withid_relationships() {
        return uml2withid_relationships;
    }

    public void addUml2withid_relationship(Uml2withid_relationship uml2withid_relationship) {
        this.uml2withid_relationships.add(uml2withid_relationship);
    }
    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }

}