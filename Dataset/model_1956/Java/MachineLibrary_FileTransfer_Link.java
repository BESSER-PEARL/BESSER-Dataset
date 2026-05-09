





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_FileTransfer_Link  {

    private String timeoutwrite;
    private int flagWriteAfterReading;
    private int flagToWriteWaitFor;
    private String delimiter;
    private int sendBuffer;
    private int flagToWriteWaitForDeleted;
    private int pollTime;
    private String readPath;
    private String writePath;
    private int writeAfterReading;
    private int receiveBuffer;
    private int translation;
    private int flagDelAfterReading;
    private int maxDataLength;
    private String toWriteWaitFor;
    private String delimter;





    private MachineLibrary_LinkConfig machinelibrary_linkconfig;


    public MachineLibrary_FileTransfer_Link(
        String timeoutwrite,        int flagWriteAfterReading,        int flagToWriteWaitFor,        String delimiter,        int sendBuffer,        int flagToWriteWaitForDeleted,        int pollTime,        String readPath,        String writePath,        int writeAfterReading,        int receiveBuffer,        int translation,        int flagDelAfterReading,        int maxDataLength,        String toWriteWaitFor,        String delimter    ) {
        this.timeoutwrite = timeoutwrite;
        this.flagWriteAfterReading = flagWriteAfterReading;
        this.flagToWriteWaitFor = flagToWriteWaitFor;
        this.delimiter = delimiter;
        this.sendBuffer = sendBuffer;
        this.flagToWriteWaitForDeleted = flagToWriteWaitForDeleted;
        this.pollTime = pollTime;
        this.readPath = readPath;
        this.writePath = writePath;
        this.writeAfterReading = writeAfterReading;
        this.receiveBuffer = receiveBuffer;
        this.translation = translation;
        this.flagDelAfterReading = flagDelAfterReading;
        this.maxDataLength = maxDataLength;
        this.toWriteWaitFor = toWriteWaitFor;
        this.delimter = delimter;
    }


    public String getTimeoutwrite() {
        return timeoutwrite;
    }

    public void setTimeoutwrite(String timeoutwrite) {
        this.timeoutwrite = timeoutwrite;
    }
    public int getFlagwriteafterreading() {
        return flagWriteAfterReading;
    }

    public void setFlagwriteafterreading(int flagWriteAfterReading) {
        this.flagWriteAfterReading = flagWriteAfterReading;
    }
    public int getFlagtowritewaitfor() {
        return flagToWriteWaitFor;
    }

    public void setFlagtowritewaitfor(int flagToWriteWaitFor) {
        this.flagToWriteWaitFor = flagToWriteWaitFor;
    }
    public String getDelimiter() {
        return delimiter;
    }

    public void setDelimiter(String delimiter) {
        this.delimiter = delimiter;
    }
    public int getSendbuffer() {
        return sendBuffer;
    }

    public void setSendbuffer(int sendBuffer) {
        this.sendBuffer = sendBuffer;
    }
    public int getFlagtowritewaitfordeleted() {
        return flagToWriteWaitForDeleted;
    }

    public void setFlagtowritewaitfordeleted(int flagToWriteWaitForDeleted) {
        this.flagToWriteWaitForDeleted = flagToWriteWaitForDeleted;
    }
    public int getPolltime() {
        return pollTime;
    }

    public void setPolltime(int pollTime) {
        this.pollTime = pollTime;
    }
    public String getReadpath() {
        return readPath;
    }

    public void setReadpath(String readPath) {
        this.readPath = readPath;
    }
    public String getWritepath() {
        return writePath;
    }

    public void setWritepath(String writePath) {
        this.writePath = writePath;
    }
    public int getWriteafterreading() {
        return writeAfterReading;
    }

    public void setWriteafterreading(int writeAfterReading) {
        this.writeAfterReading = writeAfterReading;
    }
    public int getReceivebuffer() {
        return receiveBuffer;
    }

    public void setReceivebuffer(int receiveBuffer) {
        this.receiveBuffer = receiveBuffer;
    }
    public int getTranslation() {
        return translation;
    }

    public void setTranslation(int translation) {
        this.translation = translation;
    }
    public int getFlagdelafterreading() {
        return flagDelAfterReading;
    }

    public void setFlagdelafterreading(int flagDelAfterReading) {
        this.flagDelAfterReading = flagDelAfterReading;
    }
    public int getMaxdatalength() {
        return maxDataLength;
    }

    public void setMaxdatalength(int maxDataLength) {
        this.maxDataLength = maxDataLength;
    }
    public String getTowritewaitfor() {
        return toWriteWaitFor;
    }

    public void setTowritewaitfor(String toWriteWaitFor) {
        this.toWriteWaitFor = toWriteWaitFor;
    }
    public String getDelimter() {
        return delimter;
    }

    public void setDelimter(String delimter) {
        this.delimter = delimter;
    }

    public MachineLibrary_LinkConfig getMachinelibrary_linkconfig() {
        return machinelibrary_linkconfig;
    }

    public void setMachinelibrary_linkconfig(MachineLibrary_LinkConfig machinelibrary_linkconfig) {
        this.machinelibrary_linkconfig = machinelibrary_linkconfig;
    }

}