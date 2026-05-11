





import java.util.List;
import java.util.ArrayList;

public class application_Mashup extends Source {

    private String backupIntervall;
    private String cacheDelay;
    private String sourceIdentCounter;
    private String workingDirectory;
    private String backupDataSet;
    private String cacheAttachments;
    private String cacheDataSet;





    private List<application_Source> application_sources;




    private List<application_MashupAdmin> application_mashupadmins;




    private List<application_Interface> application_interfaces;




    private application_Source application_source;




    private application_Interface application_interface;




    private application_MashupAdmin application_mashupadmin;


    public application_Mashup(
        String backupIntervall,        String cacheDelay,        String sourceIdentCounter,        String workingDirectory,        String backupDataSet,        String cacheAttachments,        String cacheDataSet    ) {
        super(
        );
        this.backupIntervall = backupIntervall;
        this.cacheDelay = cacheDelay;
        this.sourceIdentCounter = sourceIdentCounter;
        this.workingDirectory = workingDirectory;
        this.backupDataSet = backupDataSet;
        this.cacheAttachments = cacheAttachments;
        this.cacheDataSet = cacheDataSet;
        this.application_sources = new ArrayList<>();
        this.application_mashupadmins = new ArrayList<>();
        this.application_interfaces = new ArrayList<>();
    }

    public application_Mashup(
        String backupIntervall,        String cacheDelay,        String sourceIdentCounter,        String workingDirectory,        String backupDataSet,        String cacheAttachments,        String cacheDataSet        ArrayList<application_Source> application_sources,        ArrayList<application_MashupAdmin> application_mashupadmins,        ArrayList<application_Interface> application_interfaces    ) {
        this.backupIntervall = backupIntervall;
        this.cacheDelay = cacheDelay;
        this.sourceIdentCounter = sourceIdentCounter;
        this.workingDirectory = workingDirectory;
        this.backupDataSet = backupDataSet;
        this.cacheAttachments = cacheAttachments;
        this.cacheDataSet = cacheDataSet;
        this.application_sources = application_sources;
        this.application_mashupadmins = application_mashupadmins;
        this.application_interfaces = application_interfaces;
    }

    public String getBackupintervall() {
        return backupIntervall;
    }

    public void setBackupintervall(String backupIntervall) {
        this.backupIntervall = backupIntervall;
    }
    public String getCachedelay() {
        return cacheDelay;
    }

    public void setCachedelay(String cacheDelay) {
        this.cacheDelay = cacheDelay;
    }
    public String getSourceidentcounter() {
        return sourceIdentCounter;
    }

    public void setSourceidentcounter(String sourceIdentCounter) {
        this.sourceIdentCounter = sourceIdentCounter;
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

    public List<application_Source> getApplication_sources() {
        return application_sources;
    }

    public void addApplication_source(Application_source application_source) {
        this.application_sources.add(application_source);
    }
    public List<application_MashupAdmin> getApplication_mashupadmins() {
        return application_mashupadmins;
    }

    public void addApplication_mashupadmin(Application_mashupadmin application_mashupadmin) {
        this.application_mashupadmins.add(application_mashupadmin);
    }
    public List<application_Interface> getApplication_interfaces() {
        return application_interfaces;
    }

    public void addApplication_interface(Application_interface application_interface) {
        this.application_interfaces.add(application_interface);
    }
    public application_Source getApplication_source() {
        return application_source;
    }

    public void setApplication_source(application_Source application_source) {
        this.application_source = application_source;
    }
    public application_Interface getApplication_interface() {
        return application_interface;
    }

    public void setApplication_interface(application_Interface application_interface) {
        this.application_interface = application_interface;
    }
    public application_MashupAdmin getApplication_mashupadmin() {
        return application_mashupadmin;
    }

    public void setApplication_mashupadmin(application_MashupAdmin application_mashupadmin) {
        this.application_mashupadmin = application_mashupadmin;
    }

}