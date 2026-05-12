




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String number;
    private LocalDate ordered;
    private String ship_to;
    private LocalDate shipped;





    private Customer customer;


    public Order(
        String number,        LocalDate ordered,        String ship_to,        LocalDate shipped    ) {
        this.number = number;
        this.ordered = ordered;
        this.ship_to = ship_to;
        this.shipped = shipped;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
    }
    public String getShip_to() {
        return ship_to;
    }

    public void setShip_to(String ship_to) {
        this.ship_to = ship_to;
    }
    public LocalDate getShipped() {
        return shipped;
    }

    public void setShipped(LocalDate shipped) {
        this.shipped = shipped;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}