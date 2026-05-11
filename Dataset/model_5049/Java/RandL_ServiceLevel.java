





import java.util.List;
import java.util.ArrayList;

public class RandL_ServiceLevel  {

    private String name;





    private RandL_LoyaltyProgram randl_loyaltyprogram;




    private List<RandL_Membership> randl_memberships;




    private RandL_Membership randl_membership;




    private RandL_CustomerCard randl_customercard;




    private RandL_LoyaltyProgram randl_loyaltyprogram;




    private List<RandL_Service> randl_services;




    private RandL_Service randl_service;


    public RandL_ServiceLevel(
        String name    ) {
        this.name = name;
        this.randl_memberships = new ArrayList<>();
        this.randl_services = new ArrayList<>();
    }

    public RandL_ServiceLevel(
        String name        ArrayList<RandL_Membership> randl_memberships,        ArrayList<RandL_Service> randl_services    ) {
        this.name = name;
        this.randl_memberships = randl_memberships;
        this.randl_services = randl_services;
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
    public List<RandL_Membership> getRandl_memberships() {
        return randl_memberships;
    }

    public void addRandl_membership(Randl_membership randl_membership) {
        this.randl_memberships.add(randl_membership);
    }
    public RandL_Membership getRandl_membership() {
        return randl_membership;
    }

    public void setRandl_membership(RandL_Membership randl_membership) {
        this.randl_membership = randl_membership;
    }
    public RandL_CustomerCard getRandl_customercard() {
        return randl_customercard;
    }

    public void setRandl_customercard(RandL_CustomerCard randl_customercard) {
        this.randl_customercard = randl_customercard;
    }
    public RandL_LoyaltyProgram getRandl_loyaltyprogram() {
        return randl_loyaltyprogram;
    }

    public void setRandl_loyaltyprogram(RandL_LoyaltyProgram randl_loyaltyprogram) {
        this.randl_loyaltyprogram = randl_loyaltyprogram;
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