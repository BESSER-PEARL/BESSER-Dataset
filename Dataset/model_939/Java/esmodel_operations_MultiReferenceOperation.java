





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiReferenceOperation extends ReferenceOperation {

    private boolean add;
    private int index;





    private List<ModelElementId> modelelementids;


    public esmodel_operations_MultiReferenceOperation(
        boolean add,        int index    ) {
        super(
        );
        this.add = add;
        this.index = index;
        this.modelelementids = new ArrayList<>();
    }

    public esmodel_operations_MultiReferenceOperation(
        boolean add,        int index        ArrayList<ModelElementId> modelelementids    ) {
        this.add = add;
        this.index = index;
        this.modelelementids = modelelementids;
    }

    public boolean getAdd() {
        return add;
    }

    public void setAdd(boolean add) {
        this.add = add;
    }
    public int getIndex() {
        return index;
    }

    public void setIndex(int index) {
        this.index = index;
    }

    public List<ModelElementId> getModelelementids() {
        return modelelementids;
    }

    public void addModelelementid(Modelelementid modelelementid) {
        this.modelelementids.add(modelelementid);
    }

}