





import java.util.List;
import java.util.ArrayList;

public class Hotel  {

    private String name;





    private HotelBusiness hotelbusiness;




    private List<Booking> bookings;




    private List<RoomType> roomtypes;


    public Hotel(
        String name    ) {
        this.name = name;
        this.bookings = new ArrayList<>();
        this.roomtypes = new ArrayList<>();
    }

    public Hotel(
        String name        ArrayList<Booking> bookings,        ArrayList<RoomType> roomtypes    ) {
        this.name = name;
        this.bookings = bookings;
        this.roomtypes = roomtypes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public HotelBusiness getHotelbusiness() {
        return hotelbusiness;
    }

    public void setHotelbusiness(HotelBusiness hotelbusiness) {
        this.hotelbusiness = hotelbusiness;
    }
    public List<Booking> getBookings() {
        return bookings;
    }

    public void addBooking(Booking booking) {
        this.bookings.add(booking);
    }
    public List<RoomType> getRoomtypes() {
        return roomtypes;
    }

    public void addRoomtype(Roomtype roomtype) {
        this.roomtypes.add(roomtype);
    }

}