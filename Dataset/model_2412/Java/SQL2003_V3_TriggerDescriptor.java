





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_TriggerDescriptor  {

    private String triggeredAction;
    private String event;
    private String level;
    private String actionTime;





    private SQL2003_V3_Trigger sql2003_v3_trigger;




    private SQL2003_V3_Trigger sql2003_v3_trigger;


    public SQL2003_V3_TriggerDescriptor(
        String triggeredAction,        String event,        String level,        String actionTime    ) {
        this.triggeredAction = triggeredAction;
        this.event = event;
        this.level = level;
        this.actionTime = actionTime;
    }


    public String getTriggeredaction() {
        return triggeredAction;
    }

    public void setTriggeredaction(String triggeredAction) {
        this.triggeredAction = triggeredAction;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
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

    public SQL2003_V3_Trigger getSql2003_v3_trigger() {
        return sql2003_v3_trigger;
    }

    public void setSql2003_v3_trigger(SQL2003_V3_Trigger sql2003_v3_trigger) {
        this.sql2003_v3_trigger = sql2003_v3_trigger;
    }
    public SQL2003_V3_Trigger getSql2003_v3_trigger() {
        return sql2003_v3_trigger;
    }

    public void setSql2003_v3_trigger(SQL2003_V3_Trigger sql2003_v3_trigger) {
        this.sql2003_v3_trigger = sql2003_v3_trigger;
    }

}