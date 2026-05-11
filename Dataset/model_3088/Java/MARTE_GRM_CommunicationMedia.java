





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_CommunicationMedia extends ProcessingResource {

    private String transmMode;
    private String elementSize;
    private String packetT;
    private String blockT;
    private String capacity;



    public MARTE_GRM_CommunicationMedia(
        String transmMode,        String elementSize,        String packetT,        String blockT,        String capacity    ) {
        super(
        );
        this.transmMode = transmMode;
        this.elementSize = elementSize;
        this.packetT = packetT;
        this.blockT = blockT;
        this.capacity = capacity;
    }


    public String getTransmmode() {
        return transmMode;
    }

    public void setTransmmode(String transmMode) {
        this.transmMode = transmMode;
    }
    public String getElementsize() {
        return elementSize;
    }

    public void setElementsize(String elementSize) {
        this.elementSize = elementSize;
    }
    public String getPackett() {
        return packetT;
    }

    public void setPackett(String packetT) {
        this.packetT = packetT;
    }
    public String getBlockt() {
        return blockT;
    }

    public void setBlockt(String blockT) {
        this.blockT = blockT;
    }
    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }


}