





import java.util.List;
import java.util.ArrayList;

public class Classes_Buissnesslayer_BookingHandler  {






    private Database database;




    private Booking booking;




    private Booking booking;




    private List<User> users;




    private UserHandler userhandler;


    public Classes_Buissnesslayer_BookingHandler(
    ) {
        this.users = new ArrayList<>();
    }

    public Classes_Buissnesslayer_BookingHandler(
        ArrayList<User> users    ) {
        this.users = users;
    }


    public Database getDatabase() {
        return database;
    }

    public void setDatabase(Database database) {
        this.database = database;
    }
    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }
    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }
    public List<User> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }
    public UserHandler getUserhandler() {
        return userhandler;
    }

    public void setUserhandler(UserHandler userhandler) {
        this.userhandler = userhandler;
    }

}