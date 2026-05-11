





import java.util.List;
import java.util.ArrayList;

public class ddsm_StormNimbus extends InternalComponent {

    private String retryInterval;
    private String monitorFrequency;
    private String queueSize;
    private String taskTimeout;
    private String retryTimes;
    private String supervisorTimeout;



    public ddsm_StormNimbus(
        String retryInterval,        String monitorFrequency,        String queueSize,        String taskTimeout,        String retryTimes,        String supervisorTimeout    ) {
        super(
        );
        this.retryInterval = retryInterval;
        this.monitorFrequency = monitorFrequency;
        this.queueSize = queueSize;
        this.taskTimeout = taskTimeout;
        this.retryTimes = retryTimes;
        this.supervisorTimeout = supervisorTimeout;
    }


    public String getRetryinterval() {
        return retryInterval;
    }

    public void setRetryinterval(String retryInterval) {
        this.retryInterval = retryInterval;
    }
    public String getMonitorfrequency() {
        return monitorFrequency;
    }

    public void setMonitorfrequency(String monitorFrequency) {
        this.monitorFrequency = monitorFrequency;
    }
    public String getQueuesize() {
        return queueSize;
    }

    public void setQueuesize(String queueSize) {
        this.queueSize = queueSize;
    }
    public String getTasktimeout() {
        return taskTimeout;
    }

    public void setTasktimeout(String taskTimeout) {
        this.taskTimeout = taskTimeout;
    }
    public String getRetrytimes() {
        return retryTimes;
    }

    public void setRetrytimes(String retryTimes) {
        this.retryTimes = retryTimes;
    }
    public String getSupervisortimeout() {
        return supervisorTimeout;
    }

    public void setSupervisortimeout(String supervisorTimeout) {
        this.supervisorTimeout = supervisorTimeout;
    }


}