





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_InstanceSpecification extends DeployedArtifact, PackageableElement, DeploymentTarget {






    private List<UML2WithID_Classifier> uml2withid_classifiers;


    public UML2WithID_InstanceSpecification(
    ) {
        super(
        );
        this.uml2withid_classifiers = new ArrayList<>();
    }

    public UML2WithID_InstanceSpecification(
        ArrayList<UML2WithID_Classifier> uml2withid_classifiers    ) {
        this.uml2withid_classifiers = uml2withid_classifiers;
    }


    public List<UML2WithID_Classifier> getUml2withid_classifiers() {
        return uml2withid_classifiers;
    }

    public void addUml2withid_classifier(Uml2withid_classifier uml2withid_classifier) {
        this.uml2withid_classifiers.add(uml2withid_classifier);
    }

}