





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeSetOperation extends FeatureOperation {

    private String oldValue;
    private int index;
    private String newValue;



    public esmodel_operations_MultiAttributeSetOperation(
        String oldValue,        int index,        String newValue    ) {
        super(
        );
        this.oldValue = oldValue;
        this.index = index;
        this.newValue = newValue;
    }


    public String getOldvalue() {
        return oldValue;
    }

    public void setOldvalue(String oldValue) {
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


}