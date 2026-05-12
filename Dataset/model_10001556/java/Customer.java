





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String date;
    private String Dishes_Ordered;
    private String Name;
    private int Contact_Number;
    private boolean Reservation;
    private String reservedTables;





    private Waiter waiter;


    public Customer(
        String date,        String Dishes_Ordered,        String Name,        int Contact_Number,        boolean Reservation,        String reservedTables    ) {
        this.date = date;
        this.Dishes_Ordered = Dishes_Ordered;
        this.Name = Name;
        this.Contact_Number = Contact_Number;
        this.Reservation = Reservation;
        this.reservedTables = reservedTables;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getDishes_ordered() {
        return Dishes_Ordered;
    }

    public void setDishes_ordered(String Dishes_Ordered) {
        this.Dishes_Ordered = Dishes_Ordered;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getContact_number() {
        return Contact_Number;
    }

    public void setContact_number(int Contact_Number) {
        this.Contact_Number = Contact_Number;
    }
    public boolean getReservation() {
        return Reservation;
    }

    public void setReservation(boolean Reservation) {
        this.Reservation = Reservation;
    }
    public String getReservedtables() {
        return reservedTables;
    }

    public void setReservedtables(String reservedTables) {
        this.reservedTables = reservedTables;
    }

    public Waiter getWaiter() {
        return waiter;
    }

    public void setWaiter(Waiter waiter) {
        this.waiter = waiter;
    }

}