





import java.util.List;
import java.util.ArrayList;

public class xmof_IntermediateActions_LinkEndDestructionData extends LinkEndData {

    private boolean destroyDuplicates;



    public xmof_IntermediateActions_LinkEndDestructionData(
        boolean destroyDuplicates    ) {
        super(
        );
        this.destroyDuplicates = destroyDuplicates;
    }


    public boolean getDestroyduplicates() {
        return destroyDuplicates;
    }

    public void setDestroyduplicates(boolean destroyDuplicates) {
        this.destroyDuplicates = destroyDuplicates;
    }


}