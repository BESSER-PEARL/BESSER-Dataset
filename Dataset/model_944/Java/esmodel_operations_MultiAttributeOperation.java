





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeOperation extends FeatureOperation {

    private boolean add;
    private int indexes;
    private String referencedValues;



    public esmodel_operations_MultiAttributeOperation(
        boolean add,        int indexes,        String referencedValues    ) {
        super(
        );
        this.add = add;
        this.indexes = indexes;
        this.referencedValues = referencedValues;
    }


    public boolean getAdd() {
        return add;
    }

    public void setAdd(boolean add) {
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


}