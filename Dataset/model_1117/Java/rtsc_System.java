





import java.util.List;
import java.util.ArrayList;

public class rtsc_System  {






    private List<rtsc_CoordinationProtocol> rtsc_coordinationprotocols;




    private List<rtsc_Realtimestatechart> rtsc_realtimestatecharts;


    public rtsc_System(
    ) {
        this.rtsc_coordinationprotocols = new ArrayList<>();
        this.rtsc_realtimestatecharts = new ArrayList<>();
    }

    public rtsc_System(
        ArrayList<rtsc_CoordinationProtocol> rtsc_coordinationprotocols,        ArrayList<rtsc_Realtimestatechart> rtsc_realtimestatecharts    ) {
        this.rtsc_coordinationprotocols = rtsc_coordinationprotocols;
        this.rtsc_realtimestatecharts = rtsc_realtimestatecharts;
    }


    public List<rtsc_CoordinationProtocol> getRtsc_coordinationprotocols() {
        return rtsc_coordinationprotocols;
    }

    public void addRtsc_coordinationprotocol(Rtsc_coordinationprotocol rtsc_coordinationprotocol) {
        this.rtsc_coordinationprotocols.add(rtsc_coordinationprotocol);
    }
    public List<rtsc_Realtimestatechart> getRtsc_realtimestatecharts() {
        return rtsc_realtimestatecharts;
    }

    public void addRtsc_realtimestatechart(Rtsc_realtimestatechart rtsc_realtimestatechart) {
        this.rtsc_realtimestatecharts.add(rtsc_realtimestatechart);
    }

}