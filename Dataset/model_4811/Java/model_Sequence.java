





import java.util.List;
import java.util.ArrayList;

public class model_Sequence extends Activity {






    private List<model_Activity> model_activitys;


    public model_Sequence(
    ) {
        super(
        );
        this.model_activitys = new ArrayList<>();
    }

    public model_Sequence(
        ArrayList<model_Activity> model_activitys    ) {
        this.model_activitys = model_activitys;
    }


    public List<model_Activity> getModel_activitys() {
        return model_activitys;
    }

    public void addModel_activity(Model_activity model_activity) {
        this.model_activitys.add(model_activity);
    }

}