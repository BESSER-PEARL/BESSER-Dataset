





import java.util.List;
import java.util.ArrayList;

public class Location1  {

    private String address;
    private int capacity;
    private String name;





    private Event1 event1;


    public Location1(
        String address,        int capacity,        String name    ) {
        this.address = address;
        this.capacity = capacity;
        this.name = name;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Event1 getEvent1() {
        return event1;
    }

    public void setEvent1(Event1 event1) {
        this.event1 = event1;
    }

}