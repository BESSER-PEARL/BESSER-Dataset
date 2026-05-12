





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_ProgramPartner  {

    private int numberOfCustomers;





    private List<RoyalAndLoyal_Service> royalandloyal_services;


    public RoyalAndLoyal_ProgramPartner(
        int numberOfCustomers    ) {
        this.numberOfCustomers = numberOfCustomers;
        this.royalandloyal_services = new ArrayList<>();
    }

    public RoyalAndLoyal_ProgramPartner(
        int numberOfCustomers        ArrayList<RoyalAndLoyal_Service> royalandloyal_services    ) {
        this.numberOfCustomers = numberOfCustomers;
        this.royalandloyal_services = royalandloyal_services;
    }

    public int getNumberofcustomers() {
        return numberOfCustomers;
    }

    public void setNumberofcustomers(int numberOfCustomers) {
        this.numberOfCustomers = numberOfCustomers;
    }

    public List<RoyalAndLoyal_Service> getRoyalandloyal_services() {
        return royalandloyal_services;
    }

    public void addRoyalandloyal_service(Royalandloyal_service royalandloyal_service) {
        this.royalandloyal_services.add(royalandloyal_service);
    }

}