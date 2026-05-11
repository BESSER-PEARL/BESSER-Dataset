





import java.util.List;
import java.util.ArrayList;

public class behaviour_RobotCollaboration  {






    private behaviour_DynamicRobot behaviour_dynamicrobot;




    private List<behaviour_Property> behaviour_propertys;




    private behaviour_MeasureValue behaviour_measurevalue;




    private behaviour_DynamicRobot behaviour_dynamicrobot;


    public behaviour_RobotCollaboration(
    ) {
        this.behaviour_propertys = new ArrayList<>();
    }

    public behaviour_RobotCollaboration(
        ArrayList<behaviour_Property> behaviour_propertys    ) {
        this.behaviour_propertys = behaviour_propertys;
    }


    public behaviour_DynamicRobot getBehaviour_dynamicrobot() {
        return behaviour_dynamicrobot;
    }

    public void setBehaviour_dynamicrobot(behaviour_DynamicRobot behaviour_dynamicrobot) {
        this.behaviour_dynamicrobot = behaviour_dynamicrobot;
    }
    public List<behaviour_Property> getBehaviour_propertys() {
        return behaviour_propertys;
    }

    public void addBehaviour_property(Behaviour_property behaviour_property) {
        this.behaviour_propertys.add(behaviour_property);
    }
    public behaviour_MeasureValue getBehaviour_measurevalue() {
        return behaviour_measurevalue;
    }

    public void setBehaviour_measurevalue(behaviour_MeasureValue behaviour_measurevalue) {
        this.behaviour_measurevalue = behaviour_measurevalue;
    }
    public behaviour_DynamicRobot getBehaviour_dynamicrobot() {
        return behaviour_dynamicrobot;
    }

    public void setBehaviour_dynamicrobot(behaviour_DynamicRobot behaviour_dynamicrobot) {
        this.behaviour_dynamicrobot = behaviour_dynamicrobot;
    }

}