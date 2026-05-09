





import java.util.List;
import java.util.ArrayList;

public class robotmodel_Property  {

    private String type;
    private String value;
    private String name;





    private robotmodel_Property_List robotmodel_property_list;


    public robotmodel_Property(
        String type,        String value,        String name    ) {
        this.type = type;
        this.value = value;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public robotmodel_Property_List getRobotmodel_property_list() {
        return robotmodel_property_list;
    }

    public void setRobotmodel_property_list(robotmodel_Property_List robotmodel_property_list) {
        this.robotmodel_property_list = robotmodel_property_list;
    }

}