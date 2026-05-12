





import java.util.List;
import java.util.ArrayList;

public class admin  {

    private int cost;
    private String name_of_flight;
    private String username;
    private int seats;
    private String pwd;
    private String type;





    private List<customer> customers;


    public admin(
        int cost,        String name_of_flight,        String username,        int seats,        String pwd,        String type    ) {
        this.cost = cost;
        this.name_of_flight = name_of_flight;
        this.username = username;
        this.seats = seats;
        this.pwd = pwd;
        this.type = type;
        this.customers = new ArrayList<>();
    }

    public admin(
        int cost,        String name_of_flight,        String username,        int seats,        String pwd,        String type        ArrayList<customer> customers    ) {
        this.cost = cost;
        this.name_of_flight = name_of_flight;
        this.username = username;
        this.seats = seats;
        this.pwd = pwd;
        this.type = type;
        this.customers = customers;
    }

    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }
    public String getName_of_flight() {
        return name_of_flight;
    }

    public void setName_of_flight(String name_of_flight) {
        this.name_of_flight = name_of_flight;
    }
    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }
    public int getSeats() {
        return seats;
    }

    public void setSeats(int seats) {
        this.seats = seats;
    }
    public String getPwd() {
        return pwd;
    }

    public void setPwd(String pwd) {
        this.pwd = pwd;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}