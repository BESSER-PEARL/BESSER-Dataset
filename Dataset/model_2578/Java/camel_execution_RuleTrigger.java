




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class camel_execution_RuleTrigger  {

    private LocalDate trigerringTime;
    private String name;





    private List<ActionRealisation> actionrealisations;




    private List<EventInstance> eventinstances;




    private ExecutionContext executioncontext;


    public camel_execution_RuleTrigger(
        LocalDate trigerringTime,        String name    ) {
        this.trigerringTime = trigerringTime;
        this.name = name;
        this.actionrealisations = new ArrayList<>();
        this.eventinstances = new ArrayList<>();
    }

    public camel_execution_RuleTrigger(
        LocalDate trigerringTime,        String name        ArrayList<ActionRealisation> actionrealisations,        ArrayList<EventInstance> eventinstances    ) {
        this.trigerringTime = trigerringTime;
        this.name = name;
        this.actionrealisations = actionrealisations;
        this.eventinstances = eventinstances;
    }

    public LocalDate getTrigerringtime() {
        return trigerringTime;
    }

    public void setTrigerringtime(LocalDate trigerringTime) {
        this.trigerringTime = trigerringTime;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ActionRealisation> getActionrealisations() {
        return actionrealisations;
    }

    public void addActionrealisation(Actionrealisation actionrealisation) {
        this.actionrealisations.add(actionrealisation);
    }
    public List<EventInstance> getEventinstances() {
        return eventinstances;
    }

    public void addEventinstance(Eventinstance eventinstance) {
        this.eventinstances.add(eventinstance);
    }
    public ExecutionContext getExecutioncontext() {
        return executioncontext;
    }

    public void setExecutioncontext(ExecutionContext executioncontext) {
        this.executioncontext = executioncontext;
    }

}