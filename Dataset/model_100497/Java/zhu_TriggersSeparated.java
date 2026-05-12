





import java.util.List;
import java.util.ArrayList;

public class zhu_TriggersSeparated  {

    private String followingTriggers;
    private String firstTrigger;





    private zhu_Triggers zhu_triggers;


    public zhu_TriggersSeparated(
        String followingTriggers,        String firstTrigger    ) {
        this.followingTriggers = followingTriggers;
        this.firstTrigger = firstTrigger;
    }


    public String getFollowingtriggers() {
        return followingTriggers;
    }

    public void setFollowingtriggers(String followingTriggers) {
        this.followingTriggers = followingTriggers;
    }
    public String getFirsttrigger() {
        return firstTrigger;
    }

    public void setFirsttrigger(String firstTrigger) {
        this.firstTrigger = firstTrigger;
    }

    public zhu_Triggers getZhu_triggers() {
        return zhu_triggers;
    }

    public void setZhu_triggers(zhu_Triggers zhu_triggers) {
        this.zhu_triggers = zhu_triggers;
    }

}