





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_LoyaltyProgram  {






    private RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel;




    private List<RoyalAndLoyal_ServiceLevel> royalandloyal_servicelevels;




    private RoyalAndLoyal_Customer royalandloyal_customer;




    private RoyalAndLoyal_ProgramPartner royalandloyal_programpartner;




    private List<RoyalAndLoyal_ProgramPartner> royalandloyal_programpartners;




    private RoyalAndLoyal_Container_RandL royalandloyal_container_randl;




    private List<RoyalAndLoyal_Customer> royalandloyal_customers;


    public RoyalAndLoyal_LoyaltyProgram(
    ) {
        this.royalandloyal_servicelevels = new ArrayList<>();
        this.royalandloyal_programpartners = new ArrayList<>();
        this.royalandloyal_customers = new ArrayList<>();
    }

    public RoyalAndLoyal_LoyaltyProgram(
        ArrayList<RoyalAndLoyal_ServiceLevel> royalandloyal_servicelevels,        ArrayList<RoyalAndLoyal_ProgramPartner> royalandloyal_programpartners,        ArrayList<RoyalAndLoyal_Customer> royalandloyal_customers    ) {
        this.royalandloyal_servicelevels = royalandloyal_servicelevels;
        this.royalandloyal_programpartners = royalandloyal_programpartners;
        this.royalandloyal_customers = royalandloyal_customers;
    }


    public RoyalAndLoyal_ServiceLevel getRoyalandloyal_servicelevel() {
        return royalandloyal_servicelevel;
    }

    public void setRoyalandloyal_servicelevel(RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel) {
        this.royalandloyal_servicelevel = royalandloyal_servicelevel;
    }
    public List<RoyalAndLoyal_ServiceLevel> getRoyalandloyal_servicelevels() {
        return royalandloyal_servicelevels;
    }

    public void addRoyalandloyal_servicelevel(Royalandloyal_servicelevel royalandloyal_servicelevel) {
        this.royalandloyal_servicelevels.add(royalandloyal_servicelevel);
    }
    public RoyalAndLoyal_Customer getRoyalandloyal_customer() {
        return royalandloyal_customer;
    }

    public void setRoyalandloyal_customer(RoyalAndLoyal_Customer royalandloyal_customer) {
        this.royalandloyal_customer = royalandloyal_customer;
    }
    public RoyalAndLoyal_ProgramPartner getRoyalandloyal_programpartner() {
        return royalandloyal_programpartner;
    }

    public void setRoyalandloyal_programpartner(RoyalAndLoyal_ProgramPartner royalandloyal_programpartner) {
        this.royalandloyal_programpartner = royalandloyal_programpartner;
    }
    public List<RoyalAndLoyal_ProgramPartner> getRoyalandloyal_programpartners() {
        return royalandloyal_programpartners;
    }

    public void addRoyalandloyal_programpartner(Royalandloyal_programpartner royalandloyal_programpartner) {
        this.royalandloyal_programpartners.add(royalandloyal_programpartner);
    }
    public RoyalAndLoyal_Container_RandL getRoyalandloyal_container_randl() {
        return royalandloyal_container_randl;
    }

    public void setRoyalandloyal_container_randl(RoyalAndLoyal_Container_RandL royalandloyal_container_randl) {
        this.royalandloyal_container_randl = royalandloyal_container_randl;
    }
    public List<RoyalAndLoyal_Customer> getRoyalandloyal_customers() {
        return royalandloyal_customers;
    }

    public void addRoyalandloyal_customer(Royalandloyal_customer royalandloyal_customer) {
        this.royalandloyal_customers.add(royalandloyal_customer);
    }

}