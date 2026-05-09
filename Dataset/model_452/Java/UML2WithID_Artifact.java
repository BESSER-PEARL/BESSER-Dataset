





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Artifact extends DeployedArtifact, Classifier {

    private String fileName;





    private UML2WithID_Artifact uml2withid_artifact;


    public UML2WithID_Artifact(
        String fileName    ) {
        super(
        );
        this.fileName = fileName;
    }


    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }

    public UML2WithID_Artifact getUml2withid_artifact() {
        return uml2withid_artifact;
    }

    public void setUml2withid_artifact(UML2WithID_Artifact uml2withid_artifact) {
        this.uml2withid_artifact = uml2withid_artifact;
    }

}