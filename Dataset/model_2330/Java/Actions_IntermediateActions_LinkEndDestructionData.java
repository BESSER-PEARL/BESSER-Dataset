





import java.util.List;
import java.util.ArrayList;

public class Actions_IntermediateActions_LinkEndDestructionData extends LinkEndData {

    private boolean isDestroyDuplicates;



    public Actions_IntermediateActions_LinkEndDestructionData(
        boolean isDestroyDuplicates    ) {
        super(
        );
        this.isDestroyDuplicates = isDestroyDuplicates;
    }


    public boolean getIsdestroyduplicates() {
        return isDestroyDuplicates;
    }

    public void setIsdestroyduplicates(boolean isDestroyDuplicates) {
        this.isDestroyDuplicates = isDestroyDuplicates;
    }


}