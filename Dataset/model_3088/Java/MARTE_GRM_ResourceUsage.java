





import java.util.List;
import java.util.ArrayList;

public class MARTE_GRM_ResourceUsage  {

    private String allocatedMemory;
    private String execTime;
    private String usedMemory;
    private String energy;
    private String msgSize;
    private String powerPeak;



    public MARTE_GRM_ResourceUsage(
        String allocatedMemory,        String execTime,        String usedMemory,        String energy,        String msgSize,        String powerPeak    ) {
        this.allocatedMemory = allocatedMemory;
        this.execTime = execTime;
        this.usedMemory = usedMemory;
        this.energy = energy;
        this.msgSize = msgSize;
        this.powerPeak = powerPeak;
    }


    public String getAllocatedmemory() {
        return allocatedMemory;
    }

    public void setAllocatedmemory(String allocatedMemory) {
        this.allocatedMemory = allocatedMemory;
    }
    public String getExectime() {
        return execTime;
    }

    public void setExectime(String execTime) {
        this.execTime = execTime;
    }
    public String getUsedmemory() {
        return usedMemory;
    }

    public void setUsedmemory(String usedMemory) {
        this.usedMemory = usedMemory;
    }
    public String getEnergy() {
        return energy;
    }

    public void setEnergy(String energy) {
        this.energy = energy;
    }
    public String getMsgsize() {
        return msgSize;
    }

    public void setMsgsize(String msgSize) {
        this.msgSize = msgSize;
    }
    public String getPowerpeak() {
        return powerPeak;
    }

    public void setPowerpeak(String powerPeak) {
        this.powerPeak = powerPeak;
    }


}