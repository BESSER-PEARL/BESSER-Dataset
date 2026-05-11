





import java.util.List;
import java.util.ArrayList;

public class btsviewmodel_DBCollectionStatusInformation  {

    private String dbUpdateSeq;
    private String dbPurgeSeq;
    private String dbDocDelCount;
    private String syncStatusToRemote;
    private String indexUpdateSeq;
    private String dbDiskSize;
    private String syncStatusFromRemote;
    private String dbCollectionName;
    private String indexDocCount;
    private String indexStatus;
    private String dbDocCount;



    public btsviewmodel_DBCollectionStatusInformation(
        String dbUpdateSeq,        String dbPurgeSeq,        String dbDocDelCount,        String syncStatusToRemote,        String indexUpdateSeq,        String dbDiskSize,        String syncStatusFromRemote,        String dbCollectionName,        String indexDocCount,        String indexStatus,        String dbDocCount    ) {
        this.dbUpdateSeq = dbUpdateSeq;
        this.dbPurgeSeq = dbPurgeSeq;
        this.dbDocDelCount = dbDocDelCount;
        this.syncStatusToRemote = syncStatusToRemote;
        this.indexUpdateSeq = indexUpdateSeq;
        this.dbDiskSize = dbDiskSize;
        this.syncStatusFromRemote = syncStatusFromRemote;
        this.dbCollectionName = dbCollectionName;
        this.indexDocCount = indexDocCount;
        this.indexStatus = indexStatus;
        this.dbDocCount = dbDocCount;
    }


    public String getDbupdateseq() {
        return dbUpdateSeq;
    }

    public void setDbupdateseq(String dbUpdateSeq) {
        this.dbUpdateSeq = dbUpdateSeq;
    }
    public String getDbpurgeseq() {
        return dbPurgeSeq;
    }

    public void setDbpurgeseq(String dbPurgeSeq) {
        this.dbPurgeSeq = dbPurgeSeq;
    }
    public String getDbdocdelcount() {
        return dbDocDelCount;
    }

    public void setDbdocdelcount(String dbDocDelCount) {
        this.dbDocDelCount = dbDocDelCount;
    }
    public String getSyncstatustoremote() {
        return syncStatusToRemote;
    }

    public void setSyncstatustoremote(String syncStatusToRemote) {
        this.syncStatusToRemote = syncStatusToRemote;
    }
    public String getIndexupdateseq() {
        return indexUpdateSeq;
    }

    public void setIndexupdateseq(String indexUpdateSeq) {
        this.indexUpdateSeq = indexUpdateSeq;
    }
    public String getDbdisksize() {
        return dbDiskSize;
    }

    public void setDbdisksize(String dbDiskSize) {
        this.dbDiskSize = dbDiskSize;
    }
    public String getSyncstatusfromremote() {
        return syncStatusFromRemote;
    }

    public void setSyncstatusfromremote(String syncStatusFromRemote) {
        this.syncStatusFromRemote = syncStatusFromRemote;
    }
    public String getDbcollectionname() {
        return dbCollectionName;
    }

    public void setDbcollectionname(String dbCollectionName) {
        this.dbCollectionName = dbCollectionName;
    }
    public String getIndexdoccount() {
        return indexDocCount;
    }

    public void setIndexdoccount(String indexDocCount) {
        this.indexDocCount = indexDocCount;
    }
    public String getIndexstatus() {
        return indexStatus;
    }

    public void setIndexstatus(String indexStatus) {
        this.indexStatus = indexStatus;
    }
    public String getDbdoccount() {
        return dbDocCount;
    }

    public void setDbdoccount(String dbDocCount) {
        this.dbDocCount = dbDocCount;
    }


}