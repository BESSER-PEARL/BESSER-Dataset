





import java.util.List;
import java.util.ArrayList;

public class Reservation  {

    private None seats;
    private None table;





    private List<Order> orders;


    public Reservation(
        None seats,        None table    ) {
        this.seats = seats;
        this.table = table;
        this.orders = new ArrayList<>();
    }

    public Reservation(
        None seats,        None table        ArrayList<Order> orders    ) {
        this.seats = seats;
        this.table = table;
        this.orders = orders;
    }

    public None getSeats() {
        return seats;
    }

    public void setSeats(None seats) {
        this.seats = seats;
    }
    public None getTable() {
        return table;
    }

    public void setTable(None table) {
        this.table = table;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}