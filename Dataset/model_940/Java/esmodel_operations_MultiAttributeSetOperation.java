





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeSetOperation extends FeatureOperation {

    private int index;
    private String newValue;
    private String oldValue;



    public esmodel_operations_MultiAttributeSetOperation(
        int index,        String newValue,        String oldValue    ) {
        super(
        );
        this.index = index;
        this.newValue = newValue;
        this.oldValue = oldValue;
    }


    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
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