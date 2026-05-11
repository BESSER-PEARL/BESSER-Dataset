





import java.util.List;
import java.util.ArrayList;

public class ddsm_StormSupervisor extends InternalComponent {

    private String cpuCapacity;
    private String workerStartTimeout;
    private String memoryCapacity;
    private String heartbeatFrequency;



    public ddsm_StormSupervisor(
        String cpuCapacity,        String workerStartTimeout,        String memoryCapacity,        String heartbeatFrequency    ) {
        super(
        );
        this.cpuCapacity = cpuCapacity;
        this.workerStartTimeout = workerStartTimeout;
        this.memoryCapacity = memoryCapacity;
        this.heartbeatFrequency = heartbeatFrequency;
    }


    public String getCpucapacity() {
        return cpuCapacity;
    }

    public void setCpucapacity(String cpuCapacity) {
        this.cpuCapacity = cpuCapacity;
    }
    public String getWorkerstarttimeout() {
        return workerStartTimeout;
    }

    public void setWorkerstarttimeout(String workerStartTimeout) {
        this.workerStartTimeout = workerStartTimeout;
    }
    public String getMemorycapacity() {
        return memoryCapacity;
    }

    public void setMemorycapacity(String memoryCapacity) {
        this.memoryCapacity = memoryCapacity;
    }
    public String getHeartbeatfrequency() {
        return heartbeatFrequency;
    }

    public void setHeartbeatfrequency(String heartbeatFrequency) {
        this.heartbeatFrequency = heartbeatFrequency;
    }


}