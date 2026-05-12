





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int roomNo;
    private int RatesofRoom;
    private String typeOfRoom;





    private Guest guest;




    private List<Receptionist> receptionists;


    public Room(
        int roomNo,        int RatesofRoom,        String typeOfRoom    ) {
        this.roomNo = roomNo;
        this.RatesofRoom = RatesofRoom;
        this.typeOfRoom = typeOfRoom;
        this.receptionists = new ArrayList<>();
    }

    public Room(
        int roomNo,        int RatesofRoom,        String typeOfRoom        ArrayList<Receptionist> receptionists    ) {
        this.roomNo = roomNo;
        this.RatesofRoom = RatesofRoom;
        this.typeOfRoom = typeOfRoom;
        this.receptionists = receptionists;
    }

    public int getRoomno() {
        return roomNo;
    }

    public void setRoomno(int roomNo) {
        this.roomNo = roomNo;
    }
    public int getRatesofroom() {
        return RatesofRoom;
    }

    public void setRatesofroom(int RatesofRoom) {
        this.RatesofRoom = RatesofRoom;
    }
    public String getTypeofroom() {
        return typeOfRoom;
    }

    public void setTypeofroom(String typeOfRoom) {
        this.typeOfRoom = typeOfRoom;
    }

    public Guest getGuest() {
        return guest;
    }

    public void setGuest(Guest guest) {
        this.guest = guest;
    }
    public List<Receptionist> getReceptionists() {
        return receptionists;
    }

    public void addReceptionist(Receptionist receptionist) {
        this.receptionists.add(receptionist);
    }

}