





import java.util.List;
import java.util.ArrayList;

public class archimateC2_DataObject extends ArchimateElement {






    private archimateC2_ApplicationFunction archimatec2_applicationfunction;




    private List<archimateC2_Artifact> archimatec2_artifacts;




    private List<archimateC2_ApplicationFunction> archimatec2_applicationfunctions;




    private archimateC2_Artifact archimatec2_artifact;


    public archimateC2_DataObject(
    ) {
        super(
        );
        this.archimatec2_artifacts = new ArrayList<>();
        this.archimatec2_applicationfunctions = new ArrayList<>();
    }

    public archimateC2_DataObject(
        ArrayList<archimateC2_Artifact> archimatec2_artifacts,        ArrayList<archimateC2_ApplicationFunction> archimatec2_applicationfunctions    ) {
        this.archimatec2_artifacts = archimatec2_artifacts;
        this.archimatec2_applicationfunctions = archimatec2_applicationfunctions;
    }


    public archimateC2_ApplicationFunction getArchimatec2_applicationfunction() {
        return archimatec2_applicationfunction;
    }

    public void setArchimatec2_applicationfunction(archimateC2_ApplicationFunction archimatec2_applicationfunction) {
        this.archimatec2_applicationfunction = archimatec2_applicationfunction;
    }
    public List<archimateC2_Artifact> getArchimatec2_artifacts() {
        return archimatec2_artifacts;
    }

    public void addArchimatec2_artifact(Archimatec2_artifact archimatec2_artifact) {
        this.archimatec2_artifacts.add(archimatec2_artifact);
    }
    public List<archimateC2_ApplicationFunction> getArchimatec2_applicationfunctions() {
        return archimatec2_applicationfunctions;
    }

    public void addArchimatec2_applicationfunction(Archimatec2_applicationfunction archimatec2_applicationfunction) {
        this.archimatec2_applicationfunctions.add(archimatec2_applicationfunction);
    }
    public archimateC2_Artifact getArchimatec2_artifact() {
        return archimatec2_artifact;
    }

    public void setArchimatec2_artifact(archimateC2_Artifact archimatec2_artifact) {
        this.archimatec2_artifact = archimatec2_artifact;
    }

}