





import java.util.List;
import java.util.ArrayList;

public class metamodel_Value  {

    private String name;





    private metamodel_Type metamodel_type;




    private metamodel_StateMachine metamodel_statemachine;




    private metamodel_Sensor metamodel_sensor;


    public metamodel_Value(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public metamodel_Type getMetamodel_type() {
        return metamodel_type;
    }

    public void setMetamodel_type(metamodel_Type metamodel_type) {
        this.metamodel_type = metamodel_type;
    }
    public metamodel_StateMachine getMetamodel_statemachine() {
        return metamodel_statemachine;
    }

    public void setMetamodel_statemachine(metamodel_StateMachine metamodel_statemachine) {
        this.metamodel_statemachine = metamodel_statemachine;
    }
    public metamodel_Sensor getMetamodel_sensor() {
        return metamodel_sensor;
    }

    public void setMetamodel_sensor(metamodel_Sensor metamodel_sensor) {
        this.metamodel_sensor = metamodel_sensor;
    }

}