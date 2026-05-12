





import java.util.List;
import java.util.ArrayList;

public class CoachBus_Trip  {

    private String type;
    private String destination;
    private int number;
    private String origin;
    private String name;



    public CoachBus_Trip(
        String type,        String destination,        int number,        String origin,        String name    ) {
        this.type = type;
        this.destination = destination;
        this.number = number;
        this.origin = origin;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDestination() {
        return destination;
    }

    public void setDestination(String destination) {
        this.destination = destination;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public String getOrigin() {
        return origin;
    }

    public void setOrigin(String origin) {
        this.origin = origin;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}