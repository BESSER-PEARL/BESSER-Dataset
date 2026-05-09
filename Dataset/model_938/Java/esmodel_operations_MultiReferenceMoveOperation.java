





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiReferenceMoveOperation extends FeatureOperation {

    private int oldIndex;
    private int newIndex;





    private ModelElementId modelelementid;


    public esmodel_operations_MultiReferenceMoveOperation(
        int oldIndex,        int newIndex    ) {
        super(
        );
        this.oldIndex = oldIndex;
        this.newIndex = newIndex;
    }


    public int getOldindex() {
        return oldIndex;
    }

    public void setOldindex(int oldIndex) {
        this.oldIndex = oldIndex;
    }
    public int getNewindex() {
        return newIndex;
    }

    public void setNewindex(int newIndex) {
        this.newIndex = newIndex;
    }

    public ModelElementId getModelelementid() {
        return modelelementid;
    }

    public void setModelelementid(ModelElementId modelelementid) {
        this.modelelementid = modelelementid;
    }

}