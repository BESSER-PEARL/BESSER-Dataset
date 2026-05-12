





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String capacity;
    private int door;
    private float price;
    private int floor;





    private List<Customer> customers;




    private Hotel hotel;


    public Room(
        String capacity,        int door,        float price,        int floor    ) {
        this.capacity = capacity;
        this.door = door;
        this.price = price;
        this.floor = floor;
        this.customers = new ArrayList<>();
    }

    public Room(
        String capacity,        int door,        float price,        int floor        ArrayList<Customer> customers    ) {
        this.capacity = capacity;
        this.door = door;
        this.price = price;
        this.floor = floor;
        this.customers = customers;
    }

    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }
    public int getDoor() {
        return door;
    }

    public void setDoor(int door) {
        this.door = door;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }
    public Hotel getHotel() {
        return hotel;
    }

    public void setHotel(Hotel hotel) {
        this.hotel = hotel;
    }

}