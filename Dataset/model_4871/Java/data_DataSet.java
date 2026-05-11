




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class data_DataSet  {

    private String identCounter;
    private LocalDate created;
    private String cacheFolder;
    private String logLevel;
    private String identPrefix;
    private LocalDate lastModified;
    private String keepDeletedItemsList;
    private String cacheFileAttachements;





    private List<data_DeletedItem> data_deleteditems;


    public data_DataSet(
        String identCounter,        LocalDate created,        String cacheFolder,        String logLevel,        String identPrefix,        LocalDate lastModified,        String keepDeletedItemsList,        String cacheFileAttachements    ) {
        this.identCounter = identCounter;
        this.created = created;
        this.cacheFolder = cacheFolder;
        this.logLevel = logLevel;
        this.identPrefix = identPrefix;
        this.lastModified = lastModified;
        this.keepDeletedItemsList = keepDeletedItemsList;
        this.cacheFileAttachements = cacheFileAttachements;
        this.data_deleteditems = new ArrayList<>();
    }

    public data_DataSet(
        String identCounter,        LocalDate created,        String cacheFolder,        String logLevel,        String identPrefix,        LocalDate lastModified,        String keepDeletedItemsList,        String cacheFileAttachements        ArrayList<data_DeletedItem> data_deleteditems    ) {
        this.identCounter = identCounter;
        this.created = created;
        this.cacheFolder = cacheFolder;
        this.logLevel = logLevel;
        this.identPrefix = identPrefix;
        this.lastModified = lastModified;
        this.keepDeletedItemsList = keepDeletedItemsList;
        this.cacheFileAttachements = cacheFileAttachements;
        this.data_deleteditems = data_deleteditems;
    }

    public String getIdentcounter() {
        return identCounter;
    }

    public void setIdentcounter(String identCounter) {
        this.identCounter = identCounter;
    }
    public LocalDate getCreated() {
        return created;
    }

    public void setCreated(LocalDate created) {
        this.created = created;
    }
    public String getCachefolder() {
        return cacheFolder;
    }

    public void setCachefolder(String cacheFolder) {
        this.cacheFolder = cacheFolder;
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
    public LocalDate getLastmodified() {
        return lastModified;
    }

    public void setLastmodified(LocalDate lastModified) {
        this.lastModified = lastModified;
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

    public List<data_DeletedItem> getData_deleteditems() {
        return data_deleteditems;
    }

    public void addData_deleteditem(Data_deleteditem data_deleteditem) {
        this.data_deleteditems.add(data_deleteditem);
    }

}