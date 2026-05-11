





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_ProgramPartner  {

    private int numberOfCustomers;
    private String name;





    private RoyalAndLoyal_Service royalandloyal_service;




    private List<RoyalAndLoyal_LoyaltyProgram> royalandloyal_loyaltyprograms;




    private List<RoyalAndLoyal_Service> royalandloyal_services;




    private RoyalAndLoyal_LoyaltyProgram royalandloyal_loyaltyprogram;


    public RoyalAndLoyal_ProgramPartner(
        int numberOfCustomers,        String name    ) {
        this.numberOfCustomers = numberOfCustomers;
        this.name = name;
        this.royalandloyal_loyaltyprograms = new ArrayList<>();
        this.royalandloyal_services = new ArrayList<>();
    }

    public RoyalAndLoyal_ProgramPartner(
        int numberOfCustomers,        String name        ArrayList<RoyalAndLoyal_LoyaltyProgram> royalandloyal_loyaltyprograms,        ArrayList<RoyalAndLoyal_Service> royalandloyal_services    ) {
        this.numberOfCustomers = numberOfCustomers;
        this.name = name;
        this.royalandloyal_loyaltyprograms = royalandloyal_loyaltyprograms;
        this.royalandloyal_services = royalandloyal_services;
    }

    public int getNumberofcustomers() {
        return numberOfCustomers;
    }

    public void setNumberofcustomers(int numberOfCustomers) {
        this.numberOfCustomers = numberOfCustomers;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RoyalAndLoyal_Service getRoyalandloyal_service() {
        return royalandloyal_service;
    }

    public void setRoyalandloyal_service(RoyalAndLoyal_Service royalandloyal_service) {
        this.royalandloyal_service = royalandloyal_service;
    }
    public List<RoyalAndLoyal_LoyaltyProgram> getRoyalandloyal_loyaltyprograms() {
        return royalandloyal_loyaltyprograms;
    }

    public void addRoyalandloyal_loyaltyprogram(Royalandloyal_loyaltyprogram royalandloyal_loyaltyprogram) {
        this.royalandloyal_loyaltyprograms.add(royalandloyal_loyaltyprogram);
    }
    public List<RoyalAndLoyal_Service> getRoyalandloyal_services() {
        return royalandloyal_services;
    }

    public void addRoyalandloyal_service(Royalandloyal_service royalandloyal_service) {
        this.royalandloyal_services.add(royalandloyal_service);
    }
    public RoyalAndLoyal_LoyaltyProgram getRoyalandloyal_loyaltyprogram() {
        return royalandloyal_loyaltyprogram;
    }

    public void setRoyalandloyal_loyaltyprogram(RoyalAndLoyal_LoyaltyProgram royalandloyal_loyaltyprogram) {
        this.royalandloyal_loyaltyprogram = royalandloyal_loyaltyprogram;
    }

}