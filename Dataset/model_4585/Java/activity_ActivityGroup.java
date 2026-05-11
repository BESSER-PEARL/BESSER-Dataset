





import java.util.List;
import java.util.ArrayList;

public class activity_ActivityGroup extends Activity {

    private String name;





    private activity_Activity activity_activity;


    public activity_ActivityGroup(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public activity_Activity getActivity_activity() {
        return activity_activity;
    }

    public void setActivity_activity(activity_Activity activity_activity) {
        this.activity_activity = activity_activity;
    }

}