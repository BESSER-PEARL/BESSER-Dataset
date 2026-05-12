





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int floor;
    private String capacity;
    private int door;
    private float price;





    private List<Customer> customers;




    private Hotel hotel;


    public Room(
        int floor,        String capacity,        int door,        float price    ) {
        this.floor = floor;
        this.capacity = capacity;
        this.door = door;
        this.price = price;
        this.customers = new ArrayList<>();
    }

    public Room(
        int floor,        String capacity,        int door,        float price        ArrayList<Customer> customers    ) {
        this.floor = floor;
        this.capacity = capacity;
        this.door = door;
        this.price = price;
        this.customers = customers;
    }

    public int getFloor() {
        return floor;
    }

    public void setFloor(int floor) {
        this.floor = floor;
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