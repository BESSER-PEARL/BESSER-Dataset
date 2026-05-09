





import java.util.List;
import java.util.ArrayList;

public class robotmodel_Role  {

    private String name;





    private robotmodel_Port robotmodel_port;




    private robotmodel_Connector robotmodel_connector;


    public robotmodel_Role(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public robotmodel_Port getRobotmodel_port() {
        return robotmodel_port;
    }

    public void setRobotmodel_port(robotmodel_Port robotmodel_port) {
        this.robotmodel_port = robotmodel_port;
    }
    public robotmodel_Connector getRobotmodel_connector() {
        return robotmodel_connector;
    }

    public void setRobotmodel_connector(robotmodel_Connector robotmodel_connector) {
        this.robotmodel_connector = robotmodel_connector;
    }

}