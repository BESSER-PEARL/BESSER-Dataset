





import java.util.List;
import java.util.ArrayList;

public class metamodel_Robot  {

    private String name;





    private List<metamodel_Action> metamodel_actions;




    private List<metamodel_Sensor> metamodel_sensors;




    private List<metamodel_Actuator> metamodel_actuators;


    public metamodel_Robot(
        String name    ) {
        this.name = name;
        this.metamodel_actions = new ArrayList<>();
        this.metamodel_sensors = new ArrayList<>();
        this.metamodel_actuators = new ArrayList<>();
    }

    public metamodel_Robot(
        String name        ArrayList<metamodel_Action> metamodel_actions,        ArrayList<metamodel_Sensor> metamodel_sensors,        ArrayList<metamodel_Actuator> metamodel_actuators    ) {
        this.name = name;
        this.metamodel_actions = metamodel_actions;
        this.metamodel_sensors = metamodel_sensors;
        this.metamodel_actuators = metamodel_actuators;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<metamodel_Action> getMetamodel_actions() {
        return metamodel_actions;
    }

    public void addMetamodel_action(Metamodel_action metamodel_action) {
        this.metamodel_actions.add(metamodel_action);
    }
    public List<metamodel_Sensor> getMetamodel_sensors() {
        return metamodel_sensors;
    }

    public void addMetamodel_sensor(Metamodel_sensor metamodel_sensor) {
        this.metamodel_sensors.add(metamodel_sensor);
    }
    public List<metamodel_Actuator> getMetamodel_actuators() {
        return metamodel_actuators;
    }

    public void addMetamodel_actuator(Metamodel_actuator metamodel_actuator) {
        this.metamodel_actuators.add(metamodel_actuator);
    }

}