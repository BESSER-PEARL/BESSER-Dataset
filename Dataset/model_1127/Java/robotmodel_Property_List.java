





import java.util.List;
import java.util.ArrayList;

public class robotmodel_Property_List  {

    private String name;





    private robotmodel_Component robotmodel_component;




    private robotmodel_Connector robotmodel_connector;


    public robotmodel_Property_List(
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
    public robotmodel_Connector getRobotmodel_connector() {
        return robotmodel_connector;
    }

    public void setRobotmodel_connector(robotmodel_Connector robotmodel_connector) {
        this.robotmodel_connector = robotmodel_connector;
    }

}