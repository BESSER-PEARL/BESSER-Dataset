




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_DataSet  {

    private LocalDate lastModified;
    private String logLevel;
    private String cacheFolder;
    private String identPrefix;
    private String identCounter;
    private String keepDeletedItemsList;
    private String cacheFileAttachements;
    private LocalDate created;





    private List<data_DeletedItem> data_deleteditems;


    public data_DataSet(
        LocalDate lastModified,        String logLevel,        String cacheFolder,        String identPrefix,        String identCounter,        String keepDeletedItemsList,        String cacheFileAttachements,        LocalDate created    ) {
        this.lastModified = lastModified;
        this.logLevel = logLevel;
        this.cacheFolder = cacheFolder;
        this.identPrefix = identPrefix;
        this.identCounter = identCounter;
        this.keepDeletedItemsList = keepDeletedItemsList;
        this.cacheFileAttachements = cacheFileAttachements;
        this.created = created;
        this.data_deleteditems = new ArrayList<>();
    }

    public data_DataSet(
        LocalDate lastModified,        String logLevel,        String cacheFolder,        String identPrefix,        String identCounter,        String keepDeletedItemsList,        String cacheFileAttachements,        LocalDate created        ArrayList<data_DeletedItem> data_deleteditems    ) {
        this.lastModified = lastModified;
        this.logLevel = logLevel;
        this.cacheFolder = cacheFolder;
        this.identPrefix = identPrefix;
        this.identCounter = identCounter;
        this.keepDeletedItemsList = keepDeletedItemsList;
        this.cacheFileAttachements = cacheFileAttachements;
        this.created = created;
        this.data_deleteditems = data_deleteditems;
    }

    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
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
    public String getIdentprefix() {
        return identPrefix;
    }

    public void setIdentprefix(String identPrefix) {
        this.identPrefix = identPrefix;
    }
    public String getIdentcounter() {
        return identCounter;
    }

    public void setIdentcounter(String identCounter) {
        this.identCounter = identCounter;
    }
    public String getKeepdeleteditemslist() {
        return keepDeletedItemsList;
    }

    public void setKeepdeleteditemslist(String keepDeletedItemsList) {
        this.keepDeletedItemsList = keepDeletedItemsList;
    }
    public String getCachefileattachements() {
        return cacheFileAttachements;
    }

    public void setCachefileattachements(String cacheFileAttachements) {
        this.cacheFileAttachements = cacheFileAttachements;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }

    public List<data_DeletedItem> getData_deleteditems() {
        return data_deleteditems;
    }

    public void addData_deleteditem(Data_deleteditem data_deleteditem) {
        this.data_deleteditems.add(data_deleteditem);
    }

}