





import java.util.List;
import java.util.ArrayList;

public class SQL2003_evo_TriggerDescriptor  {

    private String level;
    private String triggeredAction;
    private String actionTime;
    private String event;





    private SQL2003_evo_Trigger sql2003_evo_trigger;




    private SQL2003_evo_Trigger sql2003_evo_trigger;


    public SQL2003_evo_TriggerDescriptor(
        String level,        String triggeredAction,        String actionTime,        String event    ) {
        this.level = level;
        this.triggeredAction = triggeredAction;
        this.actionTime = actionTime;
        this.event = event;
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
    public String getActiontime() {
        return actionTime;
    }

    public void setActiontime(String actionTime) {
        this.actionTime = actionTime;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public SQL2003_evo_Trigger getSql2003_evo_trigger() {
        return sql2003_evo_trigger;
    }

    public void setSql2003_evo_trigger(SQL2003_evo_Trigger sql2003_evo_trigger) {
        this.sql2003_evo_trigger = sql2003_evo_trigger;
    }
    public SQL2003_evo_Trigger getSql2003_evo_trigger() {
        return sql2003_evo_trigger;
    }

    public void setSql2003_evo_trigger(SQL2003_evo_Trigger sql2003_evo_trigger) {
        this.sql2003_evo_trigger = sql2003_evo_trigger;
    }

}