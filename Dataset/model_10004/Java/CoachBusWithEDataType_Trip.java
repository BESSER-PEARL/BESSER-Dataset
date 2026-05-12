





import java.util.List;
import java.util.ArrayList;

public class CoachBusWithEDataType_Trip  {

    private String type;
    private int number;
    private String name;
    private String origin;
    private String destination;



    public CoachBusWithEDataType_Trip(
        String type,        int number,        String name,        String origin,        String destination    ) {
        this.type = type;
        this.number = number;
        this.name = name;
        this.origin = origin;
        this.destination = destination;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOrigin() {
        return origin;
    }

    public void setOrigin(String origin) {
        this.origin = origin;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }


}