




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private int id;
    private LocalDate creationDate;





    private Customer customer;


    public ShoppingCart(
        int id,        LocalDate creationDate    ) {
        this.id = id;
        this.creationDate = creationDate;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}