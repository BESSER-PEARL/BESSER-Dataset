





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String name;





    private Guest guest;


    public Room(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Guest getGuest() {
        return guest;
    }

    public void setGuest(Guest guest) {
        this.guest = guest;
    }

}