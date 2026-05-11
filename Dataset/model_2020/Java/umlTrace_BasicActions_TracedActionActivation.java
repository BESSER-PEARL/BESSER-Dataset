





import java.util.List;
import java.util.ArrayList;

public class umlTrace_BasicActions_TracedActionActivation extends TracedActivityNodeActivation {






    private List<Values_ActionActivation_firing_Value> values_actionactivation_firing_values;


    public umlTrace_BasicActions_TracedActionActivation(
    ) {
        super(
        );
        this.values_actionactivation_firing_values = new ArrayList<>();
    }

    public umlTrace_BasicActions_TracedActionActivation(
        ArrayList<Values_ActionActivation_firing_Value> values_actionactivation_firing_values    ) {
        this.values_actionactivation_firing_values = values_actionactivation_firing_values;
    }


    public List<Values_ActionActivation_firing_Value> getValues_actionactivation_firing_values() {
        return values_actionactivation_firing_values;
    }

    public void addValues_actionactivation_firing_value(Values_actionactivation_firing_value values_actionactivation_firing_value) {
        this.values_actionactivation_firing_values.add(values_actionactivation_firing_value);
    }

}