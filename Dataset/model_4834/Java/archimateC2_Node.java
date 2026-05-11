





import java.util.List;
import java.util.ArrayList;

public class archimateC2_Node extends ArchimateElement {






    private archimateC2_Artifact archimatec2_artifact;




    private archimateC2_CommunicationPath archimatec2_communicationpath;




    private archimateC2_InfrastructureInterface archimatec2_infrastructureinterface;




    private List<archimateC2_InfrastructureInterface> archimatec2_infrastructureinterfaces;




    private List<archimateC2_InfrastructureInterface> archimatec2_infrastructureinterfaces;




    private archimateC2_CommunicationPath archimatec2_communicationpath;




    private archimateC2_InfrastructureInterface archimatec2_infrastructureinterface;




    private List<archimateC2_Artifact> archimatec2_artifacts;


    public archimateC2_Node(
    ) {
        super(
        );
        this.archimatec2_infrastructureinterfaces = new ArrayList<>();
        this.archimatec2_infrastructureinterfaces = new ArrayList<>();
        this.archimatec2_artifacts = new ArrayList<>();
    }

    public archimateC2_Node(
        ArrayList<archimateC2_InfrastructureInterface> archimatec2_infrastructureinterfaces,        ArrayList<archimateC2_InfrastructureInterface> archimatec2_infrastructureinterfaces,        ArrayList<archimateC2_Artifact> archimatec2_artifacts    ) {
        this.archimatec2_infrastructureinterfaces = archimatec2_infrastructureinterfaces;
        this.archimatec2_infrastructureinterfaces = archimatec2_infrastructureinterfaces;
        this.archimatec2_artifacts = archimatec2_artifacts;
    }


    public archimateC2_Artifact getArchimatec2_artifact() {
        return archimatec2_artifact;
    }

    public void setArchimatec2_artifact(archimateC2_Artifact archimatec2_artifact) {
        this.archimatec2_artifact = archimatec2_artifact;
    }
    public archimateC2_CommunicationPath getArchimatec2_communicationpath() {
        return archimatec2_communicationpath;
    }

    public void setArchimatec2_communicationpath(archimateC2_CommunicationPath archimatec2_communicationpath) {
        this.archimatec2_communicationpath = archimatec2_communicationpath;
    }
    public archimateC2_InfrastructureInterface getArchimatec2_infrastructureinterface() {
        return archimatec2_infrastructureinterface;
    }

    public void setArchimatec2_infrastructureinterface(archimateC2_InfrastructureInterface archimatec2_infrastructureinterface) {
        this.archimatec2_infrastructureinterface = archimatec2_infrastructureinterface;
    }
    public List<archimateC2_InfrastructureInterface> getArchimatec2_infrastructureinterfaces() {
        return archimatec2_infrastructureinterfaces;
    }

    public void addArchimatec2_infrastructureinterface(Archimatec2_infrastructureinterface archimatec2_infrastructureinterface) {
        this.archimatec2_infrastructureinterfaces.add(archimatec2_infrastructureinterface);
    }
    public List<archimateC2_InfrastructureInterface> getArchimatec2_infrastructureinterfaces() {
        return archimatec2_infrastructureinterfaces;
    }

    public void addArchimatec2_infrastructureinterface(Archimatec2_infrastructureinterface archimatec2_infrastructureinterface) {
        this.archimatec2_infrastructureinterfaces.add(archimatec2_infrastructureinterface);
    }
    public archimateC2_CommunicationPath getArchimatec2_communicationpath() {
        return archimatec2_communicationpath;
    }

    public void setArchimatec2_communicationpath(archimateC2_CommunicationPath archimatec2_communicationpath) {
        this.archimatec2_communicationpath = archimatec2_communicationpath;
    }
    public archimateC2_InfrastructureInterface getArchimatec2_infrastructureinterface() {
        return archimatec2_infrastructureinterface;
    }

    public void setArchimatec2_infrastructureinterface(archimateC2_InfrastructureInterface archimatec2_infrastructureinterface) {
        this.archimatec2_infrastructureinterface = archimatec2_infrastructureinterface;
    }
    public List<archimateC2_Artifact> getArchimatec2_artifacts() {
        return archimatec2_artifacts;
    }

    public void addArchimatec2_artifact(Archimatec2_artifact archimatec2_artifact) {
        this.archimatec2_artifacts.add(archimatec2_artifact);
    }

}