





import java.util.List;
import java.util.ArrayList;

public class esmodel_operations_MultiReferenceMoveOperation extends FeatureOperation {

    private int newIndex;
    private int oldIndex;





    private ModelElementId modelelementid;


    public esmodel_operations_MultiReferenceMoveOperation(
        int newIndex,        int oldIndex    ) {
        super(
        );
        this.newIndex = newIndex;
        this.oldIndex = oldIndex;
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

    public ModelElementId getModelelementid() {
        return modelelementid;
    }

    public void setModelelementid(ModelElementId modelelementid) {
        this.modelelementid = modelelementid;
    }

}