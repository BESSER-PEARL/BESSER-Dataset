





import java.util.List;
import java.util.ArrayList;

public class adlrecur_Component  {

    private String name;





    private List<adlrecur_Provided> adlrecur_provideds;




    private List<adlrecur_Required> adlrecur_requireds;


    public adlrecur_Component(
        String name    ) {
        this.name = name;
        this.adlrecur_provideds = new ArrayList<>();
        this.adlrecur_requireds = new ArrayList<>();
    }

    public adlrecur_Component(
        String name        ArrayList<adlrecur_Provided> adlrecur_provideds,        ArrayList<adlrecur_Required> adlrecur_requireds    ) {
        this.name = name;
        this.adlrecur_provideds = adlrecur_provideds;
        this.adlrecur_requireds = adlrecur_requireds;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<adlrecur_Provided> getAdlrecur_provideds() {
        return adlrecur_provideds;
    }

    public void addAdlrecur_provided(Adlrecur_provided adlrecur_provided) {
        this.adlrecur_provideds.add(adlrecur_provided);
    }
    public List<adlrecur_Required> getAdlrecur_requireds() {
        return adlrecur_requireds;
    }

    public void addAdlrecur_required(Adlrecur_required adlrecur_required) {
        this.adlrecur_requireds.add(adlrecur_required);
    }

}