





import java.util.List;
import java.util.ArrayList;

public class System  {






    private List<Hotel> hotels;




    private List<Customer> customers;


    public System(
    ) {
        this.hotels = new ArrayList<>();
        this.customers = new ArrayList<>();
    }

    public System(
        ArrayList<Hotel> hotels,        ArrayList<Customer> customers    ) {
        this.hotels = hotels;
        this.customers = customers;
    }


    public List<Hotel> getHotels() {
        return hotels;
    }

    public void addHotel(Hotel hotel) {
        this.hotels.add(hotel);
    }
    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}