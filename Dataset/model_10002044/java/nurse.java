





import java.util.List;
import java.util.ArrayList;

public class nurse  {

    private boolean availability;
    private String name;
    private int contact;
    private int id;





    private Room room;


    public nurse(
        boolean availability,        String name,        int contact,        int id    ) {
        this.availability = availability;
        this.name = name;
        this.contact = contact;
        this.id = id;
    }


    public boolean getAvailability() {
        return availability;
    }

    public void setAvailability(boolean availability) {
        this.availability = availability;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getContact() {
        return contact;
    }

    public void setContact(int contact) {
        this.contact = contact;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Room getRoom() {
        return room;
    }

    public void setRoom(Room room) {
        this.room = room;
    }

}