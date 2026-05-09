





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeMoveOperation extends FeatureOperation {

    private int newIndex;
    private int oldIndex;
    private String referencedValue;



    public esmodel_operations_MultiAttributeMoveOperation(
        int newIndex,        int oldIndex,        String referencedValue    ) {
        super(
        );
        this.newIndex = newIndex;
        this.oldIndex = oldIndex;
        this.referencedValue = referencedValue;
    }


    public int getNewindex() {
        return newIndex;
    }

    public void setNewindex(int newIndex) {
        this.newIndex = newIndex;
    }
    public int getOldindex() {
        return oldIndex;
    }

    public void setOldindex(int oldIndex) {
        this.oldIndex = oldIndex;
    }
    public String getReferencedvalue() {
        return referencedValue;
    }

    public void setReferencedvalue(String referencedValue) {
        this.referencedValue = referencedValue;
    }


}