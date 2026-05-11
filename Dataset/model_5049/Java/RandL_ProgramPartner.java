





import java.util.List;
import java.util.ArrayList;

public class RandL_ProgramPartner  {

    private String numberOfCustomers;
    private String name;





    private RandL_LoyaltyProgram randl_loyaltyprogram;




    private List<RandL_LoyaltyProgram> randl_loyaltyprograms;




    private List<RandL_Service> randl_services;




    private RandL_Service randl_service;


    public RandL_ProgramPartner(
        String numberOfCustomers,        String name    ) {
        this.numberOfCustomers = numberOfCustomers;
        this.name = name;
        this.randl_loyaltyprograms = new ArrayList<>();
        this.randl_services = new ArrayList<>();
    }

    public RandL_ProgramPartner(
        String numberOfCustomers,        String name        ArrayList<RandL_LoyaltyProgram> randl_loyaltyprograms,        ArrayList<RandL_Service> randl_services    ) {
        this.numberOfCustomers = numberOfCustomers;
        this.name = name;
        this.randl_loyaltyprograms = randl_loyaltyprograms;
        this.randl_services = randl_services;
    }

    public String getNumberofcustomers() {
        return numberOfCustomers;
    }

    public void setNumberofcustomers(String numberOfCustomers) {
        this.numberOfCustomers = numberOfCustomers;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RandL_LoyaltyProgram getRandl_loyaltyprogram() {
        return randl_loyaltyprogram;
    }

    public void setRandl_loyaltyprogram(RandL_LoyaltyProgram randl_loyaltyprogram) {
        this.randl_loyaltyprogram = randl_loyaltyprogram;
    }
    public List<RandL_LoyaltyProgram> getRandl_loyaltyprograms() {
        return randl_loyaltyprograms;
    }

    public void addRandl_loyaltyprogram(Randl_loyaltyprogram randl_loyaltyprogram) {
        this.randl_loyaltyprograms.add(randl_loyaltyprogram);
    }
    public List<RandL_Service> getRandl_services() {
        return randl_services;
    }

    public void addRandl_service(Randl_service randl_service) {
        this.randl_services.add(randl_service);
    }
    public RandL_Service getRandl_service() {
        return randl_service;
    }

    public void setRandl_service(RandL_Service randl_service) {
        this.randl_service = randl_service;
    }

}