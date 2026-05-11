





import java.util.List;
import java.util.ArrayList;

public class application_Mashup extends Source {

    private String sourceIdentCounter;
    private String backupIntervall;
    private String workingDirectory;
    private String backupDataSet;
    private String cacheDelay;
    private String cacheAttachments;
    private String cacheDataSet;
    private String keepDeletedItemsList;





    private application_Source application_source;




    private List<application_Source> application_sources;




    private application_Interface application_interface;




    private List<application_Interface> application_interfaces;


    public application_Mashup(
        String sourceIdentCounter,        String backupIntervall,        String workingDirectory,        String backupDataSet,        String cacheDelay,        String cacheAttachments,        String cacheDataSet,        String keepDeletedItemsList    ) {
        super(
        );
        this.sourceIdentCounter = sourceIdentCounter;
        this.backupIntervall = backupIntervall;
        this.workingDirectory = workingDirectory;
        this.backupDataSet = backupDataSet;
        this.cacheDelay = cacheDelay;
        this.cacheAttachments = cacheAttachments;
        this.cacheDataSet = cacheDataSet;
        this.keepDeletedItemsList = keepDeletedItemsList;
        this.application_sources = new ArrayList<>();
        this.application_interfaces = new ArrayList<>();
    }

    public application_Mashup(
        String sourceIdentCounter,        String backupIntervall,        String workingDirectory,        String backupDataSet,        String cacheDelay,        String cacheAttachments,        String cacheDataSet,        String keepDeletedItemsList        ArrayList<application_Source> application_sources,        ArrayList<application_Interface> application_interfaces    ) {
        this.sourceIdentCounter = sourceIdentCounter;
        this.backupIntervall = backupIntervall;
        this.workingDirectory = workingDirectory;
        this.backupDataSet = backupDataSet;
        this.cacheDelay = cacheDelay;
        this.cacheAttachments = cacheAttachments;
        this.cacheDataSet = cacheDataSet;
        this.keepDeletedItemsList = keepDeletedItemsList;
        this.application_sources = application_sources;
        this.application_interfaces = application_interfaces;
    }

    public String getSourceidentcounter() {
        return sourceIdentCounter;
    }

    public void setSourceidentcounter(String sourceIdentCounter) {
        this.sourceIdentCounter = sourceIdentCounter;
    }
    public String getBackupintervall() {
        return backupIntervall;
    }

    public void setBackupintervall(String backupIntervall) {
        this.backupIntervall = backupIntervall;
    }
    public String getWorkingdirectory() {
        return workingDirectory;
    }

    public void setWorkingdirectory(String workingDirectory) {
        this.workingDirectory = workingDirectory;
    }
    public String getBackupdataset() {
        return backupDataSet;
    }

    public void setBackupdataset(String backupDataSet) {
        this.backupDataSet = backupDataSet;
    }
    public String getCachedelay() {
        return cacheDelay;
    }

    public void setCachedelay(String cacheDelay) {
        this.cacheDelay = cacheDelay;
    }
    public String getCacheattachments() {
        return cacheAttachments;
    }

    public void setCacheattachments(String cacheAttachments) {
        this.cacheAttachments = cacheAttachments;
    }
    public String getCachedataset() {
        return cacheDataSet;
    }

    public void setCachedataset(String cacheDataSet) {
        this.cacheDataSet = cacheDataSet;
    }
    public String getKeepdeleteditemslist() {
        return keepDeletedItemsList;
    }

    public void setKeepdeleteditemslist(String keepDeletedItemsList) {
        this.keepDeletedItemsList = keepDeletedItemsList;
    }

    public application_Source getApplication_source() {
        return application_source;
    }

    public void setApplication_source(application_Source application_source) {
        this.application_source = application_source;
    }
    public List<application_Source> getApplication_sources() {
        return application_sources;
    }

    public void addApplication_source(Application_source application_source) {
        this.application_sources.add(application_source);
    }
    public application_Interface getApplication_interface() {
        return application_interface;
    }

    public void setApplication_interface(application_Interface application_interface) {
        this.application_interface = application_interface;
    }
    public List<application_Interface> getApplication_interfaces() {
        return application_interfaces;
    }

    public void addApplication_interface(Application_interface application_interface) {
        this.application_interfaces.add(application_interface);
    }

}