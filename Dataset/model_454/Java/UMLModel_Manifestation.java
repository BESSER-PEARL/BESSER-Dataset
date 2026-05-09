





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Manifestation extends Abstraction {

    private String utilizedElement;





    private UMLModel_Artifact umlmodel_artifact;


    public UMLModel_Manifestation(
        String utilizedElement    ) {
        super(
        );
        this.utilizedElement = utilizedElement;
    }


    public String getUtilizedelement() {
        return utilizedElement;
    }

    public void setUtilizedelement(String utilizedElement) {
        this.utilizedElement = utilizedElement;
    }

    public UMLModel_Artifact getUmlmodel_artifact() {
        return umlmodel_artifact;
    }

    public void setUmlmodel_artifact(UMLModel_Artifact umlmodel_artifact) {
        this.umlmodel_artifact = umlmodel_artifact;
    }

}