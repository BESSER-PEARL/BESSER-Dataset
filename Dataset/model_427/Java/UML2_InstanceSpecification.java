





import java.util.List;
import java.util.ArrayList;

public class UML2_InstanceSpecification extends DeploymentTarget, PackageableElement, DeployedArtifact {






    private List<UML2_Classifier> uml2_classifiers;


    public UML2_InstanceSpecification(
    ) {
        super(
        );
        this.uml2_classifiers = new ArrayList<>();
    }

    public UML2_InstanceSpecification(
        ArrayList<UML2_Classifier> uml2_classifiers    ) {
        this.uml2_classifiers = uml2_classifiers;
    }


    public List<UML2_Classifier> getUml2_classifiers() {
        return uml2_classifiers;
    }

    public void addUml2_classifier(Uml2_classifier uml2_classifier) {
        this.uml2_classifiers.add(uml2_classifier);
    }

}