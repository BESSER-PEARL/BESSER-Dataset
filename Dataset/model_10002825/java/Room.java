





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String name;





    private List<Guest> guests;


    public Room(
        String name    ) {
        this.name = name;
        this.guests = new ArrayList<>();
    }

    public Room(
        String name        ArrayList<Guest> guests    ) {
        this.name = name;
        this.guests = guests;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Guest> getGuests() {
        return guests;
    }

    public void addGuest(Guest guest) {
        this.guests.add(guest);
    }

}