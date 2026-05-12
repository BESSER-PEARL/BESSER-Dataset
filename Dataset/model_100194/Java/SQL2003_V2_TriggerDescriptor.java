





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V2_TriggerDescriptor  {

    private String event;
    private String triggeredAction;
    private String level;
    private String actionTime;





    private SQL2003_V2_Trigger sql2003_v2_trigger;




    private SQL2003_V2_Trigger sql2003_v2_trigger;


    public SQL2003_V2_TriggerDescriptor(
        String event,        String triggeredAction,        String level,        String actionTime    ) {
        this.event = event;
        this.triggeredAction = triggeredAction;
        this.level = level;
        this.actionTime = actionTime;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getTriggeredaction() {
        return triggeredAction;
    }

    public void setTriggeredaction(String triggeredAction) {
        this.triggeredAction = triggeredAction;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
    }
    public String getActiontime() {
        return actionTime;
    }

    public void setActiontime(String actionTime) {
        this.actionTime = actionTime;
    }

    public SQL2003_V2_Trigger getSql2003_v2_trigger() {
        return sql2003_v2_trigger;
    }

    public void setSql2003_v2_trigger(SQL2003_V2_Trigger sql2003_v2_trigger) {
        this.sql2003_v2_trigger = sql2003_v2_trigger;
    }
    public SQL2003_V2_Trigger getSql2003_v2_trigger() {
        return sql2003_v2_trigger;
    }

    public void setSql2003_v2_trigger(SQL2003_V2_Trigger sql2003_v2_trigger) {
        this.sql2003_v2_trigger = sql2003_v2_trigger;
    }

}