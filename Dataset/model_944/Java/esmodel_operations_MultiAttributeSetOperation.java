





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeSetOperation extends FeatureOperation {

    private String newValue;
    private String oldValue;
    private int index;



    public esmodel_operations_MultiAttributeSetOperation(
        String newValue,        String oldValue,        int index    ) {
        super(
        );
        this.newValue = newValue;
        this.oldValue = oldValue;
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
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }


}