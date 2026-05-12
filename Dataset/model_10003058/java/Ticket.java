





import java.util.List;
import java.util.ArrayList;

public class Ticket  {

    private String Customer_Name;
    private boolean Price;
    private int Id;
    private String Type;





    private Customer customer;




    private Flight flight;


    public Ticket(
        String Customer_Name,        boolean Price,        int Id,        String Type    ) {
        this.Customer_Name = Customer_Name;
        this.Price = Price;
        this.Id = Id;
        this.Type = Type;
    }


    public String getCustomer_name() {
        return Customer_Name;
    }

    public void setCustomer_name(String Customer_Name) {
        this.Customer_Name = Customer_Name;
    }
    public boolean getPrice() {
        return Price;
    }

    public void setPrice(boolean Price) {
        this.Price = Price;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Flight getFlight() {
        return flight;
    }

    public void setFlight(Flight flight) {
        this.flight = flight;
    }

}