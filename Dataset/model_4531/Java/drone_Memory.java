





import java.util.List;
import java.util.ArrayList;

public class drone_Memory extends NamedElement {

    private int size;
    private String type;
    private String subType;





    private drone_Drone drone_drone;


    public drone_Memory(
        int size,        String type,        String subType    ) {
        super(
        );
        this.size = size;
        this.type = type;
        this.subType = subType;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getSubtype() {
        return subType;
    }

    public void setSubtype(String subType) {
        this.subType = subType;
    }

    public drone_Drone getDrone_drone() {
        return drone_drone;
    }

    public void setDrone_drone(drone_Drone drone_drone) {
        this.drone_drone = drone_drone;
    }

}