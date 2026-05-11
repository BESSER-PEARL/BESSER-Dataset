





import java.util.List;
import java.util.ArrayList;

public class MARTE_GQAM_GaCommChannel extends SchedulableResource {

    private String utilization;
    private String packetSize;



    public MARTE_GQAM_GaCommChannel(
        String utilization,        String packetSize    ) {
        super(
        );
        this.utilization = utilization;
        this.packetSize = packetSize;
    }


    public String getUtilization() {
        return utilization;
    }

    public void setUtilization(String utilization) {
        this.utilization = utilization;
    }
    public String getPacketsize() {
        return packetSize;
    }

    public void setPacketsize(String packetSize) {
        this.packetSize = packetSize;
    }


}