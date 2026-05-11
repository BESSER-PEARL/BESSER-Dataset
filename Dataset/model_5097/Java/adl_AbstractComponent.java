





import java.util.List;
import java.util.ArrayList;

public class adl_AbstractComponent  {






    private List<adl_Required> adl_requireds;




    private List<adl_Provided> adl_provideds;


    public adl_AbstractComponent(
    ) {
        this.adl_requireds = new ArrayList<>();
        this.adl_provideds = new ArrayList<>();
    }

    public adl_AbstractComponent(
        ArrayList<adl_Required> adl_requireds,        ArrayList<adl_Provided> adl_provideds    ) {
        this.adl_requireds = adl_requireds;
        this.adl_provideds = adl_provideds;
    }


    public List<adl_Required> getAdl_requireds() {
        return adl_requireds;
    }

    public void addAdl_required(Adl_required adl_required) {
        this.adl_requireds.add(adl_required);
    }
    public List<adl_Provided> getAdl_provideds() {
        return adl_provideds;
    }

    public void addAdl_provided(Adl_provided adl_provided) {
        this.adl_provideds.add(adl_provided);
    }

}