





import java.util.List;
import java.util.ArrayList;

public class camel_scalability_VerticalScalingAction extends ScalingAction {

    private int memoryUpdate;
    private int coreUpdate;
    private int networkUpdate;
    private int storageUpdate;
    private float CPUUpdate;
    private int ioUpdate;



    public camel_scalability_VerticalScalingAction(
        int memoryUpdate,        int coreUpdate,        int networkUpdate,        int storageUpdate,        float CPUUpdate,        int ioUpdate    ) {
        super(
        );
        this.memoryUpdate = memoryUpdate;
        this.coreUpdate = coreUpdate;
        this.networkUpdate = networkUpdate;
        this.storageUpdate = storageUpdate;
        this.CPUUpdate = CPUUpdate;
        this.ioUpdate = ioUpdate;
    }


    public int getMemoryupdate() {
        return memoryUpdate;
    }

    public void setMemoryupdate(int memoryUpdate) {
        this.memoryUpdate = memoryUpdate;
    }
    public int getCoreupdate() {
        return coreUpdate;
    }

    public void setCoreupdate(int coreUpdate) {
        this.coreUpdate = coreUpdate;
    }
    public int getNetworkupdate() {
        return networkUpdate;
    }

    public void setNetworkupdate(int networkUpdate) {
        this.networkUpdate = networkUpdate;
    }
    public int getStorageupdate() {
        return storageUpdate;
    }

    public void setStorageupdate(int storageUpdate) {
        this.storageUpdate = storageUpdate;
    }
    public float getCpuupdate() {
        return CPUUpdate;
    }

    public void setCpuupdate(float CPUUpdate) {
        this.CPUUpdate = CPUUpdate;
    }
    public int getIoupdate() {
        return ioUpdate;
    }

    public void setIoupdate(int ioUpdate) {
        this.ioUpdate = ioUpdate;
    }


}