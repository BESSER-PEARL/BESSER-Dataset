





import java.util.List;
import java.util.ArrayList;

public class RandL_ProgramPartner  {

    private String name;
    private String numberOfCustomers;





    private List<RandL_Service> randl_services;




    private RandL_Service randl_service;




    private RandL_LoyaltyProgram randl_loyaltyprogram;




    private List<RandL_LoyaltyProgram> randl_loyaltyprograms;


    public RandL_ProgramPartner(
        String name,        String numberOfCustomers    ) {
        this.name = name;
        this.numberOfCustomers = numberOfCustomers;
        this.randl_services = new ArrayList<>();
        this.randl_loyaltyprograms = new ArrayList<>();
    }

    public RandL_ProgramPartner(
        String name,        String numberOfCustomers        ArrayList<RandL_Service> randl_services,        ArrayList<RandL_LoyaltyProgram> randl_loyaltyprograms    ) {
        this.name = name;
        this.numberOfCustomers = numberOfCustomers;
        this.randl_services = randl_services;
        this.randl_loyaltyprograms = randl_loyaltyprograms;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getNumberofcustomers() {
        return numberOfCustomers;
    }

    public void setNumberofcustomers(String numberOfCustomers) {
        this.numberOfCustomers = numberOfCustomers;
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

}