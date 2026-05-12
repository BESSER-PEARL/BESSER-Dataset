





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_ServiceLevel  {






    private List<RoyalAndLoyal_Service> royalandloyal_services;


    public RoyalAndLoyal_ServiceLevel(
    ) {
        this.royalandloyal_services = new ArrayList<>();
    }

    public RoyalAndLoyal_ServiceLevel(
        ArrayList<RoyalAndLoyal_Service> royalandloyal_services    ) {
        this.royalandloyal_services = royalandloyal_services;
    }


    public List<RoyalAndLoyal_Service> getRoyalandloyal_services() {
        return royalandloyal_services;
    }

    public void addRoyalandloyal_service(Royalandloyal_service royalandloyal_service) {
        this.royalandloyal_services.add(royalandloyal_service);
    }

}