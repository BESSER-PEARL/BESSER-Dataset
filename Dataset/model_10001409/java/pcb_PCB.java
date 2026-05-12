





import java.util.List;
import java.util.ArrayList;

public class pcb_PCB  {

    private int startDiskOutputBufferAddress;
    private int startDiskTempBufferAddress;
    private int priority;
    private int startDiskInstructionAddress;
    private int pid;
    private int clock;
    private int outputBufferLength;
    private int elapsedWaitTime;
    private int tempBufferLength;
    private int executionCount;
    private int cpuid;
    private int programCounter;
    private int elapsedRunTime;
    private int instructionLength;
    private int numIO;
    private int startDiskInputBufferAddress;
    private int inputBufferLength;



    public pcb_PCB(
        int startDiskOutputBufferAddress,        int startDiskTempBufferAddress,        int priority,        int startDiskInstructionAddress,        int pid,        int clock,        int outputBufferLength,        int elapsedWaitTime,        int tempBufferLength,        int executionCount,        int cpuid,        int programCounter,        int elapsedRunTime,        int instructionLength,        int numIO,        int startDiskInputBufferAddress,        int inputBufferLength    ) {
        this.startDiskOutputBufferAddress = startDiskOutputBufferAddress;
        this.startDiskTempBufferAddress = startDiskTempBufferAddress;
        this.priority = priority;
        this.startDiskInstructionAddress = startDiskInstructionAddress;
        this.pid = pid;
        this.clock = clock;
        this.outputBufferLength = outputBufferLength;
        this.elapsedWaitTime = elapsedWaitTime;
        this.tempBufferLength = tempBufferLength;
        this.executionCount = executionCount;
        this.cpuid = cpuid;
        this.programCounter = programCounter;
        this.elapsedRunTime = elapsedRunTime;
        this.instructionLength = instructionLength;
        this.numIO = numIO;
        this.startDiskInputBufferAddress = startDiskInputBufferAddress;
        this.inputBufferLength = inputBufferLength;
    }


    public int getStartdiskoutputbufferaddress() {
        return startDiskOutputBufferAddress;
    }

    public void setStartdiskoutputbufferaddress(int startDiskOutputBufferAddress) {
        this.startDiskOutputBufferAddress = startDiskOutputBufferAddress;
    }
    public int getStartdisktempbufferaddress() {
        return startDiskTempBufferAddress;
    }

    public void setStartdisktempbufferaddress(int startDiskTempBufferAddress) {
        this.startDiskTempBufferAddress = startDiskTempBufferAddress;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public int getStartdiskinstructionaddress() {
        return startDiskInstructionAddress;
    }

    public void setStartdiskinstructionaddress(int startDiskInstructionAddress) {
        this.startDiskInstructionAddress = startDiskInstructionAddress;
    }
    public int getPid() {
        return pid;
    }

    public void setPid(int pid) {
        this.pid = pid;
    }
    public int getClock() {
        return clock;
    }

    public void setClock(int clock) {
        this.clock = clock;
    }
    public int getOutputbufferlength() {
        return outputBufferLength;
    }

    public void setOutputbufferlength(int outputBufferLength) {
        this.outputBufferLength = outputBufferLength;
    }
    public int getElapsedwaittime() {
        return elapsedWaitTime;
    }

    public void setElapsedwaittime(int elapsedWaitTime) {
        this.elapsedWaitTime = elapsedWaitTime;
    }
    public int getTempbufferlength() {
        return tempBufferLength;
    }

    public void setTempbufferlength(int tempBufferLength) {
        this.tempBufferLength = tempBufferLength;
    }
    public int getExecutioncount() {
        return executionCount;
    }

    public void setExecutioncount(int executionCount) {
        this.executionCount = executionCount;
    }
    public int getCpuid() {
        return cpuid;
    }

    public void setCpuid(int cpuid) {
        this.cpuid = cpuid;
    }
    public int getProgramcounter() {
        return programCounter;
    }

    public void setProgramcounter(int programCounter) {
        this.programCounter = programCounter;
    }
    public int getElapsedruntime() {
        return elapsedRunTime;
    }

    public void setElapsedruntime(int elapsedRunTime) {
        this.elapsedRunTime = elapsedRunTime;
    }
    public int getInstructionlength() {
        return instructionLength;
    }

    public void setInstructionlength(int instructionLength) {
        this.instructionLength = instructionLength;
    }
    public int getNumio() {
        return numIO;
    }

    public void setNumio(int numIO) {
        this.numIO = numIO;
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


}