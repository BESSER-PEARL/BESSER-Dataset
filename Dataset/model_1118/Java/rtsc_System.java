





import java.util.List;
import java.util.ArrayList;

public class rtsc_System  {






    private List<rtsc_CoordinationProtocol> rtsc_coordinationprotocols;


    public rtsc_System(
    ) {
        this.rtsc_coordinationprotocols = new ArrayList<>();
    }

    public rtsc_System(
        ArrayList<rtsc_CoordinationProtocol> rtsc_coordinationprotocols    ) {
        this.rtsc_coordinationprotocols = rtsc_coordinationprotocols;
    }


    public List<rtsc_CoordinationProtocol> getRtsc_coordinationprotocols() {
        return rtsc_coordinationprotocols;
    }

    public void addRtsc_coordinationprotocol(Rtsc_coordinationprotocol rtsc_coordinationprotocol) {
        this.rtsc_coordinationprotocols.add(rtsc_coordinationprotocol);
    }

}