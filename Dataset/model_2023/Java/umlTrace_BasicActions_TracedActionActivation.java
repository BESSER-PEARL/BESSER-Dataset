





import java.util.List;
import java.util.ArrayList;

public class umlTrace_BasicActions_TracedActionActivation extends TracedActivityNodeActivation {






    private List<ActionActivation_pinActivations_Value> actionactivation_pinactivations_values;




    private List<ActionActivation_firing_Value> actionactivation_firing_values;


    public umlTrace_BasicActions_TracedActionActivation(
    ) {
        super(
        );
        this.actionactivation_pinactivations_values = new ArrayList<>();
        this.actionactivation_firing_values = new ArrayList<>();
    }

    public umlTrace_BasicActions_TracedActionActivation(
        ArrayList<ActionActivation_pinActivations_Value> actionactivation_pinactivations_values,        ArrayList<ActionActivation_firing_Value> actionactivation_firing_values    ) {
        this.actionactivation_pinactivations_values = actionactivation_pinactivations_values;
        this.actionactivation_firing_values = actionactivation_firing_values;
    }


    public List<ActionActivation_pinActivations_Value> getActionactivation_pinactivations_values() {
        return actionactivation_pinactivations_values;
    }

    public void addActionactivation_pinactivations_value(Actionactivation_pinactivations_value actionactivation_pinactivations_value) {
        this.actionactivation_pinactivations_values.add(actionactivation_pinactivations_value);
    }
    public List<ActionActivation_firing_Value> getActionactivation_firing_values() {
        return actionactivation_firing_values;
    }

    public void addActionactivation_firing_value(Actionactivation_firing_value actionactivation_firing_value) {
        this.actionactivation_firing_values.add(actionactivation_firing_value);
    }

}