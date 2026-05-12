





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int room_size_interior;
    private int room_no_bathroom;
    private int room_no_bedroom;
    private String room_name;
    private float room_rent_night;
    private int room_id;





    private List<Users> userss;




    private Hotel hotel;


    public Room(
        int room_size_interior,        int room_no_bathroom,        int room_no_bedroom,        String room_name,        float room_rent_night,        int room_id    ) {
        this.room_size_interior = room_size_interior;
        this.room_no_bathroom = room_no_bathroom;
        this.room_no_bedroom = room_no_bedroom;
        this.room_name = room_name;
        this.room_rent_night = room_rent_night;
        this.room_id = room_id;
        this.userss = new ArrayList<>();
    }

    public Room(
        int room_size_interior,        int room_no_bathroom,        int room_no_bedroom,        String room_name,        float room_rent_night,        int room_id        ArrayList<Users> userss    ) {
        this.room_size_interior = room_size_interior;
        this.room_no_bathroom = room_no_bathroom;
        this.room_no_bedroom = room_no_bedroom;
        this.room_name = room_name;
        this.room_rent_night = room_rent_night;
        this.room_id = room_id;
        this.userss = userss;
    }

    public int getRoom_size_interior() {
        return room_size_interior;
    }

    public void setRoom_size_interior(int room_size_interior) {
        this.room_size_interior = room_size_interior;
    }
    public int getRoom_no_bathroom() {
        return room_no_bathroom;
    }

    public void setRoom_no_bathroom(int room_no_bathroom) {
        this.room_no_bathroom = room_no_bathroom;
    }
    public int getRoom_no_bedroom() {
        return room_no_bedroom;
    }

    public void setRoom_no_bedroom(int room_no_bedroom) {
        this.room_no_bedroom = room_no_bedroom;
    }
    public String getRoom_name() {
        return room_name;
    }

    public void setRoom_name(String room_name) {
        this.room_name = room_name;
    }
    public float getRoom_rent_night() {
        return room_rent_night;
    }

    public void setRoom_rent_night(float room_rent_night) {
        this.room_rent_night = room_rent_night;
    }
    public int getRoom_id() {
        return room_id;
    }

    public void setRoom_id(int room_id) {
        this.room_id = room_id;
    }

    public List<Users> getUserss() {
        return userss;
    }

    public void addUsers(Users users) {
        this.userss.add(users);
    }
    public Hotel getHotel() {
        return hotel;
    }

    public void setHotel(Hotel hotel) {
        this.hotel = hotel;
    }

}