





import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_Bill  {

    private float total_price;
    private int booking_id;





    private List<Room> rooms;




    private List<ExtraService> extraservices;


    public CodePack_DataModels_Bill(
        float total_price,        int booking_id    ) {
        this.total_price = total_price;
        this.booking_id = booking_id;
        this.rooms = new ArrayList<>();
        this.extraservices = new ArrayList<>();
    }

    public CodePack_DataModels_Bill(
        float total_price,        int booking_id        ArrayList<Room> rooms,        ArrayList<ExtraService> extraservices    ) {
        this.total_price = total_price;
        this.booking_id = booking_id;
        this.rooms = rooms;
        this.extraservices = extraservices;
    }

    public float getTotal_price() {
        return total_price;
    }

    public void setTotal_price(float total_price) {
        this.total_price = total_price;
    }
    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }

    public List<Room> getRooms() {
        return rooms;
    }

    public void addRoom(Room room) {
        this.rooms.add(room);
    }
    public List<ExtraService> getExtraservices() {
        return extraservices;
    }

    public void addExtraservice(Extraservice extraservice) {
        this.extraservices.add(extraservice);
    }

}