





import java.util.List;
import java.util.ArrayList;

public class driver_Loader  {

    private int endTempBufferAddress;
    private int startOutputBufferAddress;
    private int outputBuffSize;
    private int priority;
    private int currAddress;
    private int endInputBufferAddres;
    private int startInstructionAddress;
    private None disk;
    private int tempBuffSize;
    private int endOutputBufferAddress;
    private int startInputBufferAddress;
    private int startTempBufferAddress;
    private String programFile;
    private int instructionsLength;
    private None processList;
    private int endInstructionAddress;
    private int pid;
    private int inputBuffSize;





    private List<driver_Driver> driver_drivers;


    public driver_Loader(
        int endTempBufferAddress,        int startOutputBufferAddress,        int outputBuffSize,        int priority,        int currAddress,        int endInputBufferAddres,        int startInstructionAddress,        None disk,        int tempBuffSize,        int endOutputBufferAddress,        int startInputBufferAddress,        int startTempBufferAddress,        String programFile,        int instructionsLength,        None processList,        int endInstructionAddress,        int pid,        int inputBuffSize    ) {
        this.endTempBufferAddress = endTempBufferAddress;
        this.startOutputBufferAddress = startOutputBufferAddress;
        this.outputBuffSize = outputBuffSize;
        this.priority = priority;
        this.currAddress = currAddress;
        this.endInputBufferAddres = endInputBufferAddres;
        this.startInstructionAddress = startInstructionAddress;
        this.disk = disk;
        this.tempBuffSize = tempBuffSize;
        this.endOutputBufferAddress = endOutputBufferAddress;
        this.startInputBufferAddress = startInputBufferAddress;
        this.startTempBufferAddress = startTempBufferAddress;
        this.programFile = programFile;
        this.instructionsLength = instructionsLength;
        this.processList = processList;
        this.endInstructionAddress = endInstructionAddress;
        this.pid = pid;
        this.inputBuffSize = inputBuffSize;
        this.driver_drivers = new ArrayList<>();
    }

    public driver_Loader(
        int endTempBufferAddress,        int startOutputBufferAddress,        int outputBuffSize,        int priority,        int currAddress,        int endInputBufferAddres,        int startInstructionAddress,        None disk,        int tempBuffSize,        int endOutputBufferAddress,        int startInputBufferAddress,        int startTempBufferAddress,        String programFile,        int instructionsLength,        None processList,        int endInstructionAddress,        int pid,        int inputBuffSize        ArrayList<driver_Driver> driver_drivers    ) {
        this.endTempBufferAddress = endTempBufferAddress;
        this.startOutputBufferAddress = startOutputBufferAddress;
        this.outputBuffSize = outputBuffSize;
        this.priority = priority;
        this.currAddress = currAddress;
        this.endInputBufferAddres = endInputBufferAddres;
        this.startInstructionAddress = startInstructionAddress;
        this.disk = disk;
        this.tempBuffSize = tempBuffSize;
        this.endOutputBufferAddress = endOutputBufferAddress;
        this.startInputBufferAddress = startInputBufferAddress;
        this.startTempBufferAddress = startTempBufferAddress;
        this.programFile = programFile;
        this.instructionsLength = instructionsLength;
        this.processList = processList;
        this.endInstructionAddress = endInstructionAddress;
        this.pid = pid;
        this.inputBuffSize = inputBuffSize;
        this.driver_drivers = driver_drivers;
    }

    public int getEndtempbufferaddress() {
        return endTempBufferAddress;
    }

    public void setEndtempbufferaddress(int endTempBufferAddress) {
        this.endTempBufferAddress = endTempBufferAddress;
    }
    public int getStartoutputbufferaddress() {
        return startOutputBufferAddress;
    }

    public void setStartoutputbufferaddress(int startOutputBufferAddress) {
        this.startOutputBufferAddress = startOutputBufferAddress;
    }
    public int getOutputbuffsize() {
        return outputBuffSize;
    }

    public void setOutputbuffsize(int outputBuffSize) {
        this.outputBuffSize = outputBuffSize;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public int getCurraddress() {
        return currAddress;
    }

    public void setCurraddress(int currAddress) {
        this.currAddress = currAddress;
    }
    public int getEndinputbufferaddres() {
        return endInputBufferAddres;
    }

    public void setEndinputbufferaddres(int endInputBufferAddres) {
        this.endInputBufferAddres = endInputBufferAddres;
    }
    public int getStartinstructionaddress() {
        return startInstructionAddress;
    }

    public void setStartinstructionaddress(int startInstructionAddress) {
        this.startInstructionAddress = startInstructionAddress;
    }
    public None getDisk() {
        return disk;
    }

    public void setDisk(None disk) {
        this.disk = disk;
    }
    public int getTempbuffsize() {
        return tempBuffSize;
    }

    public void setTempbuffsize(int tempBuffSize) {
        this.tempBuffSize = tempBuffSize;
    }
    public int getEndoutputbufferaddress() {
        return endOutputBufferAddress;
    }

    public void setEndoutputbufferaddress(int endOutputBufferAddress) {
        this.endOutputBufferAddress = endOutputBufferAddress;
    }
    public int getStartinputbufferaddress() {
        return startInputBufferAddress;
    }

    public void setStartinputbufferaddress(int startInputBufferAddress) {
        this.startInputBufferAddress = startInputBufferAddress;
    }
    public int getStarttempbufferaddress() {
        return startTempBufferAddress;
    }

    public void setStarttempbufferaddress(int startTempBufferAddress) {
        this.startTempBufferAddress = startTempBufferAddress;
    }
    public String getProgramfile() {
        return programFile;
    }

    public void setProgramfile(String programFile) {
        this.programFile = programFile;
    }
    public int getInstructionslength() {
        return instructionsLength;
    }

    public void setInstructionslength(int instructionsLength) {
        this.instructionsLength = instructionsLength;
    }
    public None getProcesslist() {
        return processList;
    }

    public void setProcesslist(None processList) {
        this.processList = processList;
    }
    public int getEndinstructionaddress() {
        return endInstructionAddress;
    }

    public void setEndinstructionaddress(int endInstructionAddress) {
        this.endInstructionAddress = endInstructionAddress;
    }
    public int getPid() {
        return pid;
    }

    public void setPid(int pid) {
        this.pid = pid;
    }
    public int getInputbuffsize() {
        return inputBuffSize;
    }

    public void setInputbuffsize(int inputBuffSize) {
        this.inputBuffSize = inputBuffSize;
    }

    public List<driver_Driver> getDriver_drivers() {
        return driver_drivers;
    }

    public void addDriver_driver(Driver_driver driver_driver) {
        this.driver_drivers.add(driver_driver);
    }

}