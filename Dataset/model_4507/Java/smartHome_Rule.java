





import java.util.List;
import java.util.ArrayList;

public class smartHome_Rule  {






    private smartHome_Duration smarthome_duration;




    private smartHome_Event smarthome_event;




    private List<smartHome_Condition> smarthome_conditions;




    private smartHome_SmartHome smarthome_smarthome;


    public smartHome_Rule(
    ) {
        this.smarthome_conditions = new ArrayList<>();
    }

    public smartHome_Rule(
        ArrayList<smartHome_Condition> smarthome_conditions    ) {
        this.smarthome_conditions = smarthome_conditions;
    }


    public smartHome_Duration getSmarthome_duration() {
        return smarthome_duration;
    }

    public void setSmarthome_duration(smartHome_Duration smarthome_duration) {
        this.smarthome_duration = smarthome_duration;
    }
    public smartHome_Event getSmarthome_event() {
        return smarthome_event;
    }

    public void setSmarthome_event(smartHome_Event smarthome_event) {
        this.smarthome_event = smarthome_event;
    }
    public List<smartHome_Condition> getSmarthome_conditions() {
        return smarthome_conditions;
    }

    public void addSmarthome_condition(Smarthome_condition smarthome_condition) {
        this.smarthome_conditions.add(smarthome_condition);
    }
    public smartHome_SmartHome getSmarthome_smarthome() {
        return smarthome_smarthome;
    }

    public void setSmarthome_smarthome(smartHome_SmartHome smarthome_smarthome) {
        this.smarthome_smarthome = smarthome_smarthome;
    }

}