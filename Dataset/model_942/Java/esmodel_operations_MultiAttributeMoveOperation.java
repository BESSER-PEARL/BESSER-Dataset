





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeMoveOperation extends FeatureOperation {

    private int oldIndex;
    private String referencedValue;
    private int newIndex;



    public esmodel_operations_MultiAttributeMoveOperation(
        int oldIndex,        String referencedValue,        int newIndex    ) {
        super(
        );
        this.oldIndex = oldIndex;
        this.referencedValue = referencedValue;
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
    public int getNewindex() {
        return newIndex;
    }

    public void setNewindex(int newIndex) {
        this.newIndex = newIndex;
    }


}