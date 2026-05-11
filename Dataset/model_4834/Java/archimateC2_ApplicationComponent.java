





import java.util.List;
import java.util.ArrayList;

public class archimateC2_ApplicationComponent extends ArchimateElement {






    private archimateC2_Artifact archimatec2_artifact;




    private List<archimateC2_Artifact> archimatec2_artifacts;




    private archimateC2_ApplicationInterface archimatec2_applicationinterface;




    private List<archimateC2_InfrastructureInterface> archimatec2_infrastructureinterfaces;




    private List<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces;




    private archimateC2_InfrastructureInterface archimatec2_infrastructureinterface;




    private List<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces;




    private archimateC2_ApplicationInterface archimatec2_applicationinterface;


    public archimateC2_ApplicationComponent(
    ) {
        super(
        );
        this.archimatec2_artifacts = new ArrayList<>();
        this.archimatec2_infrastructureinterfaces = new ArrayList<>();
        this.archimatec2_applicationinterfaces = new ArrayList<>();
        this.archimatec2_applicationinterfaces = new ArrayList<>();
    }

    public archimateC2_ApplicationComponent(
        ArrayList<archimateC2_Artifact> archimatec2_artifacts,        ArrayList<archimateC2_InfrastructureInterface> archimatec2_infrastructureinterfaces,        ArrayList<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces,        ArrayList<archimateC2_ApplicationInterface> archimatec2_applicationinterfaces    ) {
        this.archimatec2_artifacts = archimatec2_artifacts;
        this.archimatec2_infrastructureinterfaces = archimatec2_infrastructureinterfaces;
        this.archimatec2_applicationinterfaces = archimatec2_applicationinterfaces;
        this.archimatec2_applicationinterfaces = archimatec2_applicationinterfaces;
    }


    public archimateC2_Artifact getArchimatec2_artifact() {
        return archimatec2_artifact;
    }

    public void setArchimatec2_artifact(archimateC2_Artifact archimatec2_artifact) {
        this.archimatec2_artifact = archimatec2_artifact;
    }
    public List<archimateC2_Artifact> getArchimatec2_artifacts() {
        return archimatec2_artifacts;
    }

    public void addArchimatec2_artifact(Archimatec2_artifact archimatec2_artifact) {
        this.archimatec2_artifacts.add(archimatec2_artifact);
    }
    public archimateC2_ApplicationInterface getArchimatec2_applicationinterface() {
        return archimatec2_applicationinterface;
    }

    public void setArchimatec2_applicationinterface(archimateC2_ApplicationInterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterface = archimatec2_applicationinterface;
    }
    public List<archimateC2_InfrastructureInterface> getArchimatec2_infrastructureinterfaces() {
        return archimatec2_infrastructureinterfaces;
    }

    public void addArchimatec2_infrastructureinterface(Archimatec2_infrastructureinterface archimatec2_infrastructureinterface) {
        this.archimatec2_infrastructureinterfaces.add(archimatec2_infrastructureinterface);
    }
    public List<archimateC2_ApplicationInterface> getArchimatec2_applicationinterfaces() {
        return archimatec2_applicationinterfaces;
    }

    public void addArchimatec2_applicationinterface(Archimatec2_applicationinterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterfaces.add(archimatec2_applicationinterface);
    }
    public archimateC2_InfrastructureInterface getArchimatec2_infrastructureinterface() {
        return archimatec2_infrastructureinterface;
    }

    public void setArchimatec2_infrastructureinterface(archimateC2_InfrastructureInterface archimatec2_infrastructureinterface) {
        this.archimatec2_infrastructureinterface = archimatec2_infrastructureinterface;
    }
    public List<archimateC2_ApplicationInterface> getArchimatec2_applicationinterfaces() {
        return archimatec2_applicationinterfaces;
    }

    public void addArchimatec2_applicationinterface(Archimatec2_applicationinterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterfaces.add(archimatec2_applicationinterface);
    }
    public archimateC2_ApplicationInterface getArchimatec2_applicationinterface() {
        return archimatec2_applicationinterface;
    }

    public void setArchimatec2_applicationinterface(archimateC2_ApplicationInterface archimatec2_applicationinterface) {
        this.archimatec2_applicationinterface = archimatec2_applicationinterface;
    }

}