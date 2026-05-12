





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int room_no_bedroom;
    private int room_size_interior;
    private String room_name;
    private int room_id;
    private int room_no_bathroom;
    private float room_rent_night;





    private Hotel hotel;




    private List<Users> userss;


    public Room(
        int room_no_bedroom,        int room_size_interior,        String room_name,        int room_id,        int room_no_bathroom,        float room_rent_night    ) {
        this.room_no_bedroom = room_no_bedroom;
        this.room_size_interior = room_size_interior;
        this.room_name = room_name;
        this.room_id = room_id;
        this.room_no_bathroom = room_no_bathroom;
        this.room_rent_night = room_rent_night;
        this.userss = new ArrayList<>();
    }

    public Room(
        int room_no_bedroom,        int room_size_interior,        String room_name,        int room_id,        int room_no_bathroom,        float room_rent_night        ArrayList<Users> userss    ) {
        this.room_no_bedroom = room_no_bedroom;
        this.room_size_interior = room_size_interior;
        this.room_name = room_name;
        this.room_id = room_id;
        this.room_no_bathroom = room_no_bathroom;
        this.room_rent_night = room_rent_night;
        this.userss = userss;
    }

    public int getRoom_no_bedroom() {
        return room_no_bedroom;
    }

    public void setRoom_no_bedroom(int room_no_bedroom) {
        this.room_no_bedroom = room_no_bedroom;
    }
    public int getRoom_size_interior() {
        return room_size_interior;
    }

    public void setRoom_size_interior(int room_size_interior) {
        this.room_size_interior = room_size_interior;
    }
    public String getRoom_name() {
        return room_name;
    }

    public void setRoom_name(String room_name) {
        this.room_name = room_name;
    }
    public int getRoom_id() {
        return room_id;
    }

    public void setRoom_id(int room_id) {
        this.room_id = room_id;
    }
    public int getRoom_no_bathroom() {
        return room_no_bathroom;
    }

    public void setRoom_no_bathroom(int room_no_bathroom) {
        this.room_no_bathroom = room_no_bathroom;
    }
    public float getRoom_rent_night() {
        return room_rent_night;
    }

    public void setRoom_rent_night(float room_rent_night) {
        this.room_rent_night = room_rent_night;
    }

    public Hotel getHotel() {
        return hotel;
    }

    public void setHotel(Hotel hotel) {
        this.hotel = hotel;
    }
    public List<Users> getUserss() {
        return userss;
    }

    public void addUsers(Users users) {
        this.userss.add(users);
    }

}