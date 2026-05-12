





import java.util.List;
import java.util.ArrayList;

public class pcb_PCB  {

    private int programCounter;
    private int startDiskOutputBufferAddress;
    private int startDiskInputBufferAddress;
    private int inputBufferLength;
    private int priority;
    private int cpuid;
    private int outputBufferLength;
    private int pid;
    private int instructionLength;
    private int startDiskTempBufferAddress;
    private int numIO;
    private int elapsedRunTime;
    private int tempBufferLength;
    private int elapsedWaitTime;
    private int executionCount;
    private int clock;
    private int startDiskInstructionAddress;



    public pcb_PCB(
        int programCounter,        int startDiskOutputBufferAddress,        int startDiskInputBufferAddress,        int inputBufferLength,        int priority,        int cpuid,        int outputBufferLength,        int pid,        int instructionLength,        int startDiskTempBufferAddress,        int numIO,        int elapsedRunTime,        int tempBufferLength,        int elapsedWaitTime,        int executionCount,        int clock,        int startDiskInstructionAddress    ) {
        this.programCounter = programCounter;
        this.startDiskOutputBufferAddress = startDiskOutputBufferAddress;
        this.startDiskInputBufferAddress = startDiskInputBufferAddress;
        this.inputBufferLength = inputBufferLength;
        this.priority = priority;
        this.cpuid = cpuid;
        this.outputBufferLength = outputBufferLength;
        this.pid = pid;
        this.instructionLength = instructionLength;
        this.startDiskTempBufferAddress = startDiskTempBufferAddress;
        this.numIO = numIO;
        this.elapsedRunTime = elapsedRunTime;
        this.tempBufferLength = tempBufferLength;
        this.elapsedWaitTime = elapsedWaitTime;
        this.executionCount = executionCount;
        this.clock = clock;
        this.startDiskInstructionAddress = startDiskInstructionAddress;
    }


    public int getProgramcounter() {
        return programCounter;
    }

    public void setProgramcounter(int programCounter) {
        this.programCounter = programCounter;
    }
    public int getStartdiskoutputbufferaddress() {
        return startDiskOutputBufferAddress;
    }

    public void setStartdiskoutputbufferaddress(int startDiskOutputBufferAddress) {
        this.startDiskOutputBufferAddress = startDiskOutputBufferAddress;
    }
    public int getStartdiskinputbufferaddress() {
        return startDiskInputBufferAddress;
    }

    public void setStartdiskinputbufferaddress(int startDiskInputBufferAddress) {
        this.startDiskInputBufferAddress = startDiskInputBufferAddress;
    }
    public int getInputbufferlength() {
        return inputBufferLength;
    }

    public void setInputbufferlength(int inputBufferLength) {
        this.inputBufferLength = inputBufferLength;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public int getCpuid() {
        return cpuid;
    }

    public void setCpuid(int cpuid) {
        this.cpuid = cpuid;
    }
    public int getOutputbufferlength() {
        return outputBufferLength;
    }

    public void setOutputbufferlength(int outputBufferLength) {
        this.outputBufferLength = outputBufferLength;
    }
    public int getPid() {
        return pid;
    }

    public void setPid(int pid) {
        this.pid = pid;
    }
    public int getInstructionlength() {
        return instructionLength;
    }

    public void setInstructionlength(int instructionLength) {
        this.instructionLength = instructionLength;
    }
    public int getStartdisktempbufferaddress() {
        return startDiskTempBufferAddress;
    }

    public void setStartdisktempbufferaddress(int startDiskTempBufferAddress) {
        this.startDiskTempBufferAddress = startDiskTempBufferAddress;
    }
    public int getNumio() {
        return numIO;
    }

    public void setNumio(int numIO) {
        this.numIO = numIO;
    }
    public int getElapsedruntime() {
        return elapsedRunTime;
    }

    public void setElapsedruntime(int elapsedRunTime) {
        this.elapsedRunTime = elapsedRunTime;
    }
    public int getTempbufferlength() {
        return tempBufferLength;
    }

    public void setTempbufferlength(int tempBufferLength) {
        this.tempBufferLength = tempBufferLength;
    }
    public int getElapsedwaittime() {
        return elapsedWaitTime;
    }

    public void setElapsedwaittime(int elapsedWaitTime) {
        this.elapsedWaitTime = elapsedWaitTime;
    }
    public int getExecutioncount() {
        return executionCount;
    }

    public void setExecutioncount(int executionCount) {
        this.executionCount = executionCount;
    }
    public int getClock() {
        return clock;
    }

    public void setClock(int clock) {
        this.clock = clock;
    }
    public int getStartdiskinstructionaddress() {
        return startDiskInstructionAddress;
    }

    public void setStartdiskinstructionaddress(int startDiskInstructionAddress) {
        this.startDiskInstructionAddress = startDiskInstructionAddress;
    }


}