





import java.util.List;
import java.util.ArrayList;

public class rtsc_CoordinationProtocol extends NamedElement {






    private List<rtsc_Port> rtsc_ports;


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

}