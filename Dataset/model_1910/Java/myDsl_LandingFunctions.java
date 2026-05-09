





import java.util.List;
import java.util.ArrayList;

public class myDsl_LandingFunctions  {

    private String name;





    private myDsl_LandingActions mydsl_landingactions;


    public myDsl_LandingFunctions(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public myDsl_LandingActions getMydsl_landingactions() {
        return mydsl_landingactions;
    }

    public void setMydsl_landingactions(myDsl_LandingActions mydsl_landingactions) {
        this.mydsl_landingactions = mydsl_landingactions;
    }

}