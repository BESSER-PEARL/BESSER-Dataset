





import java.util.List;
import java.util.ArrayList;

public class model_Flow extends Activity {






    private model_CompletionCondition model_completioncondition;




    private List<model_Activity> model_activitys;




    private model_Links model_links;


    public model_Flow(
    ) {
        super(
        );
        this.model_activitys = new ArrayList<>();
    }

    public model_Flow(
        ArrayList<model_Activity> model_activitys    ) {
        this.model_activitys = model_activitys;
    }


    public model_CompletionCondition getModel_completioncondition() {
        return model_completioncondition;
    }

    public void setModel_completioncondition(model_CompletionCondition model_completioncondition) {
        this.model_completioncondition = model_completioncondition;
    }
    public List<model_Activity> getModel_activitys() {
        return model_activitys;
    }

    public void addModel_activity(Model_activity model_activity) {
        this.model_activitys.add(model_activity);
    }
    public model_Links getModel_links() {
        return model_links;
    }

    public void setModel_links(model_Links model_links) {
        this.model_links = model_links;
    }

}