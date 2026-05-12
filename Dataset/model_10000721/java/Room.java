





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String capacity;
    private float price;
    private int door;
    private int floor;





    private List<Customer> customers;




    private Hotel hotel;


    public Room(
        String capacity,        float price,        int door,        int floor    ) {
        this.capacity = capacity;
        this.price = price;
        this.door = door;
        this.floor = floor;
        this.customers = new ArrayList<>();
    }

    public Room(
        String capacity,        float price,        int door,        int floor        ArrayList<Customer> customers    ) {
        this.capacity = capacity;
        this.price = price;
        this.door = door;
        this.floor = floor;
        this.customers = customers;
    }

    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getDoor() {
        return door;
    }

    public void setDoor(int door) {
        this.door = door;
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