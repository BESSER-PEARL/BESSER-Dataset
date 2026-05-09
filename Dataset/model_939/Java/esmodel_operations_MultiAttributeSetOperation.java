





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeSetOperation extends FeatureOperation {

    private int index;
    private String oldValue;
    private String newValue;



    public esmodel_operations_MultiAttributeSetOperation(
        int index,        String oldValue,        String newValue    ) {
        super(
        );
        this.index = index;
        this.oldValue = oldValue;
        this.newValue = newValue;
    }


    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public String getOldvalue() {
        return oldValue;
    }

    public void setOldvalue(String oldValue) {
        this.oldValue = oldValue;
    }
    public String getNewvalue() {
        return newValue;
    }

    public void setNewvalue(String newValue) {
        this.newValue = newValue;
    }


}