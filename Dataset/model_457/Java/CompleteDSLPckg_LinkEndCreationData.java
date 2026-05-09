





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_LinkEndCreationData extends LinkEndData {

    private boolean isReplaceAll;





    private CompleteDSLPckg_InputPin completedslpckg_inputpin;


    public CompleteDSLPckg_LinkEndCreationData(
        boolean isReplaceAll    ) {
        super(
        );
        this.isReplaceAll = isReplaceAll;
    }


    public boolean getIsreplaceall() {
        return isReplaceAll;
    }

    public void setIsreplaceall(boolean isReplaceAll) {
        this.isReplaceAll = isReplaceAll;
    }

    public CompleteDSLPckg_InputPin getCompletedslpckg_inputpin() {
        return completedslpckg_inputpin;
    }

    public void setCompletedslpckg_inputpin(CompleteDSLPckg_InputPin completedslpckg_inputpin) {
        this.completedslpckg_inputpin = completedslpckg_inputpin;
    }

}