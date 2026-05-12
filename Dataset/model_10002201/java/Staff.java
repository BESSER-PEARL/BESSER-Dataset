





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private int Id;
    private String Staff_name;
    private String Type;





    private Rooms rooms;


    public Staff(
        int Id,        String Staff_name,        String Type    ) {
        this.Id = Id;
        this.Staff_name = Staff_name;
        this.Type = Type;
    }


    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getStaff_name() {
        return Staff_name;
    }

    public void setStaff_name(String Staff_name) {
        this.Staff_name = Staff_name;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public Rooms getRooms() {
        return rooms;
    }

    public void setRooms(Rooms rooms) {
        this.rooms = rooms;
    }

}