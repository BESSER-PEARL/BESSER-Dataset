





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private float price;
    private int floor;
    private int door;
    private String capacity;





    private List<Customer> customers;




    private Hotel hotel;


    public Room(
        float price,        int floor,        int door,        String capacity    ) {
        this.price = price;
        this.floor = floor;
        this.door = door;
        this.capacity = capacity;
        this.customers = new ArrayList<>();
    }

    public Room(
        float price,        int floor,        int door,        String capacity        ArrayList<Customer> customers    ) {
        this.price = price;
        this.floor = floor;
        this.door = door;
        this.capacity = capacity;
        this.customers = customers;
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