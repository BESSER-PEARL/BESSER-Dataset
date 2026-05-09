





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeSetOperation extends FeatureOperation {

    private String newValue;
    private int index;
    private String oldValue;



    public esmodel_operations_MultiAttributeSetOperation(
        String newValue,        int index,        String oldValue    ) {
        super(
        );
        this.newValue = newValue;
        this.index = index;
        this.oldValue = oldValue;
    }


    public String getNewvalue() {
        return newValue;
    }

    public void setNewvalue(String newValue) {
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


}