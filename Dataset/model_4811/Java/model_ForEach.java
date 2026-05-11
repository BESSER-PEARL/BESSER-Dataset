





import java.util.List;
import java.util.ArrayList;

public class model_ForEach extends Activity {

    private String parallel;





    private model_Activity model_activity;




    private model_Variable model_variable;




    private model_CompletionCondition model_completioncondition;


    public model_ForEach(
        String parallel    ) {
        super(
        );
        this.parallel = parallel;
    }


    public String getParallel() {
        return parallel;
    }

    public void setParallel(String parallel) {
        this.parallel = parallel;
    }

    public model_Activity getModel_activity() {
        return model_activity;
    }

    public void setModel_activity(model_Activity model_activity) {
        this.model_activity = model_activity;
    }
    public model_Variable getModel_variable() {
        return model_variable;
    }

    public void setModel_variable(model_Variable model_variable) {
        this.model_variable = model_variable;
    }
    public model_CompletionCondition getModel_completioncondition() {
        return model_completioncondition;
    }

    public void setModel_completioncondition(model_CompletionCondition model_completioncondition) {
        this.model_completioncondition = model_completioncondition;
    }

}