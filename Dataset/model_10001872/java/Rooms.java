





import java.util.List;
import java.util.ArrayList;

public class Rooms  {

    private String type;
    private int roomNo;





    private List<Receptionist> receptionists;




    private Guest guest;


    public Rooms(
        String type,        int roomNo    ) {
        this.type = type;
        this.roomNo = roomNo;
        this.receptionists = new ArrayList<>();
    }

    public Rooms(
        String type,        int roomNo        ArrayList<Receptionist> receptionists    ) {
        this.type = type;
        this.roomNo = roomNo;
        this.receptionists = receptionists;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getRoomno() {
        return roomNo;
    }

    public void setRoomno(int roomNo) {
        this.roomNo = roomNo;
    }

    public List<Receptionist> getReceptionists() {
        return receptionists;
    }

    public void addReceptionist(Receptionist receptionist) {
        this.receptionists.add(receptionist);
    }
    public Guest getGuest() {
        return guest;
    }

    public void setGuest(Guest guest) {
        this.guest = guest;
    }

}