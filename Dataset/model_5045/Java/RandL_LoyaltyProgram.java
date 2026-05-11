





import java.util.List;
import java.util.ArrayList;

public class RandL_LoyaltyProgram  {

    private String name;





    private RandL_ServiceLevel randl_servicelevel;




    private List<RandL_ServiceLevel> randl_servicelevels;


    public RandL_LoyaltyProgram(
        String name    ) {
        this.name = name;
        this.randl_servicelevels = new ArrayList<>();
    }

    public RandL_LoyaltyProgram(
        String name        ArrayList<RandL_ServiceLevel> randl_servicelevels    ) {
        this.name = name;
        this.randl_servicelevels = randl_servicelevels;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RandL_ServiceLevel getRandl_servicelevel() {
        return randl_servicelevel;
    }

    public void setRandl_servicelevel(RandL_ServiceLevel randl_servicelevel) {
        this.randl_servicelevel = randl_servicelevel;
    }
    public List<RandL_ServiceLevel> getRandl_servicelevels() {
        return randl_servicelevels;
    }

    public void addRandl_servicelevel(Randl_servicelevel randl_servicelevel) {
        this.randl_servicelevels.add(randl_servicelevel);
    }

}