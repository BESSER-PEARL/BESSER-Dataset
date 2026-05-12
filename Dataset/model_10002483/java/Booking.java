





import java.util.List;
import java.util.ArrayList;

public class Booking  {

    private int guest_name;
    private String guest_adress;
    private int booking_id;
    private int guest_id;
    private int guestphn_no;
    private int user_id;





    private Rooms rooms;




    private User user;


    public Booking(
        int guest_name,        String guest_adress,        int booking_id,        int guest_id,        int guestphn_no,        int user_id    ) {
        this.guest_name = guest_name;
        this.guest_adress = guest_adress;
        this.booking_id = booking_id;
        this.guest_id = guest_id;
        this.guestphn_no = guestphn_no;
        this.user_id = user_id;
    }


    public int getGuest_name() {
        return guest_name;
    }

    public void setGuest_name(int guest_name) {
        this.guest_name = guest_name;
    }
    public String getGuest_adress() {
        return guest_adress;
    }

    public void setGuest_adress(String guest_adress) {
        this.guest_adress = guest_adress;
    }
    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }
    public int getGuest_id() {
        return guest_id;
    }

    public void setGuest_id(int guest_id) {
        this.guest_id = guest_id;
    }
    public int getGuestphn_no() {
        return guestphn_no;
    }

    public void setGuestphn_no(int guestphn_no) {
        this.guestphn_no = guestphn_no;
    }
    public int getUser_id() {
        return user_id;
    }

    public void setUser_id(int user_id) {
        this.user_id = user_id;
    }

    public Rooms getRooms() {
        return rooms;
    }

    public void setRooms(Rooms rooms) {
        this.rooms = rooms;
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}