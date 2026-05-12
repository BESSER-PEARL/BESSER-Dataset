





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int door;
    private int floor;
    private float price;
    private String capacity;





    private Hotel hotel;




    private List<Customer> customers;


    public Room(
        int door,        int floor,        float price,        String capacity    ) {
        this.door = door;
        this.floor = floor;
        this.price = price;
        this.capacity = capacity;
        this.customers = new ArrayList<>();
    }

    public Room(
        int door,        int floor,        float price,        String capacity        ArrayList<Customer> customers    ) {
        this.door = door;
        this.floor = floor;
        this.price = price;
        this.capacity = capacity;
        this.customers = customers;
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
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }

    public Hotel getHotel() {
        return hotel;
    }

    public void setHotel(Hotel hotel) {
        this.hotel = hotel;
    }
    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}