




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_DataSet  {

    private String identCounter;
    private String identPrefix;
    private LocalDate lastModified;
    private LocalDate created;
    private String logLevel;
    private String cacheFolder;
    private String cacheFileAttachements;



    public data_DataSet(
        String identCounter,        String identPrefix,        LocalDate lastModified,        LocalDate created,        String logLevel,        String cacheFolder,        String cacheFileAttachements    ) {
        this.identCounter = identCounter;
        this.identPrefix = identPrefix;
        this.lastModified = lastModified;
        this.created = created;
        this.logLevel = logLevel;
        this.cacheFolder = cacheFolder;
        this.cacheFileAttachements = cacheFileAttachements;
    }


    public String getIdentcounter() {
        return identCounter;
    }

    public void setIdentcounter(String identCounter) {
        this.identCounter = identCounter;
    }
    public String getIdentprefix() {
        return identPrefix;
    }

    public void setIdentprefix(String identPrefix) {
        this.identPrefix = identPrefix;
    }
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public String getLoglevel() {
        return logLevel;
    }

    public void setLoglevel(String logLevel) {
        this.logLevel = logLevel;
    }
    public String getCachefolder() {
        return cacheFolder;
    }

    public void setCachefolder(String cacheFolder) {
        this.cacheFolder = cacheFolder;
    }
    public String getCachefileattachements() {
        return cacheFileAttachements;
    }

    public void setCachefileattachements(String cacheFileAttachements) {
        this.cacheFileAttachements = cacheFileAttachements;
    }


}