





import java.util.List;
import java.util.ArrayList;

public class Reservation  {






    private List<Flight> flights;




    private List<Customers> customerss;


    public Reservation(
    ) {
        this.flights = new ArrayList<>();
        this.customerss = new ArrayList<>();
    }

    public Reservation(
        ArrayList<Flight> flights,        ArrayList<Customers> customerss    ) {
        this.flights = flights;
        this.customerss = customerss;
    }


    public List<Flight> getFlights() {
        return flights;
    }

    public void addFlight(Flight flight) {
        this.flights.add(flight);
    }
    public List<Customers> getCustomerss() {
        return customerss;
    }

    public void addCustomers(Customers customers) {
        this.customerss.add(customers);
    }

}