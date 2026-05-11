





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_ExternalSensor extends Sensor {






    private List<ioT_metamodel_Action> iot_metamodel_actions;


    public ioT_metamodel_ExternalSensor(
    ) {
        super(
        );
        this.iot_metamodel_actions = new ArrayList<>();
    }

    public ioT_metamodel_ExternalSensor(
        ArrayList<ioT_metamodel_Action> iot_metamodel_actions    ) {
        this.iot_metamodel_actions = iot_metamodel_actions;
    }


    public List<ioT_metamodel_Action> getIot_metamodel_actions() {
        return iot_metamodel_actions;
    }

    public void addIot_metamodel_action(Iot_metamodel_action iot_metamodel_action) {
        this.iot_metamodel_actions.add(iot_metamodel_action);
    }

}