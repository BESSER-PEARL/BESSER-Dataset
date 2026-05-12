





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Name;
    private boolean Reservation;
    private String date;
    private String reservedTables;
    private int Contact_Number;
    private String Dishes_Ordered;





    private Waiter waiter;


    public Customer(
        String Name,        boolean Reservation,        String date,        String reservedTables,        int Contact_Number,        String Dishes_Ordered    ) {
        this.Name = Name;
        this.Reservation = Reservation;
        this.date = date;
        this.reservedTables = reservedTables;
        this.Contact_Number = Contact_Number;
        this.Dishes_Ordered = Dishes_Ordered;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getReservation() {
        return Reservation;
    }

    public void setReservation(boolean Reservation) {
        this.Reservation = Reservation;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getReservedtables() {
        return reservedTables;
    }

    public void setReservedtables(String reservedTables) {
        this.reservedTables = reservedTables;
    }
    public int getContact_number() {
        return Contact_Number;
    }

    public void setContact_number(int Contact_Number) {
        this.Contact_Number = Contact_Number;
    }
    public String getDishes_ordered() {
        return Dishes_Ordered;
    }

    public void setDishes_ordered(String Dishes_Ordered) {
        this.Dishes_Ordered = Dishes_Ordered;
    }

    public Waiter getWaiter() {
        return waiter;
    }

    public void setWaiter(Waiter waiter) {
        this.waiter = waiter;
    }

}