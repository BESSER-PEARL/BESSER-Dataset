





import java.util.List;
import java.util.ArrayList;

public class relational_Trigger extends SQLObject {

    private boolean updateType;
    private boolean deleteType;
    private String actionTime;
    private boolean insertType;



    public relational_Trigger(
        boolean updateType,        boolean deleteType,        String actionTime,        boolean insertType    ) {
        super(
        );
        this.updateType = updateType;
        this.deleteType = deleteType;
        this.actionTime = actionTime;
        this.insertType = insertType;
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


}