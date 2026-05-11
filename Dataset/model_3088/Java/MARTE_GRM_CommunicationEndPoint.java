





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_CommunicationEndPoint extends Resource {

    private String packetSize;



    public MARTE_GRM_CommunicationEndPoint(
        String packetSize    ) {
        super(
        );
        this.packetSize = packetSize;
    }


    public String getPacketsize() {
        return packetSize;
    }

    public void setPacketsize(String packetSize) {
        this.packetSize = packetSize;
    }


}