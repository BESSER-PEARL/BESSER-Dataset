





import java.util.List;
import java.util.ArrayList;

public class rtsc_CoordinationProtocol extends NamedElement {






    private List<rtsc_Port> rtsc_ports;




    private rtsc_System rtsc_system;




    private rtsc_Connector rtsc_connector;


    public rtsc_CoordinationProtocol(
    ) {
        super(
        );
        this.rtsc_ports = new ArrayList<>();
    }

    public rtsc_CoordinationProtocol(
        ArrayList<rtsc_Port> rtsc_ports    ) {
        this.rtsc_ports = rtsc_ports;
    }


    public List<rtsc_Port> getRtsc_ports() {
        return rtsc_ports;
    }

    public void addRtsc_port(Rtsc_port rtsc_port) {
        this.rtsc_ports.add(rtsc_port);
    }
    public rtsc_System getRtsc_system() {
        return rtsc_system;
    }

    public void setRtsc_system(rtsc_System rtsc_system) {
        this.rtsc_system = rtsc_system;
    }
    public rtsc_Connector getRtsc_connector() {
        return rtsc_connector;
    }

    public void setRtsc_connector(rtsc_Connector rtsc_connector) {
        this.rtsc_connector = rtsc_connector;
    }

}