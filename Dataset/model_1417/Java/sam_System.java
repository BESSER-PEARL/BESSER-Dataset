





import java.util.List;
import java.util.ArrayList;

public class sam_System extends ModelContent {






    private sam_Port sam_port;




    private List<sam_DataStore> sam_datastores;




    private sam_Flow sam_flow;




    private List<sam_Flow> sam_flows;




    private sam_System sam_system;




    private sam_ModelContent sam_modelcontent;




    private sam_DataStore sam_datastore;




    private List<sam_ModelContent> sam_modelcontents;




    private List<sam_Port> sam_ports;


    public sam_System(
    ) {
        super(
        );
        this.sam_datastores = new ArrayList<>();
        this.sam_flows = new ArrayList<>();
        this.sam_modelcontents = new ArrayList<>();
        this.sam_ports = new ArrayList<>();
    }

    public sam_System(
        ArrayList<sam_DataStore> sam_datastores,        ArrayList<sam_Flow> sam_flows,        ArrayList<sam_ModelContent> sam_modelcontents,        ArrayList<sam_Port> sam_ports    ) {
        this.sam_datastores = sam_datastores;
        this.sam_flows = sam_flows;
        this.sam_modelcontents = sam_modelcontents;
        this.sam_ports = sam_ports;
    }


    public sam_Port getSam_port() {
        return sam_port;
    }

    public void setSam_port(sam_Port sam_port) {
        this.sam_port = sam_port;
    }
    public List<sam_DataStore> getSam_datastores() {
        return sam_datastores;
    }

    public void addSam_datastore(Sam_datastore sam_datastore) {
        this.sam_datastores.add(sam_datastore);
    }
    public sam_Flow getSam_flow() {
        return sam_flow;
    }

    public void setSam_flow(sam_Flow sam_flow) {
        this.sam_flow = sam_flow;
    }
    public List<sam_Flow> getSam_flows() {
        return sam_flows;
    }

    public void addSam_flow(Sam_flow sam_flow) {
        this.sam_flows.add(sam_flow);
    }
    public sam_System getSam_system() {
        return sam_system;
    }

    public void setSam_system(sam_System sam_system) {
        this.sam_system = sam_system;
    }
    public sam_ModelContent getSam_modelcontent() {
        return sam_modelcontent;
    }

    public void setSam_modelcontent(sam_ModelContent sam_modelcontent) {
        this.sam_modelcontent = sam_modelcontent;
    }
    public sam_DataStore getSam_datastore() {
        return sam_datastore;
    }

    public void setSam_datastore(sam_DataStore sam_datastore) {
        this.sam_datastore = sam_datastore;
    }
    public List<sam_ModelContent> getSam_modelcontents() {
        return sam_modelcontents;
    }

    public void addSam_modelcontent(Sam_modelcontent sam_modelcontent) {
        this.sam_modelcontents.add(sam_modelcontent);
    }
    public List<sam_Port> getSam_ports() {
        return sam_ports;
    }

    public void addSam_port(Sam_port sam_port) {
        this.sam_ports.add(sam_port);
    }

}