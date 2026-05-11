





import java.util.List;
import java.util.ArrayList;

public class model_history_Change  {

    private String objectType;
    private String feature;
    private boolean isCreate;
    private boolean isDelete;
    private String oldValue;
    private String objectName;
    private String newValue;



    public model_history_Change(
        String objectType,        String feature,        boolean isCreate,        boolean isDelete,        String oldValue,        String objectName,        String newValue    ) {
        this.objectType = objectType;
        this.feature = feature;
        this.isCreate = isCreate;
        this.isDelete = isDelete;
        this.oldValue = oldValue;
        this.objectName = objectName;
        this.newValue = newValue;
    }


    public String getObjecttype() {
        return objectType;
    }

    public void setObjecttype(String objectType) {
        this.objectType = objectType;
    }
    public String getFeature() {
        return feature;
    }

    public void setFeature(String feature) {
        this.feature = feature;
    }
    public boolean getIscreate() {
        return isCreate;
    }

    public void setIscreate(boolean isCreate) {
        this.isCreate = isCreate;
    }
    public boolean getIsdelete() {
        return isDelete;
    }

    public void setIsdelete(boolean isDelete) {
        this.isDelete = isDelete;
    }
    public String getOldvalue() {
        return oldValue;
    }

    public void setOldvalue(String oldValue) {
        this.oldValue = oldValue;
    }
    public String getObjectname() {
        return objectName;
    }

    public void setObjectname(String objectName) {
        this.objectName = objectName;
    }
    public String getNewvalue() {
        return newValue;
    }

    public void setNewvalue(String newValue) {
        this.newValue = newValue;
    }


}