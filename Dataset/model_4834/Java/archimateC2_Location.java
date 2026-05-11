





import java.util.List;
import java.util.ArrayList;

public class archimateC2_Location extends ActiveStructure {

    private String address;





    private archimateC2_Artifact archimatec2_artifact;




    private List<archimateC2_CommunicationPath> archimatec2_communicationpaths;




    private List<archimateC2_ApplicationComponent> archimatec2_applicationcomponents;




    private archimateC2_DataObject archimatec2_dataobject;




    private archimateC2_CommunicationPath archimatec2_communicationpath;




    private archimateC2_Node archimatec2_node;




    private archimateC2_Network archimatec2_network;




    private List<archimateC2_Representation> archimatec2_representations;




    private List<archimateC2_Node> archimatec2_nodes;




    private archimateC2_Representation archimatec2_representation;




    private List<archimateC2_DataObject> archimatec2_dataobjects;




    private archimateC2_ApplicationComponent archimatec2_applicationcomponent;




    private archimateC2_BusinessObject archimatec2_businessobject;




    private List<archimateC2_BusinessObject> archimatec2_businessobjects;




    private List<archimateC2_Artifact> archimatec2_artifacts;




    private List<archimateC2_Network> archimatec2_networks;


    public archimateC2_Location(
        String address    ) {
        super(
        );
        this.address = address;
        this.archimatec2_communicationpaths = new ArrayList<>();
        this.archimatec2_applicationcomponents = new ArrayList<>();
        this.archimatec2_representations = new ArrayList<>();
        this.archimatec2_nodes = new ArrayList<>();
        this.archimatec2_dataobjects = new ArrayList<>();
        this.archimatec2_businessobjects = new ArrayList<>();
        this.archimatec2_artifacts = new ArrayList<>();
        this.archimatec2_networks = new ArrayList<>();
    }

    public archimateC2_Location(
        String address        ArrayList<archimateC2_CommunicationPath> archimatec2_communicationpaths,        ArrayList<archimateC2_ApplicationComponent> archimatec2_applicationcomponents,        ArrayList<archimateC2_Representation> archimatec2_representations,        ArrayList<archimateC2_Node> archimatec2_nodes,        ArrayList<archimateC2_DataObject> archimatec2_dataobjects,        ArrayList<archimateC2_BusinessObject> archimatec2_businessobjects,        ArrayList<archimateC2_Artifact> archimatec2_artifacts,        ArrayList<archimateC2_Network> archimatec2_networks    ) {
        this.address = address;
        this.archimatec2_communicationpaths = archimatec2_communicationpaths;
        this.archimatec2_applicationcomponents = archimatec2_applicationcomponents;
        this.archimatec2_representations = archimatec2_representations;
        this.archimatec2_nodes = archimatec2_nodes;
        this.archimatec2_dataobjects = archimatec2_dataobjects;
        this.archimatec2_businessobjects = archimatec2_businessobjects;
        this.archimatec2_artifacts = archimatec2_artifacts;
        this.archimatec2_networks = archimatec2_networks;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public archimateC2_Artifact getArchimatec2_artifact() {
        return archimatec2_artifact;
    }

    public void setArchimatec2_artifact(archimateC2_Artifact archimatec2_artifact) {
        this.archimatec2_artifact = archimatec2_artifact;
    }
    public List<archimateC2_CommunicationPath> getArchimatec2_communicationpaths() {
        return archimatec2_communicationpaths;
    }

    public void addArchimatec2_communicationpath(Archimatec2_communicationpath archimatec2_communicationpath) {
        this.archimatec2_communicationpaths.add(archimatec2_communicationpath);
    }
    public List<archimateC2_ApplicationComponent> getArchimatec2_applicationcomponents() {
        return archimatec2_applicationcomponents;
    }

    public void addArchimatec2_applicationcomponent(Archimatec2_applicationcomponent archimatec2_applicationcomponent) {
        this.archimatec2_applicationcomponents.add(archimatec2_applicationcomponent);
    }
    public archimateC2_DataObject getArchimatec2_dataobject() {
        return archimatec2_dataobject;
    }

    public void setArchimatec2_dataobject(archimateC2_DataObject archimatec2_dataobject) {
        this.archimatec2_dataobject = archimatec2_dataobject;
    }
    public archimateC2_CommunicationPath getArchimatec2_communicationpath() {
        return archimatec2_communicationpath;
    }

    public void setArchimatec2_communicationpath(archimateC2_CommunicationPath archimatec2_communicationpath) {
        this.archimatec2_communicationpath = archimatec2_communicationpath;
    }
    public archimateC2_Node getArchimatec2_node() {
        return archimatec2_node;
    }

    public void setArchimatec2_node(archimateC2_Node archimatec2_node) {
        this.archimatec2_node = archimatec2_node;
    }
    public archimateC2_Network getArchimatec2_network() {
        return archimatec2_network;
    }

    public void setArchimatec2_network(archimateC2_Network archimatec2_network) {
        this.archimatec2_network = archimatec2_network;
    }
    public List<archimateC2_Representation> getArchimatec2_representations() {
        return archimatec2_representations;
    }

    public void addArchimatec2_representation(Archimatec2_representation archimatec2_representation) {
        this.archimatec2_representations.add(archimatec2_representation);
    }
    public List<archimateC2_Node> getArchimatec2_nodes() {
        return archimatec2_nodes;
    }

    public void addArchimatec2_node(Archimatec2_node archimatec2_node) {
        this.archimatec2_nodes.add(archimatec2_node);
    }
    public archimateC2_Representation getArchimatec2_representation() {
        return archimatec2_representation;
    }

    public void setArchimatec2_representation(archimateC2_Representation archimatec2_representation) {
        this.archimatec2_representation = archimatec2_representation;
    }
    public List<archimateC2_DataObject> getArchimatec2_dataobjects() {
        return archimatec2_dataobjects;
    }

    public void addArchimatec2_dataobject(Archimatec2_dataobject archimatec2_dataobject) {
        this.archimatec2_dataobjects.add(archimatec2_dataobject);
    }
    public archimateC2_ApplicationComponent getArchimatec2_applicationcomponent() {
        return archimatec2_applicationcomponent;
    }

    public void setArchimatec2_applicationcomponent(archimateC2_ApplicationComponent archimatec2_applicationcomponent) {
        this.archimatec2_applicationcomponent = archimatec2_applicationcomponent;
    }
    public archimateC2_BusinessObject getArchimatec2_businessobject() {
        return archimatec2_businessobject;
    }

    public void setArchimatec2_businessobject(archimateC2_BusinessObject archimatec2_businessobject) {
        this.archimatec2_businessobject = archimatec2_businessobject;
    }
    public List<archimateC2_BusinessObject> getArchimatec2_businessobjects() {
        return archimatec2_businessobjects;
    }

    public void addArchimatec2_businessobject(Archimatec2_businessobject archimatec2_businessobject) {
        this.archimatec2_businessobjects.add(archimatec2_businessobject);
    }
    public List<archimateC2_Artifact> getArchimatec2_artifacts() {
        return archimatec2_artifacts;
    }

    public void addArchimatec2_artifact(Archimatec2_artifact archimatec2_artifact) {
        this.archimatec2_artifacts.add(archimatec2_artifact);
    }
    public List<archimateC2_Network> getArchimatec2_networks() {
        return archimatec2_networks;
    }

    public void addArchimatec2_network(Archimatec2_network archimatec2_network) {
        this.archimatec2_networks.add(archimatec2_network);
    }

}