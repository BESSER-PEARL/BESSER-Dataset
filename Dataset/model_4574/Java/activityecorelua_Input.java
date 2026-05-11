





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Input  {






    private List<activityecorelua_InputValue> activityecorelua_inputvalues;


    public activityecorelua_Input(
    ) {
        this.activityecorelua_inputvalues = new ArrayList<>();
    }

    public activityecorelua_Input(
        ArrayList<activityecorelua_InputValue> activityecorelua_inputvalues    ) {
        this.activityecorelua_inputvalues = activityecorelua_inputvalues;
    }


    public List<activityecorelua_InputValue> getActivityecorelua_inputvalues() {
        return activityecorelua_inputvalues;
    }

    public void addActivityecorelua_inputvalue(Activityecorelua_inputvalue activityecorelua_inputvalue) {
        this.activityecorelua_inputvalues.add(activityecorelua_inputvalue);
    }

}