




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_DataSet  {

    private String cacheFileAttachements;
    private String logLevel;
    private String identPrefix;
    private LocalDate created;
    private LocalDate lastModified;
    private String cacheFolder;
    private String identCounter;



    public data_DataSet(
        String cacheFileAttachements,        String logLevel,        String identPrefix,        LocalDate created,        LocalDate lastModified,        String cacheFolder,        String identCounter    ) {
        this.cacheFileAttachements = cacheFileAttachements;
        this.logLevel = logLevel;
        this.identPrefix = identPrefix;
        this.created = created;
        this.lastModified = lastModified;
        this.cacheFolder = cacheFolder;
        this.identCounter = identCounter;
    }


    public String getCachefileattachements() {
        return cacheFileAttachements;
    }

    public void setCachefileattachements(String cacheFileAttachements) {
        this.cacheFileAttachements = cacheFileAttachements;
    }
    public String getLoglevel() {
        return logLevel;
    }

    public void setLoglevel(String logLevel) {
        this.logLevel = logLevel;
    }
    public String getIdentprefix() {
        return identPrefix;
    }

    public void setIdentprefix(String identPrefix) {
        this.identPrefix = identPrefix;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
    }
    public String getCachefolder() {
        return cacheFolder;
    }

    public void setCachefolder(String cacheFolder) {
        this.cacheFolder = cacheFolder;
    }
    public String getIdentcounter() {
        return identCounter;
    }

    public void setIdentcounter(String identCounter) {
        this.identCounter = identCounter;
    }


}