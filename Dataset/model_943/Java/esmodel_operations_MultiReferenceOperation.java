





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiReferenceOperation extends ReferenceOperation {

    private int index;
    private boolean add;





    private List<ModelElementId> modelelementids;


    public esmodel_operations_MultiReferenceOperation(
        int index,        boolean add    ) {
        super(
        );
        this.index = index;
        this.add = add;
        this.modelelementids = new ArrayList<>();
    }

    public esmodel_operations_MultiReferenceOperation(
        int index,        boolean add        ArrayList<ModelElementId> modelelementids    ) {
        this.index = index;
        this.add = add;
        this.modelelementids = modelelementids;
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

    public List<ModelElementId> getModelelementids() {
        return modelelementids;
    }

    public void addModelelementid(Modelelementid modelelementid) {
        this.modelelementids.add(modelelementid);
    }

}