





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_LinkEndDestructionData extends LinkEndData {

    private boolean isDestroyDuplicates;





    private CompleteDSLPckg_InputPin completedslpckg_inputpin;


    public CompleteDSLPckg_LinkEndDestructionData(
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

    public CompleteDSLPckg_InputPin getCompletedslpckg_inputpin() {
        return completedslpckg_inputpin;
    }

    public void setCompletedslpckg_inputpin(CompleteDSLPckg_InputPin completedslpckg_inputpin) {
        this.completedslpckg_inputpin = completedslpckg_inputpin;
    }

}