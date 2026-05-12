





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_tables_Trigger extends SQLObject {

    private String oldRow;
    private String newRow;
    private String newTable;
    private boolean deleteType;
    private String oldTable;
    private boolean updateType;
    private String actionTime;
    private boolean insertType;
    private String timeStamp;
    private String actionGranularity;



    public sqlmodel_tables_Trigger(
        String oldRow,        String newRow,        String newTable,        boolean deleteType,        String oldTable,        boolean updateType,        String actionTime,        boolean insertType,        String timeStamp,        String actionGranularity    ) {
        super(
        );
        this.oldRow = oldRow;
        this.newRow = newRow;
        this.newTable = newTable;
        this.deleteType = deleteType;
        this.oldTable = oldTable;
        this.updateType = updateType;
        this.actionTime = actionTime;
        this.insertType = insertType;
        this.timeStamp = timeStamp;
        this.actionGranularity = actionGranularity;
    }


    public String getOldrow() {
        return oldRow;
    }

    public void setOldrow(String oldRow) {
        this.oldRow = oldRow;
    }
    public String getNewrow() {
        return newRow;
    }

    public void setNewrow(String newRow) {
        this.newRow = newRow;
    }
    public String getNewtable() {
        return newTable;
    }

    public void setNewtable(String newTable) {
        this.newTable = newTable;
    }
    public boolean getDeletetype() {
        return deleteType;
    }

    public void setDeletetype(boolean deleteType) {
        this.deleteType = deleteType;
    }
    public String getOldtable() {
        return oldTable;
    }

    public void setOldtable(String oldTable) {
        this.oldTable = oldTable;
    }
    public boolean getUpdatetype() {
        return updateType;
    }

    public void setUpdatetype(boolean updateType) {
        this.updateType = updateType;
    }
    public String getActiontime() {
        return actionTime;
    }

    public void setActiontime(String actionTime) {
        this.actionTime = actionTime;
    }
    public boolean getInserttype() {
        return insertType;
    }

    public void setInserttype(boolean insertType) {
        this.insertType = insertType;
    }
    public String getTimestamp() {
        return timeStamp;
    }

    public void setTimestamp(String timeStamp) {
        this.timeStamp = timeStamp;
    }
    public String getActiongranularity() {
        return actionGranularity;
    }

    public void setActiongranularity(String actionGranularity) {
        this.actionGranularity = actionGranularity;
    }


}