





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private int floor;
    private float price;
    private int door;
    private String capacity;





    private List<Customer> customers;




    private Hotel hotel;


    public Room(
        int floor,        float price,        int door,        String capacity    ) {
        this.floor = floor;
        this.price = price;
        this.door = door;
        this.capacity = capacity;
        this.customers = new ArrayList<>();
    }

    public Room(
        int floor,        float price,        int door,        String capacity        ArrayList<Customer> customers    ) {
        this.floor = floor;
        this.price = price;
        this.door = door;
        this.capacity = capacity;
        this.customers = customers;
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
    public int getDoor() {
        return door;
    }

    public void setDoor(int door) {
        this.door = door;
    }
    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
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