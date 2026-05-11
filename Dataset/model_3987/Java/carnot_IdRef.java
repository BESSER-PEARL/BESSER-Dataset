





import java.util.List;
import java.util.ArrayList;

public class carnot_IdRef  {

    private String ref;





    private carnot_ActivityType carnot_activitytype;




    private carnot_ProcessDefinitionType carnot_processdefinitiontype;


    public carnot_IdRef(
        String ref    ) {
        this.ref = ref;
    }


    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }

    public carnot_ActivityType getCarnot_activitytype() {
        return carnot_activitytype;
    }

    public void setCarnot_activitytype(carnot_ActivityType carnot_activitytype) {
        this.carnot_activitytype = carnot_activitytype;
    }
    public carnot_ProcessDefinitionType getCarnot_processdefinitiontype() {
        return carnot_processdefinitiontype;
    }

    public void setCarnot_processdefinitiontype(carnot_ProcessDefinitionType carnot_processdefinitiontype) {
        this.carnot_processdefinitiontype = carnot_processdefinitiontype;
    }

}