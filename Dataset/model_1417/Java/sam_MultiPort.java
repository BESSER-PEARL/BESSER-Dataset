





import java.util.List;
import java.util.ArrayList;

public class sam_MultiPort extends NamedItem {






    private List<sam_Port> sam_ports;




    private sam_Port sam_port;




    private sam_ModelContent sam_modelcontent;




    private sam_ModelContent sam_modelcontent;




    private sam_MultiPort sam_multiport;


    public sam_MultiPort(
    ) {
        super(
        );
        this.sam_ports = new ArrayList<>();
    }

    public sam_MultiPort(
        ArrayList<sam_Port> sam_ports    ) {
        this.sam_ports = sam_ports;
    }


    public List<sam_Port> getSam_ports() {
        return sam_ports;
    }

    public void addSam_port(Sam_port sam_port) {
        this.sam_ports.add(sam_port);
    }
    public sam_Port getSam_port() {
        return sam_port;
    }

    public void setSam_port(sam_Port sam_port) {
        this.sam_port = sam_port;
    }
    public sam_ModelContent getSam_modelcontent() {
        return sam_modelcontent;
    }

    public void setSam_modelcontent(sam_ModelContent sam_modelcontent) {
        this.sam_modelcontent = sam_modelcontent;
    }
    public sam_ModelContent getSam_modelcontent() {
        return sam_modelcontent;
    }

    public void setSam_modelcontent(sam_ModelContent sam_modelcontent) {
        this.sam_modelcontent = sam_modelcontent;
    }
    public sam_MultiPort getSam_multiport() {
        return sam_multiport;
    }

    public void setSam_multiport(sam_MultiPort sam_multiport) {
        this.sam_multiport = sam_multiport;
    }

}