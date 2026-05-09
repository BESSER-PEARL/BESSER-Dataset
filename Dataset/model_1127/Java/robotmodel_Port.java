





import java.util.List;
import java.util.ArrayList;

public class robotmodel_Port  {

    private String name;





    private robotmodel_Component robotmodel_component;


    public robotmodel_Port(
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

}