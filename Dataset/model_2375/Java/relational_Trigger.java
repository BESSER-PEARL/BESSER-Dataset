





import java.util.List;
import java.util.ArrayList;

public class relational_Trigger extends SQLObject {

    private boolean insertType;
    private String actionTime;
    private boolean updateType;
    private boolean deleteType;



    public relational_Trigger(
        boolean insertType,        String actionTime,        boolean updateType,        boolean deleteType    ) {
        super(
        );
        this.insertType = insertType;
        this.actionTime = actionTime;
        this.updateType = updateType;
        this.deleteType = deleteType;
    }


    public boolean getInserttype() {
        return insertType;
    }

    public void setInserttype(boolean insertType) {
        this.insertType = insertType;
    }
    public String getActiontime() {
        return actionTime;
    }

    public void setActiontime(String actionTime) {
        this.actionTime = actionTime;
    }
    public boolean getUpdatetype() {
        return updateType;
    }

    public void setUpdatetype(boolean updateType) {
        this.updateType = updateType;
    }
    public boolean getDeletetype() {
        return deleteType;
    }

    public void setDeletetype(boolean deleteType) {
        this.deleteType = deleteType;
    }


}