





import java.util.List;
import java.util.ArrayList;

public class rtsc_Connector  {






    private rtsc_CoordinationProtocol rtsc_coordinationprotocol;




    private List<rtsc_Port> rtsc_ports;




    private rtsc_Port rtsc_port;


    public rtsc_Connector(
    ) {
        this.rtsc_ports = new ArrayList<>();
    }

    public rtsc_Connector(
        ArrayList<rtsc_Port> rtsc_ports    ) {
        this.rtsc_ports = rtsc_ports;
    }


    public rtsc_CoordinationProtocol getRtsc_coordinationprotocol() {
        return rtsc_coordinationprotocol;
    }

    public void setRtsc_coordinationprotocol(rtsc_CoordinationProtocol rtsc_coordinationprotocol) {
        this.rtsc_coordinationprotocol = rtsc_coordinationprotocol;
    }
    public List<rtsc_Port> getRtsc_ports() {
        return rtsc_ports;
    }

    public void addRtsc_port(Rtsc_port rtsc_port) {
        this.rtsc_ports.add(rtsc_port);
    }
    public rtsc_Port getRtsc_port() {
        return rtsc_port;
    }

    public void setRtsc_port(rtsc_Port rtsc_port) {
        this.rtsc_port = rtsc_port;
    }

}