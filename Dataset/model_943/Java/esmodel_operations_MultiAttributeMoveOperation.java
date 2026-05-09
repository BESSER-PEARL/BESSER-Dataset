





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeMoveOperation extends FeatureOperation {

    private int newIndex;
    private String referencedValue;
    private int oldIndex;



    public esmodel_operations_MultiAttributeMoveOperation(
        int newIndex,        String referencedValue,        int oldIndex    ) {
        super(
        );
        this.newIndex = newIndex;
        this.referencedValue = referencedValue;
        this.oldIndex = oldIndex;
    }


    public int getNewindex() {
        return newIndex;
    }

    public void setNewindex(int newIndex) {
        this.newIndex = newIndex;
    }
    public String getReferencedvalue() {
        return referencedValue;
    }

    public void setReferencedvalue(String referencedValue) {
        this.referencedValue = referencedValue;
    }
    public int getOldindex() {
        return oldIndex;
    }

    public void setOldindex(int oldIndex) {
        this.oldIndex = oldIndex;
    }


}