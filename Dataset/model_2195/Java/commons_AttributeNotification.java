





import java.util.List;
import java.util.ArrayList;

public class commons_AttributeNotification  {

    private String newValue;
    private String oldValue;
    private String object;



    public commons_AttributeNotification(
        String newValue,        String oldValue,        String object    ) {
        this.newValue = newValue;
        this.oldValue = oldValue;
        this.object = object;
    }


    public String getNewvalue() {
        return newValue;
    }

    public void setNewvalue(String newValue) {
        this.newValue = newValue;
    }
    public String getOldvalue() {
        return oldValue;
    }

    public void setOldvalue(String oldValue) {
        this.oldValue = oldValue;
    }
    public String getObject() {
        return object;
    }

    public void setObject(String object) {
        this.object = object;
    }


}