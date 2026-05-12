





import java.util.List;
import java.util.ArrayList;

public class driver_Loader  {

    private int endOutputBufferAddress;
    private int priority;
    private int tempBuffSize;
    private int startTempBufferAddress;
    private int endInputBufferAddres;
    private String programFile;
    private int outputBuffSize;
    private int inputBuffSize;
    private int currAddress;
    private None disk;
    private int startOutputBufferAddress;
    private int endInstructionAddress;
    private int pid;
    private int startInstructionAddress;
    private int instructionsLength;
    private int startInputBufferAddress;
    private None processList;
    private int endTempBufferAddress;





    private List<driver_Driver> driver_drivers;


    public driver_Loader(
        int endOutputBufferAddress,        int priority,        int tempBuffSize,        int startTempBufferAddress,        int endInputBufferAddres,        String programFile,        int outputBuffSize,        int inputBuffSize,        int currAddress,        None disk,        int startOutputBufferAddress,        int endInstructionAddress,        int pid,        int startInstructionAddress,        int instructionsLength,        int startInputBufferAddress,        None processList,        int endTempBufferAddress    ) {
        this.endOutputBufferAddress = endOutputBufferAddress;
        this.priority = priority;
        this.tempBuffSize = tempBuffSize;
        this.startTempBufferAddress = startTempBufferAddress;
        this.endInputBufferAddres = endInputBufferAddres;
        this.programFile = programFile;
        this.outputBuffSize = outputBuffSize;
        this.inputBuffSize = inputBuffSize;
        this.currAddress = currAddress;
        this.disk = disk;
        this.startOutputBufferAddress = startOutputBufferAddress;
        this.endInstructionAddress = endInstructionAddress;
        this.pid = pid;
        this.startInstructionAddress = startInstructionAddress;
        this.instructionsLength = instructionsLength;
        this.startInputBufferAddress = startInputBufferAddress;
        this.processList = processList;
        this.endTempBufferAddress = endTempBufferAddress;
        this.driver_drivers = new ArrayList<>();
    }

    public driver_Loader(
        int endOutputBufferAddress,        int priority,        int tempBuffSize,        int startTempBufferAddress,        int endInputBufferAddres,        String programFile,        int outputBuffSize,        int inputBuffSize,        int currAddress,        None disk,        int startOutputBufferAddress,        int endInstructionAddress,        int pid,        int startInstructionAddress,        int instructionsLength,        int startInputBufferAddress,        None processList,        int endTempBufferAddress        ArrayList<driver_Driver> driver_drivers    ) {
        this.endOutputBufferAddress = endOutputBufferAddress;
        this.priority = priority;
        this.tempBuffSize = tempBuffSize;
        this.startTempBufferAddress = startTempBufferAddress;
        this.endInputBufferAddres = endInputBufferAddres;
        this.programFile = programFile;
        this.outputBuffSize = outputBuffSize;
        this.inputBuffSize = inputBuffSize;
        this.currAddress = currAddress;
        this.disk = disk;
        this.startOutputBufferAddress = startOutputBufferAddress;
        this.endInstructionAddress = endInstructionAddress;
        this.pid = pid;
        this.startInstructionAddress = startInstructionAddress;
        this.instructionsLength = instructionsLength;
        this.startInputBufferAddress = startInputBufferAddress;
        this.processList = processList;
        this.endTempBufferAddress = endTempBufferAddress;
        this.driver_drivers = driver_drivers;
    }

    public int getEndoutputbufferaddress() {
        return endOutputBufferAddress;
    }

    public void setEndoutputbufferaddress(int endOutputBufferAddress) {
        this.endOutputBufferAddress = endOutputBufferAddress;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public int getTempbuffsize() {
        return tempBuffSize;
    }

    public void setTempbuffsize(int tempBuffSize) {
        this.tempBuffSize = tempBuffSize;
    }
    public int getStarttempbufferaddress() {
        return startTempBufferAddress;
    }

    public void setStarttempbufferaddress(int startTempBufferAddress) {
        this.startTempBufferAddress = startTempBufferAddress;
    }
    public int getEndinputbufferaddres() {
        return endInputBufferAddres;
    }

    public void setEndinputbufferaddres(int endInputBufferAddres) {
        this.endInputBufferAddres = endInputBufferAddres;
    }
    public String getProgramfile() {
        return programFile;
    }

    public void setProgramfile(String programFile) {
        this.programFile = programFile;
    }
    public int getOutputbuffsize() {
        return outputBuffSize;
    }

    public void setOutputbuffsize(int outputBuffSize) {
        this.outputBuffSize = outputBuffSize;
    }
    public int getInputbuffsize() {
        return inputBuffSize;
    }

    public void setInputbuffsize(int inputBuffSize) {
        this.inputBuffSize = inputBuffSize;
    }
    public int getCurraddress() {
        return currAddress;
    }

    public void setCurraddress(int currAddress) {
        this.currAddress = currAddress;
    }
    public None getDisk() {
        return disk;
    }

    public void setDisk(None disk) {
        this.disk = disk;
    }
    public int getStartoutputbufferaddress() {
        return startOutputBufferAddress;
    }

    public void setStartoutputbufferaddress(int startOutputBufferAddress) {
        this.startOutputBufferAddress = startOutputBufferAddress;
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
    public int getStartinstructionaddress() {
        return startInstructionAddress;
    }

    public void setStartinstructionaddress(int startInstructionAddress) {
        this.startInstructionAddress = startInstructionAddress;
    }
    public int getInstructionslength() {
        return instructionsLength;
    }

    public void setInstructionslength(int instructionsLength) {
        this.instructionsLength = instructionsLength;
    }
    public int getStartinputbufferaddress() {
        return startInputBufferAddress;
    }

    public void setStartinputbufferaddress(int startInputBufferAddress) {
        this.startInputBufferAddress = startInputBufferAddress;
    }
    public None getProcesslist() {
        return processList;
    }

    public void setProcesslist(None processList) {
        this.processList = processList;
    }
    public int getEndtempbufferaddress() {
        return endTempBufferAddress;
    }

    public void setEndtempbufferaddress(int endTempBufferAddress) {
        this.endTempBufferAddress = endTempBufferAddress;
    }

    public List<driver_Driver> getDriver_drivers() {
        return driver_drivers;
    }

    public void addDriver_driver(Driver_driver driver_driver) {
        this.driver_drivers.add(driver_driver);
    }

}