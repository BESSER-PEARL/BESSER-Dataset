





import java.util.List;
import java.util.ArrayList;

public class UMLModel_InstanceSpecification extends DeployedArtifact, DeploymentTarget, PackageableElement {

    private String classifier;





    private UMLModel_ValueSpecification umlmodel_valuespecification;


    public UMLModel_InstanceSpecification(
        String classifier    ) {
        super(
        );
        this.classifier = classifier;
    }


    public String getClassifier() {
        return classifier;
    }

    public void setClassifier(String classifier) {
        this.classifier = classifier;
    }

    public UMLModel_ValueSpecification getUmlmodel_valuespecification() {
        return umlmodel_valuespecification;
    }

    public void setUmlmodel_valuespecification(UMLModel_ValueSpecification umlmodel_valuespecification) {
        this.umlmodel_valuespecification = umlmodel_valuespecification;
    }

}