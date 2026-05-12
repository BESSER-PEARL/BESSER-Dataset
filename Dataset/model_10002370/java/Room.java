





import java.util.List;
import java.util.ArrayList;

public class Room  {

    private String capacity;
    private float price;
    private int floor;
    private int door;





    private Hotel hotel;




    private List<Customer> customers;


    public Room(
        String capacity,        float price,        int floor,        int door    ) {
        this.capacity = capacity;
        this.price = price;
        this.floor = floor;
        this.door = door;
        this.customers = new ArrayList<>();
    }

    public Room(
        String capacity,        float price,        int floor,        int door        ArrayList<Customer> customers    ) {
        this.capacity = capacity;
        this.price = price;
        this.floor = floor;
        this.door = door;
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