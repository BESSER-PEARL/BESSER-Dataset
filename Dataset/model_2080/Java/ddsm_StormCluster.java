





import java.util.List;
import java.util.ArrayList;

public class ddsm_StormCluster extends MasterSlavePlatform {

    private int workerStartTimeout;
    private int memoryCapacity;
    private int retryInterval;
    private int queueSize;
    private int cpuCapacity;
    private int supervisorFrequency;
    private int monitorFrequency;
    private int retryTimes;
    private int heartbeatFrequency;
    private int taskTimeout;



    public ddsm_StormCluster(
        int workerStartTimeout,        int memoryCapacity,        int retryInterval,        int queueSize,        int cpuCapacity,        int supervisorFrequency,        int monitorFrequency,        int retryTimes,        int heartbeatFrequency,        int taskTimeout    ) {
        super(
        );
        this.workerStartTimeout = workerStartTimeout;
        this.memoryCapacity = memoryCapacity;
        this.retryInterval = retryInterval;
        this.queueSize = queueSize;
        this.cpuCapacity = cpuCapacity;
        this.supervisorFrequency = supervisorFrequency;
        this.monitorFrequency = monitorFrequency;
        this.retryTimes = retryTimes;
        this.heartbeatFrequency = heartbeatFrequency;
        this.taskTimeout = taskTimeout;
    }


    public int getWorkerstarttimeout() {
        return workerStartTimeout;
    }

    public void setWorkerstarttimeout(int workerStartTimeout) {
        this.workerStartTimeout = workerStartTimeout;
    }
    public int getMemorycapacity() {
        return memoryCapacity;
    }

    public void setMemorycapacity(int memoryCapacity) {
        this.memoryCapacity = memoryCapacity;
    }
    public int getRetryinterval() {
        return retryInterval;
    }

    public void setRetryinterval(int retryInterval) {
        this.retryInterval = retryInterval;
    }
    public int getQueuesize() {
        return queueSize;
    }

    public void setQueuesize(int queueSize) {
        this.queueSize = queueSize;
    }
    public int getCpucapacity() {
        return cpuCapacity;
    }

    public void setCpucapacity(int cpuCapacity) {
        this.cpuCapacity = cpuCapacity;
    }
    public int getSupervisorfrequency() {
        return supervisorFrequency;
    }

    public void setSupervisorfrequency(int supervisorFrequency) {
        this.supervisorFrequency = supervisorFrequency;
    }
    public int getMonitorfrequency() {
        return monitorFrequency;
    }

    public void setMonitorfrequency(int monitorFrequency) {
        this.monitorFrequency = monitorFrequency;
    }
    public int getRetrytimes() {
        return retryTimes;
    }

    public void setRetrytimes(int retryTimes) {
        this.retryTimes = retryTimes;
    }
    public int getHeartbeatfrequency() {
        return heartbeatFrequency;
    }

    public void setHeartbeatfrequency(int heartbeatFrequency) {
        this.heartbeatFrequency = heartbeatFrequency;
    }
    public int getTasktimeout() {
        return taskTimeout;
    }

    public void setTasktimeout(int taskTimeout) {
        this.taskTimeout = taskTimeout;
    }


}