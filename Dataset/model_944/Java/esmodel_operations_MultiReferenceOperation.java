





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiReferenceOperation extends ReferenceOperation {

    private int index;
    private boolean add;



    public esmodel_operations_MultiReferenceOperation(
        int index,        boolean add    ) {
        super(
        );
        this.index = index;
        this.add = add;
    }


    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }
    public boolean getAdd() {
        return add;
    }

    public void setAdd(boolean add) {
        this.add = add;
    }


}