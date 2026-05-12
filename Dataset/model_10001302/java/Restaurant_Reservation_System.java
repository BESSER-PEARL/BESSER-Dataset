





import java.util.List;
import java.util.ArrayList;

public class Restaurant_Reservation_System  {

    private String Menu;
    private String bookings;



    public Restaurant_Reservation_System(
        String Menu,        String bookings    ) {
        this.Menu = Menu;
        this.bookings = bookings;
    }


    public String getMenu() {
        return Menu;
    }

    public void setMenu(String Menu) {
        this.Menu = Menu;
    }
    public String getBookings() {
        return bookings;
    }

    public void setBookings(String bookings) {
        this.bookings = bookings;
    }


}