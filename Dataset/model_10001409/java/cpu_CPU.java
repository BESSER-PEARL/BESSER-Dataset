





import java.util.List;
import java.util.ArrayList;

public class cpu_CPU  {

    private boolean shutdown;
    private None cache;
    private int numProcesses;
    private int cpuids;
    private int cpuid;
    private None register;
    private None pcb;
    private None previousInstruction;
    private int idleTime;
    private String dmaChannel;
    private String log;
    private int executeTime;



    public cpu_CPU(
        boolean shutdown,        None cache,        int numProcesses,        int cpuids,        int cpuid,        None register,        None pcb,        None previousInstruction,        int idleTime,        String dmaChannel,        String log,        int executeTime    ) {
        this.shutdown = shutdown;
        this.cache = cache;
        this.numProcesses = numProcesses;
        this.cpuids = cpuids;
        this.cpuid = cpuid;
        this.register = register;
        this.pcb = pcb;
        this.previousInstruction = previousInstruction;
        this.idleTime = idleTime;
        this.dmaChannel = dmaChannel;
        this.log = log;
        this.executeTime = executeTime;
    }


    public boolean getShutdown() {
        return shutdown;
    }

    public void setShutdown(boolean shutdown) {
        this.shutdown = shutdown;
    }
    public None getCache() {
        return cache;
    }

    public void setCache(None cache) {
        this.cache = cache;
    }
    public int getNumprocesses() {
        return numProcesses;
    }

    public void setNumprocesses(int numProcesses) {
        this.numProcesses = numProcesses;
    }
    public int getCpuids() {
        return cpuids;
    }

    public void setCpuids(int cpuids) {
        this.cpuids = cpuids;
    }
    public int getCpuid() {
        return cpuid;
    }

    public void setCpuid(int cpuid) {
        this.cpuid = cpuid;
    }
    public None getRegister() {
        return register;
    }

    public void setRegister(None register) {
        this.register = register;
    }
    public None getPcb() {
        return pcb;
    }

    public void setPcb(None pcb) {
        this.pcb = pcb;
    }
    public None getPreviousinstruction() {
        return previousInstruction;
    }

    public void setPreviousinstruction(None previousInstruction) {
        this.previousInstruction = previousInstruction;
    }
    public int getIdletime() {
        return idleTime;
    }

    public void setIdletime(int idleTime) {
        this.idleTime = idleTime;
    }
    public String getDmachannel() {
        return dmaChannel;
    }

    public void setDmachannel(String dmaChannel) {
        this.dmaChannel = dmaChannel;
    }
    public String getLog() {
        return log;
    }

    public void setLog(String log) {
        this.log = log;
    }
    public int getExecutetime() {
        return executeTime;
    }

    public void setExecutetime(int executeTime) {
        this.executeTime = executeTime;
    }


}