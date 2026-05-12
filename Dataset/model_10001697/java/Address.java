





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private String House;
    private String City;
    private String Street;





    private Order order;




    private Customer1 customer1;


    public Address(
        String House,        String City,        String Street    ) {
        this.House = House;
        this.City = City;
        this.Street = Street;
    }


    public String getHouse() {
        return House;
    }

    public void setHouse(String House) {
        this.House = House;
    }
    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }
    public String getStreet() {
        return Street;
    }

    public void setStreet(String Street) {
        this.Street = Street;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }
    public Customer1 getCustomer1() {
        return customer1;
    }

    public void setCustomer1(Customer1 customer1) {
        this.customer1 = customer1;
    }

}