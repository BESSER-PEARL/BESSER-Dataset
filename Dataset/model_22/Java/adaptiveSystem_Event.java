





import java.util.List;
import java.util.ArrayList;

public class adaptiveSystem_Event extends Node {

    private boolean saturated;
    private boolean enabled;





    private adaptiveSystem_Condition adaptivesystem_condition;




    private List<adaptiveSystem_Condition> adaptivesystem_conditions;




    private List<adaptiveSystem_Condition> adaptivesystem_conditions;




    private adaptiveSystem_Condition adaptivesystem_condition;


    public adaptiveSystem_Event(
        boolean saturated,        boolean enabled    ) {
        super(
        );
        this.saturated = saturated;
        this.enabled = enabled;
        this.adaptivesystem_conditions = new ArrayList<>();
        this.adaptivesystem_conditions = new ArrayList<>();
    }

    public adaptiveSystem_Event(
        boolean saturated,        boolean enabled        ArrayList<adaptiveSystem_Condition> adaptivesystem_conditions,        ArrayList<adaptiveSystem_Condition> adaptivesystem_conditions    ) {
        this.saturated = saturated;
        this.enabled = enabled;
        this.adaptivesystem_conditions = adaptivesystem_conditions;
        this.adaptivesystem_conditions = adaptivesystem_conditions;
    }

    public boolean getSaturated() {
        return saturated;
    }

    public void setSaturated(boolean saturated) {
        this.saturated = saturated;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }

    public adaptiveSystem_Condition getAdaptivesystem_condition() {
        return adaptivesystem_condition;
    }

    public void setAdaptivesystem_condition(adaptiveSystem_Condition adaptivesystem_condition) {
        this.adaptivesystem_condition = adaptivesystem_condition;
    }
    public List<adaptiveSystem_Condition> getAdaptivesystem_conditions() {
        return adaptivesystem_conditions;
    }

    public void addAdaptivesystem_condition(Adaptivesystem_condition adaptivesystem_condition) {
        this.adaptivesystem_conditions.add(adaptivesystem_condition);
    }
    public List<adaptiveSystem_Condition> getAdaptivesystem_conditions() {
        return adaptivesystem_conditions;
    }

    public void addAdaptivesystem_condition(Adaptivesystem_condition adaptivesystem_condition) {
        this.adaptivesystem_conditions.add(adaptivesystem_condition);
    }
    public adaptiveSystem_Condition getAdaptivesystem_condition() {
        return adaptivesystem_condition;
    }

    public void setAdaptivesystem_condition(adaptiveSystem_Condition adaptivesystem_condition) {
        this.adaptivesystem_condition = adaptivesystem_condition;
    }

}