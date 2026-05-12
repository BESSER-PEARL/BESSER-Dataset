





import java.util.List;
import java.util.ArrayList;

public class Address  {

    private String City;
    private String Line1;
    private String Line_2;
    private String County;





    private List<Order> orders;




    private Customer customer;


    public Address(
        String City,        String Line1,        String Line_2,        String County    ) {
        this.City = City;
        this.Line1 = Line1;
        this.Line_2 = Line_2;
        this.County = County;
        this.orders = new ArrayList<>();
    }

    public Address(
        String City,        String Line1,        String Line_2,        String County        ArrayList<Order> orders    ) {
        this.City = City;
        this.Line1 = Line1;
        this.Line_2 = Line_2;
        this.County = County;
        this.orders = orders;
    }

    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }
    public String getLine1() {
        return Line1;
    }

    public void setLine1(String Line1) {
        this.Line1 = Line1;
    }
    public String getLine_2() {
        return Line_2;
    }

    public void setLine_2(String Line_2) {
        this.Line_2 = Line_2;
    }
    public String getCounty() {
        return County;
    }

    public void setCounty(String County) {
        this.County = County;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}