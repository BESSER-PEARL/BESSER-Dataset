





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_Container_RandL  {






    private List<RoyalAndLoyal_Service> royalandloyal_services;




    private List<RoyalAndLoyal_ProgramPartner> royalandloyal_programpartners;




    private List<RoyalAndLoyal_Customer> royalandloyal_customers;




    private List<RoyalAndLoyal_ServiceLevel> royalandloyal_servicelevels;


    public RoyalAndLoyal_Container_RandL(
    ) {
        this.royalandloyal_services = new ArrayList<>();
        this.royalandloyal_programpartners = new ArrayList<>();
        this.royalandloyal_customers = new ArrayList<>();
        this.royalandloyal_servicelevels = new ArrayList<>();
    }

    public RoyalAndLoyal_Container_RandL(
        ArrayList<RoyalAndLoyal_Service> royalandloyal_services,        ArrayList<RoyalAndLoyal_ProgramPartner> royalandloyal_programpartners,        ArrayList<RoyalAndLoyal_Customer> royalandloyal_customers,        ArrayList<RoyalAndLoyal_ServiceLevel> royalandloyal_servicelevels    ) {
        this.royalandloyal_services = royalandloyal_services;
        this.royalandloyal_programpartners = royalandloyal_programpartners;
        this.royalandloyal_customers = royalandloyal_customers;
        this.royalandloyal_servicelevels = royalandloyal_servicelevels;
    }


    public List<RoyalAndLoyal_Service> getRoyalandloyal_services() {
        return royalandloyal_services;
    }

    public void addRoyalandloyal_service(Royalandloyal_service royalandloyal_service) {
        this.royalandloyal_services.add(royalandloyal_service);
    }
    public List<RoyalAndLoyal_ProgramPartner> getRoyalandloyal_programpartners() {
        return royalandloyal_programpartners;
    }

    public void addRoyalandloyal_programpartner(Royalandloyal_programpartner royalandloyal_programpartner) {
        this.royalandloyal_programpartners.add(royalandloyal_programpartner);
    }
    public List<RoyalAndLoyal_Customer> getRoyalandloyal_customers() {
        return royalandloyal_customers;
    }

    public void addRoyalandloyal_customer(Royalandloyal_customer royalandloyal_customer) {
        this.royalandloyal_customers.add(royalandloyal_customer);
    }
    public List<RoyalAndLoyal_ServiceLevel> getRoyalandloyal_servicelevels() {
        return royalandloyal_servicelevels;
    }

    public void addRoyalandloyal_servicelevel(Royalandloyal_servicelevel royalandloyal_servicelevel) {
        this.royalandloyal_servicelevels.add(royalandloyal_servicelevel);
    }

}