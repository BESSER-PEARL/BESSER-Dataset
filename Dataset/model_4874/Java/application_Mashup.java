





import java.util.List;
import java.util.ArrayList;

public class application_Mashup extends Source {

    private String cacheAttachments;
    private String backupDataSet;
    private String backupIntervall;
    private String sourceIdentCounter;
    private String cacheDataSet;
    private String cacheDelay;
    private String workingDirectory;
    private String keepDeletedItemsList;



    public application_Mashup(
        String cacheAttachments,        String backupDataSet,        String backupIntervall,        String sourceIdentCounter,        String cacheDataSet,        String cacheDelay,        String workingDirectory,        String keepDeletedItemsList    ) {
        super(
        );
        this.cacheAttachments = cacheAttachments;
        this.backupDataSet = backupDataSet;
        this.backupIntervall = backupIntervall;
        this.sourceIdentCounter = sourceIdentCounter;
        this.cacheDataSet = cacheDataSet;
        this.cacheDelay = cacheDelay;
        this.workingDirectory = workingDirectory;
        this.keepDeletedItemsList = keepDeletedItemsList;
    }


    public String getCacheattachments() {
        return cacheAttachments;
    }

    public void setCacheattachments(String cacheAttachments) {
        this.cacheAttachments = cacheAttachments;
    }
    public String getBackupdataset() {
        return backupDataSet;
    }

    public void setBackupdataset(String backupDataSet) {
        this.backupDataSet = backupDataSet;
    }
    public String getBackupintervall() {
        return backupIntervall;
    }

    public void setBackupintervall(String backupIntervall) {
        this.backupIntervall = backupIntervall;
    }
    public String getSourceidentcounter() {
        return sourceIdentCounter;
    }

    public void setSourceidentcounter(String sourceIdentCounter) {
        this.sourceIdentCounter = sourceIdentCounter;
    }
    public String getCachedataset() {
        return cacheDataSet;
    }

    public void setCachedataset(String cacheDataSet) {
        this.cacheDataSet = cacheDataSet;
    }
    public String getCachedelay() {
        return cacheDelay;
    }

    public void setCachedelay(String cacheDelay) {
        this.cacheDelay = cacheDelay;
    }
    public String getWorkingdirectory() {
        return workingDirectory;
    }

    public void setWorkingdirectory(String workingDirectory) {
        this.workingDirectory = workingDirectory;
    }
    public String getKeepdeleteditemslist() {
        return keepDeletedItemsList;
    }

    public void setKeepdeleteditemslist(String keepDeletedItemsList) {
        this.keepDeletedItemsList = keepDeletedItemsList;
    }


}