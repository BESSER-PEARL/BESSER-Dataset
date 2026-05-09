





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_AttributeOperation extends FeatureOperation {

    private String newValue;
    private String oldValue;



    public esmodel_operations_AttributeOperation(
        String newValue,        String oldValue    ) {
        super(
        );
        this.newValue = newValue;
        this.oldValue = oldValue;
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


}