





import java.util.List;
import java.util.ArrayList;

public class RoyalAndLoyal_LoyaltyProgram  {

    private String name;





    private List<RoyalAndLoyal_ServiceLevel> royalandloyal_servicelevels;




    private RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel;


    public RoyalAndLoyal_LoyaltyProgram(
        String name    ) {
        this.name = name;
        this.royalandloyal_servicelevels = new ArrayList<>();
    }

    public RoyalAndLoyal_LoyaltyProgram(
        String name        ArrayList<RoyalAndLoyal_ServiceLevel> royalandloyal_servicelevels    ) {
        this.name = name;
        this.royalandloyal_servicelevels = royalandloyal_servicelevels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<RoyalAndLoyal_ServiceLevel> getRoyalandloyal_servicelevels() {
        return royalandloyal_servicelevels;
    }

    public void addRoyalandloyal_servicelevel(Royalandloyal_servicelevel royalandloyal_servicelevel) {
        this.royalandloyal_servicelevels.add(royalandloyal_servicelevel);
    }
    public RoyalAndLoyal_ServiceLevel getRoyalandloyal_servicelevel() {
        return royalandloyal_servicelevel;
    }

    public void setRoyalandloyal_servicelevel(RoyalAndLoyal_ServiceLevel royalandloyal_servicelevel) {
        this.royalandloyal_servicelevel = royalandloyal_servicelevel;
    }

}