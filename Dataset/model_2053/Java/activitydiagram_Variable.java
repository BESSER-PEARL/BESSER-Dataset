





import java.util.List;
import java.util.ArrayList;

public class activitydiagram_Variable  {

    private String name;





    private activitydiagram_InputValue activitydiagram_inputvalue;


    public activitydiagram_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public activitydiagram_InputValue getActivitydiagram_inputvalue() {
        return activitydiagram_inputvalue;
    }

    public void setActivitydiagram_inputvalue(activitydiagram_InputValue activitydiagram_inputvalue) {
        this.activitydiagram_inputvalue = activitydiagram_inputvalue;
    }

}