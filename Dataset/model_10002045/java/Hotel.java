





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String name;





    private List<RoomType> roomtypes;




    private List<Booking> bookings;


    public Hotel(
        String name    ) {
        this.name = name;
        this.roomtypes = new ArrayList<>();
        this.bookings = new ArrayList<>();
    }

    public Hotel(
        String name        ArrayList<RoomType> roomtypes,        ArrayList<Booking> bookings    ) {
        this.name = name;
        this.roomtypes = roomtypes;
        this.bookings = bookings;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<RoomType> getRoomtypes() {
        return roomtypes;
    }

    public void addRoomtype(Roomtype roomtype) {
        this.roomtypes.add(roomtype);
    }
    public List<Booking> getBookings() {
        return bookings;
    }

    public void addBooking(Booking booking) {
        this.bookings.add(booking);
    }

}