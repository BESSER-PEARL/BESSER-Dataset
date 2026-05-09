





import java.util.List;
import java.util.ArrayList;

public class robotmodel_Connector  {

    private String type;
    private String atype;
    private String name;





    private robotmodel_System robotmodel_system;


    public robotmodel_Connector(
        String type,        String atype,        String name    ) {
        this.type = type;
        this.atype = atype;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAtype() {
        return atype;
    }

    public void setAtype(String atype) {
        this.atype = atype;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public robotmodel_System getRobotmodel_system() {
        return robotmodel_system;
    }

    public void setRobotmodel_system(robotmodel_System robotmodel_system) {
        this.robotmodel_system = robotmodel_system;
    }

}