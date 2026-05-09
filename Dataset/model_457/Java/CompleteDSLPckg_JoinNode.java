





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_JoinNode extends ControlNode {

    private boolean isCombineDuplicate;





    private CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification;


    public CompleteDSLPckg_JoinNode(
        boolean isCombineDuplicate    ) {
        super(
        );
        this.isCombineDuplicate = isCombineDuplicate;
    }


    public boolean getIscombineduplicate() {
        return isCombineDuplicate;
    }

    public void setIscombineduplicate(boolean isCombineDuplicate) {
        this.isCombineDuplicate = isCombineDuplicate;
    }

    public CompleteDSLPckg_ValueSpecification getCompletedslpckg_valuespecification() {
        return completedslpckg_valuespecification;
    }

    public void setCompletedslpckg_valuespecification(CompleteDSLPckg_ValueSpecification completedslpckg_valuespecification) {
        this.completedslpckg_valuespecification = completedslpckg_valuespecification;
    }

}