





import java.util.List;
import java.util.ArrayList;

public class SQL2003_V3_TriggerDescriptor  {

    private String actionTime;
    private String level;
    private String triggeredAction;
    private String event;





    private SQL2003_V3_Trigger sql2003_v3_trigger;




    private SQL2003_V3_Trigger sql2003_v3_trigger;


    public SQL2003_V3_TriggerDescriptor(
        String actionTime,        String level,        String triggeredAction,        String event    ) {
        this.actionTime = actionTime;
        this.level = level;
        this.triggeredAction = triggeredAction;
        this.event = event;
    }


    public String getActiontime() {
        return actionTime;
    }

    public void setActiontime(String actionTime) {
        this.actionTime = actionTime;
    }
    public String getLevel() {
        return level;
    }

    public void setLevel(String level) {
        this.level = level;
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