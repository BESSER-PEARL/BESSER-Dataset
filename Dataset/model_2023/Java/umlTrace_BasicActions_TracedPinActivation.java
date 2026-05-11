





import java.util.List;
import java.util.ArrayList;

public class umlTrace_BasicActions_TracedPinActivation extends TracedObjectNodeActivation {






    private List<PinActivation_count_temp_Value> pinactivation_count_temp_values;




    private List<PinActivation_actionActivation_Value> pinactivation_actionactivation_values;


    public umlTrace_BasicActions_TracedPinActivation(
    ) {
        super(
        );
        this.pinactivation_count_temp_values = new ArrayList<>();
        this.pinactivation_actionactivation_values = new ArrayList<>();
    }

    public umlTrace_BasicActions_TracedPinActivation(
        ArrayList<PinActivation_count_temp_Value> pinactivation_count_temp_values,        ArrayList<PinActivation_actionActivation_Value> pinactivation_actionactivation_values    ) {
        this.pinactivation_count_temp_values = pinactivation_count_temp_values;
        this.pinactivation_actionactivation_values = pinactivation_actionactivation_values;
    }


    public List<PinActivation_count_temp_Value> getPinactivation_count_temp_values() {
        return pinactivation_count_temp_values;
    }

    public void addPinactivation_count_temp_value(Pinactivation_count_temp_value pinactivation_count_temp_value) {
        this.pinactivation_count_temp_values.add(pinactivation_count_temp_value);
    }
    public List<PinActivation_actionActivation_Value> getPinactivation_actionactivation_values() {
        return pinactivation_actionactivation_values;
    }

    public void addPinactivation_actionactivation_value(Pinactivation_actionactivation_value pinactivation_actionactivation_value) {
        this.pinactivation_actionactivation_values.add(pinactivation_actionactivation_value);
    }

}