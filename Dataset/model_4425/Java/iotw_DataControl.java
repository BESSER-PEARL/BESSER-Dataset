





import java.util.List;
import java.util.ArrayList;

public class iotw_DataControl extends Control {

    private String constraints;
    private String location;
    private String type;



    public iotw_DataControl(
        String constraints,        String location,        String type    ) {
        super(
        );
        this.constraints = constraints;
        this.location = location;
        this.type = type;
    }


    public String getConstraints() {
        return constraints;
    }

    public void setConstraints(String constraints) {
        this.constraints = constraints;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}