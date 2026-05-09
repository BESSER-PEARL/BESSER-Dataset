





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiAttributeOperation extends FeatureOperation {

    private boolean add;
    private String referencedValues;
    private int indexes;



    public esmodel_operations_MultiAttributeOperation(
        boolean add,        String referencedValues,        int indexes    ) {
        super(
        );
        this.add = add;
        this.referencedValues = referencedValues;
        this.indexes = indexes;
    }


    public boolean getAdd() {
        return add;
    }

    public void setAdd(boolean add) {
        this.add = add;
    }
    public String getReferencedvalues() {
        return referencedValues;
    }

    public void setReferencedvalues(String referencedValues) {
        this.referencedValues = referencedValues;
    }
    public int getIndexes() {
        return indexes;
    }

    public void setIndexes(int indexes) {
        this.indexes = indexes;
    }


}