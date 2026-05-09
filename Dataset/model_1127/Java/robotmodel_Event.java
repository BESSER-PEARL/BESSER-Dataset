





import java.util.List;
import java.util.ArrayList;

public class robotmodel_Event  {

    private String name;





    private robotmodel_Component robotmodel_component;




    private robotmodel_State robotmodel_state;


    public robotmodel_Event(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public robotmodel_Component getRobotmodel_component() {
        return robotmodel_component;
    }

    public void setRobotmodel_component(robotmodel_Component robotmodel_component) {
        this.robotmodel_component = robotmodel_component;
    }
    public robotmodel_State getRobotmodel_state() {
        return robotmodel_state;
    }

    public void setRobotmodel_state(robotmodel_State robotmodel_state) {
        this.robotmodel_state = robotmodel_state;
    }

}