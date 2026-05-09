





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeMoveOperation extends FeatureOperation {

    private String referencedValue;
    private int newIndex;
    private int oldIndex;



    public esmodel_operations_MultiAttributeMoveOperation(
        String referencedValue,        int newIndex,        int oldIndex    ) {
        super(
        );
        this.referencedValue = referencedValue;
        this.newIndex = newIndex;
        this.oldIndex = oldIndex;
    }


    public String getReferencedvalue() {
        return referencedValue;
    }

    public void setReferencedvalue(String referencedValue) {
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


}