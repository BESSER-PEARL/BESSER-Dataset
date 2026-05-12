





import java.util.List;
import java.util.ArrayList;

public class cpu_CPU  {

    private int cpuids;
    private None pcb;
    private String log;
    private None cache;
    private int numProcesses;
    private None previousInstruction;
    private int idleTime;
    private int executeTime;
    private int cpuid;
    private boolean shutdown;
    private None register;
    private String dmaChannel;



    public cpu_CPU(
        int cpuids,        None pcb,        String log,        None cache,        int numProcesses,        None previousInstruction,        int idleTime,        int executeTime,        int cpuid,        boolean shutdown,        None register,        String dmaChannel    ) {
        this.cpuids = cpuids;
        this.pcb = pcb;
        this.log = log;
        this.cache = cache;
        this.numProcesses = numProcesses;
        this.previousInstruction = previousInstruction;
        this.idleTime = idleTime;
        this.executeTime = executeTime;
        this.cpuid = cpuid;
        this.shutdown = shutdown;
        this.register = register;
        this.dmaChannel = dmaChannel;
    }


    public int getCpuids() {
        return cpuids;
    }

    public void setCpuids(int cpuids) {
        this.cpuids = cpuids;
    }
    public None getPcb() {
        return pcb;
    }

    public void setPcb(None pcb) {
        this.pcb = pcb;
    }
    public String getLog() {
        return log;
    }

    public void setLog(String log) {
        this.log = log;
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
    public int getExecutetime() {
        return executeTime;
    }

    public void setExecutetime(int executeTime) {
        this.executeTime = executeTime;
    }
    public int getCpuid() {
        return cpuid;
    }

    public void setCpuid(int cpuid) {
        this.cpuid = cpuid;
    }
    public boolean getShutdown() {
        return shutdown;
    }

    public void setShutdown(boolean shutdown) {
        this.shutdown = shutdown;
    }
    public None getRegister() {
        return register;
    }

    public void setRegister(None register) {
        this.register = register;
    }
    public String getDmachannel() {
        return dmaChannel;
    }

    public void setDmachannel(String dmaChannel) {
        this.dmaChannel = dmaChannel;
    }


}