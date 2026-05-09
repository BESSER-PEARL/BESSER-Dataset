





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeOperation extends FeatureOperation {

    private int indexes;
    private String referencedValues;
    private boolean add;



    public esmodel_operations_MultiAttributeOperation(
        int indexes,        String referencedValues,        boolean add    ) {
        super(
        );
        this.indexes = indexes;
        this.referencedValues = referencedValues;
        this.add = add;
    }


    public int getIndexes() {
        return indexes;
    }

    public void setIndexes(int indexes) {
        this.indexes = indexes;
    }
    public String getReferencedvalues() {
        return referencedValues;
    }

    public void setReferencedvalues(String referencedValues) {
        this.referencedValues = referencedValues;
    }
    public boolean getAdd() {
        return add;
    }

    public void setAdd(boolean add) {
        this.add = add;
    }


}