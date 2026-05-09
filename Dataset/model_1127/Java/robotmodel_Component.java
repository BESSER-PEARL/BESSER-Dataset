





import java.util.List;
import java.util.ArrayList;

public class robotmodel_Component  {

    private String type;
    private String atype;
    private String depends;
    private float frequency;
    private String name;





    private robotmodel_System robotmodel_system;




    private robotmodel_Component robotmodel_component;


    public robotmodel_Component(
        String type,        String atype,        String depends,        float frequency,        String name    ) {
        this.type = type;
        this.atype = atype;
        this.depends = depends;
        this.frequency = frequency;
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
    public String getDepends() {
        return depends;
    }

    public void setDepends(String depends) {
        this.depends = depends;
    }
    public float getFrequency() {
        return frequency;
    }

    public void setFrequency(float frequency) {
        this.frequency = frequency;
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
    public robotmodel_Component getRobotmodel_component() {
        return robotmodel_component;
    }

    public void setRobotmodel_component(robotmodel_Component robotmodel_component) {
        this.robotmodel_component = robotmodel_component;
    }

}