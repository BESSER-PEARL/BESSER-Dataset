





import java.util.List;
import java.util.ArrayList;

public class Classes_Datalayer_Database  {

    private String extrasDB;





    private List<Booking> bookings;




    private List<Employee> employees;




    private List<Guest> guests;




    private UserHandler userhandler;




    private List<Room> rooms;


    public Classes_Datalayer_Database(
        String extrasDB    ) {
        this.extrasDB = extrasDB;
        this.bookings = new ArrayList<>();
        this.employees = new ArrayList<>();
        this.guests = new ArrayList<>();
        this.rooms = new ArrayList<>();
    }

    public Classes_Datalayer_Database(
        String extrasDB        ArrayList<Booking> bookings,        ArrayList<Employee> employees,        ArrayList<Guest> guests,        ArrayList<Room> rooms    ) {
        this.extrasDB = extrasDB;
        this.bookings = bookings;
        this.employees = employees;
        this.guests = guests;
        this.rooms = rooms;
    }

    public String getExtrasdb() {
        return extrasDB;
    }

    public void setExtrasdb(String extrasDB) {
        this.extrasDB = extrasDB;
    }

    public List<Booking> getBookings() {
        return bookings;
    }

    public void addBooking(Booking booking) {
        this.bookings.add(booking);
    }
    public List<Employee> getEmployees() {
        return employees;
    }

    public void addEmployee(Employee employee) {
        this.employees.add(employee);
    }
    public List<Guest> getGuests() {
        return guests;
    }

    public void addGuest(Guest guest) {
        this.guests.add(guest);
    }
    public UserHandler getUserhandler() {
        return userhandler;
    }

    public void setUserhandler(UserHandler userhandler) {
        this.userhandler = userhandler;
    }
    public List<Room> getRooms() {
        return rooms;
    }

    public void addRoom(Room room) {
        this.rooms.add(room);
    }

}