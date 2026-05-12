





import java.util.List;
import java.util.ArrayList;

public class Light_PIR_Sensor  {

    private String attribute;





    private Door_Security door_security;


    public Light_PIR_Sensor(
        String attribute    ) {
        this.attribute = attribute;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public Door_Security getDoor_security() {
        return door_security;
    }

    public void setDoor_security(Door_Security door_security) {
        this.door_security = door_security;
    }

}