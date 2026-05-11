





import java.util.List;
import java.util.ArrayList;

public class archimateC2_InfrastructureService extends ArchimateElement {






    private List<archimateC2_Node> archimatec2_nodes;




    private archimateC2_InfrastructureInterface archimatec2_infrastructureinterface;




    private archimateC2_Node archimatec2_node;




    private archimateC2_Artifact archimatec2_artifact;




    private List<archimateC2_ApplicationFunction> archimatec2_applicationfunctions;




    private archimateC2_ApplicationComponent archimatec2_applicationcomponent;




    private List<archimateC2_ApplicationComponent> archimatec2_applicationcomponents;




    private List<archimateC2_Artifact> archimatec2_artifacts;




    private List<archimateC2_InfrastructureInterface> archimatec2_infrastructureinterfaces;




    private archimateC2_ApplicationFunction archimatec2_applicationfunction;


    public archimateC2_InfrastructureService(
    ) {
        super(
        );
        this.archimatec2_nodes = new ArrayList<>();
        this.archimatec2_applicationfunctions = new ArrayList<>();
        this.archimatec2_applicationcomponents = new ArrayList<>();
        this.archimatec2_artifacts = new ArrayList<>();
        this.archimatec2_infrastructureinterfaces = new ArrayList<>();
    }

    public archimateC2_InfrastructureService(
        ArrayList<archimateC2_Node> archimatec2_nodes,        ArrayList<archimateC2_ApplicationFunction> archimatec2_applicationfunctions,        ArrayList<archimateC2_ApplicationComponent> archimatec2_applicationcomponents,        ArrayList<archimateC2_Artifact> archimatec2_artifacts,        ArrayList<archimateC2_InfrastructureInterface> archimatec2_infrastructureinterfaces    ) {
        this.archimatec2_nodes = archimatec2_nodes;
        this.archimatec2_applicationfunctions = archimatec2_applicationfunctions;
        this.archimatec2_applicationcomponents = archimatec2_applicationcomponents;
        this.archimatec2_artifacts = archimatec2_artifacts;
        this.archimatec2_infrastructureinterfaces = archimatec2_infrastructureinterfaces;
    }


    public List<archimateC2_Node> getArchimatec2_nodes() {
        return archimatec2_nodes;
    }

    public void addArchimatec2_node(Archimatec2_node archimatec2_node) {
        this.archimatec2_nodes.add(archimatec2_node);
    }
    public archimateC2_InfrastructureInterface getArchimatec2_infrastructureinterface() {
        return archimatec2_infrastructureinterface;
    }

    public void setArchimatec2_infrastructureinterface(archimateC2_InfrastructureInterface archimatec2_infrastructureinterface) {
        this.archimatec2_infrastructureinterface = archimatec2_infrastructureinterface;
    }
    public archimateC2_Node getArchimatec2_node() {
        return archimatec2_node;
    }

    public void setArchimatec2_node(archimateC2_Node archimatec2_node) {
        this.archimatec2_node = archimatec2_node;
    }
    public archimateC2_Artifact getArchimatec2_artifact() {
        return archimatec2_artifact;
    }

    public void setArchimatec2_artifact(archimateC2_Artifact archimatec2_artifact) {
        this.archimatec2_artifact = archimatec2_artifact;
    }
    public List<archimateC2_ApplicationFunction> getArchimatec2_applicationfunctions() {
        return archimatec2_applicationfunctions;
    }

    public void addArchimatec2_applicationfunction(Archimatec2_applicationfunction archimatec2_applicationfunction) {
        this.archimatec2_applicationfunctions.add(archimatec2_applicationfunction);
    }
    public archimateC2_ApplicationComponent getArchimatec2_applicationcomponent() {
        return archimatec2_applicationcomponent;
    }

    public void setArchimatec2_applicationcomponent(archimateC2_ApplicationComponent archimatec2_applicationcomponent) {
        this.archimatec2_applicationcomponent = archimatec2_applicationcomponent;
    }
    public List<archimateC2_ApplicationComponent> getArchimatec2_applicationcomponents() {
        return archimatec2_applicationcomponents;
    }

    public void addArchimatec2_applicationcomponent(Archimatec2_applicationcomponent archimatec2_applicationcomponent) {
        this.archimatec2_applicationcomponents.add(archimatec2_applicationcomponent);
    }
    public List<archimateC2_Artifact> getArchimatec2_artifacts() {
        return archimatec2_artifacts;
    }

    public void addArchimatec2_artifact(Archimatec2_artifact archimatec2_artifact) {
        this.archimatec2_artifacts.add(archimatec2_artifact);
    }
    public List<archimateC2_InfrastructureInterface> getArchimatec2_infrastructureinterfaces() {
        return archimatec2_infrastructureinterfaces;
    }

    public void addArchimatec2_infrastructureinterface(Archimatec2_infrastructureinterface archimatec2_infrastructureinterface) {
        this.archimatec2_infrastructureinterfaces.add(archimatec2_infrastructureinterface);
    }
    public archimateC2_ApplicationFunction getArchimatec2_applicationfunction() {
        return archimatec2_applicationfunction;
    }

    public void setArchimatec2_applicationfunction(archimateC2_ApplicationFunction archimatec2_applicationfunction) {
        this.archimatec2_applicationfunction = archimatec2_applicationfunction;
    }

}