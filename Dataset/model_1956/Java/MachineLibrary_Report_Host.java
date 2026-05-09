





import java.util.List;
import java.util.ArrayList;

public class MachineLibrary_Report_Host  {

    private int maxType;
    private int stateChanged;
    private int sampleMoved;
    private int sendLifeMessages;
    private int minType;
    private int timeStamp;
    private int sampleInsert;
    private int rawData;
    private int internal;
    private int sendErrorWarningsMsgOnly;
    private int sampleRemoved;
    private String note1;
    private String fileName;
    private String note;





    private MachineLibrary_UnitConfig_Host machinelibrary_unitconfig_host;


    public MachineLibrary_Report_Host(
        int maxType,        int stateChanged,        int sampleMoved,        int sendLifeMessages,        int minType,        int timeStamp,        int sampleInsert,        int rawData,        int internal,        int sendErrorWarningsMsgOnly,        int sampleRemoved,        String note1,        String fileName,        String note    ) {
        this.maxType = maxType;
        this.stateChanged = stateChanged;
        this.sampleMoved = sampleMoved;
        this.sendLifeMessages = sendLifeMessages;
        this.minType = minType;
        this.timeStamp = timeStamp;
        this.sampleInsert = sampleInsert;
        this.rawData = rawData;
        this.internal = internal;
        this.sendErrorWarningsMsgOnly = sendErrorWarningsMsgOnly;
        this.sampleRemoved = sampleRemoved;
        this.note1 = note1;
        this.fileName = fileName;
        this.note = note;
    }


    public int getMaxtype() {
        return maxType;
    }

    public void setMaxtype(int maxType) {
        this.maxType = maxType;
    }
    public int getStatechanged() {
        return stateChanged;
    }

    public void setStatechanged(int stateChanged) {
        this.stateChanged = stateChanged;
    }
    public int getSamplemoved() {
        return sampleMoved;
    }

    public void setSamplemoved(int sampleMoved) {
        this.sampleMoved = sampleMoved;
    }
    public int getSendlifemessages() {
        return sendLifeMessages;
    }

    public void setSendlifemessages(int sendLifeMessages) {
        this.sendLifeMessages = sendLifeMessages;
    }
    public int getMintype() {
        return minType;
    }

    public void setMintype(int minType) {
        this.minType = minType;
    }
    public int getTimestamp() {
        return timeStamp;
    }

    public void setTimestamp(int timeStamp) {
        this.timeStamp = timeStamp;
    }
    public int getSampleinsert() {
        return sampleInsert;
    }

    public void setSampleinsert(int sampleInsert) {
        this.sampleInsert = sampleInsert;
    }
    public int getRawdata() {
        return rawData;
    }

    public void setRawdata(int rawData) {
        this.rawData = rawData;
    }
    public int getInternal() {
        return internal;
    }

    public void setInternal(int internal) {
        this.internal = internal;
    }
    public int getSenderrorwarningsmsgonly() {
        return sendErrorWarningsMsgOnly;
    }

    public void setSenderrorwarningsmsgonly(int sendErrorWarningsMsgOnly) {
        this.sendErrorWarningsMsgOnly = sendErrorWarningsMsgOnly;
    }
    public int getSampleremoved() {
        return sampleRemoved;
    }

    public void setSampleremoved(int sampleRemoved) {
        this.sampleRemoved = sampleRemoved;
    }
    public String getNote1() {
        return note1;
    }

    public void setNote1(String note1) {
        this.note1 = note1;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getNote() {
        return note;
    }

    public void setNote(String note) {
        this.note = note;
    }

    public MachineLibrary_UnitConfig_Host getMachinelibrary_unitconfig_host() {
        return machinelibrary_unitconfig_host;
    }

    public void setMachinelibrary_unitconfig_host(MachineLibrary_UnitConfig_Host machinelibrary_unitconfig_host) {
        this.machinelibrary_unitconfig_host = machinelibrary_unitconfig_host;
    }

}