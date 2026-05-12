





import java.util.List;
import java.util.ArrayList;

public class Lock_doors_sensors  {

    private String attribute;





    private Door_Security door_security;


    public Lock_doors_sensors(
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