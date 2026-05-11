





import java.util.List;
import java.util.ArrayList;

public class model_Branches extends Expression {

    private String countCompletedBranchesOnly;





    private model_CompletionCondition model_completioncondition;


    public model_Branches(
        String countCompletedBranchesOnly    ) {
        super(
        );
        this.countCompletedBranchesOnly = countCompletedBranchesOnly;
    }


    public String getCountcompletedbranchesonly() {
        return countCompletedBranchesOnly;
    }

    public void setCountcompletedbranchesonly(String countCompletedBranchesOnly) {
        this.countCompletedBranchesOnly = countCompletedBranchesOnly;
    }

    public model_CompletionCondition getModel_completioncondition() {
        return model_completioncondition;
    }

    public void setModel_completioncondition(model_CompletionCondition model_completioncondition) {
        this.model_completioncondition = model_completioncondition;
    }

}