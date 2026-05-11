





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Transition  {






    private List<ioT_metamodel_Action> iot_metamodel_actions;




    private List<ioT_metamodel_DeviceState> iot_metamodel_devicestates;




    private List<ioT_metamodel_DeviceState> iot_metamodel_devicestates;


    public ioT_metamodel_Transition(
    ) {
        this.iot_metamodel_actions = new ArrayList<>();
        this.iot_metamodel_devicestates = new ArrayList<>();
        this.iot_metamodel_devicestates = new ArrayList<>();
    }

    public ioT_metamodel_Transition(
        ArrayList<ioT_metamodel_Action> iot_metamodel_actions,        ArrayList<ioT_metamodel_DeviceState> iot_metamodel_devicestates,        ArrayList<ioT_metamodel_DeviceState> iot_metamodel_devicestates    ) {
        this.iot_metamodel_actions = iot_metamodel_actions;
        this.iot_metamodel_devicestates = iot_metamodel_devicestates;
        this.iot_metamodel_devicestates = iot_metamodel_devicestates;
    }


    public List<ioT_metamodel_Action> getIot_metamodel_actions() {
        return iot_metamodel_actions;
    }

    public void addIot_metamodel_action(Iot_metamodel_action iot_metamodel_action) {
        this.iot_metamodel_actions.add(iot_metamodel_action);
    }
    public List<ioT_metamodel_DeviceState> getIot_metamodel_devicestates() {
        return iot_metamodel_devicestates;
    }

    public void addIot_metamodel_devicestate(Iot_metamodel_devicestate iot_metamodel_devicestate) {
        this.iot_metamodel_devicestates.add(iot_metamodel_devicestate);
    }
    public List<ioT_metamodel_DeviceState> getIot_metamodel_devicestates() {
        return iot_metamodel_devicestates;
    }

    public void addIot_metamodel_devicestate(Iot_metamodel_devicestate iot_metamodel_devicestate) {
        this.iot_metamodel_devicestates.add(iot_metamodel_devicestate);
    }

}