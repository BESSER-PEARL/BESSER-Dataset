





import java.util.List;
import java.util.ArrayList;

public class Table  {

    private int seats;
    private int tableNumber;





    private Customer customer;


    public Table(
        int seats,        int tableNumber    ) {
        this.seats = seats;
        this.tableNumber = tableNumber;
    }


    public int getSeats() {
        return seats;
    }

    public void setSeats(int seats) {
        this.seats = seats;
    }
    public int getTablenumber() {
        return tableNumber;
    }

    public void setTablenumber(int tableNumber) {
        this.tableNumber = tableNumber;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}