





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Input  {






    private List<activitydiagram_InputValue> activitydiagram_inputvalues;


    public activitydiagram_Input(
    ) {
        this.activitydiagram_inputvalues = new ArrayList<>();
    }

    public activitydiagram_Input(
        ArrayList<activitydiagram_InputValue> activitydiagram_inputvalues    ) {
        this.activitydiagram_inputvalues = activitydiagram_inputvalues;
    }


    public List<activitydiagram_InputValue> getActivitydiagram_inputvalues() {
        return activitydiagram_inputvalues;
    }

    public void addActivitydiagram_inputvalue(Activitydiagram_inputvalue activitydiagram_inputvalue) {
        this.activitydiagram_inputvalues.add(activitydiagram_inputvalue);
    }

}