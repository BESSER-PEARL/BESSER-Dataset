





import java.util.List;
import java.util.ArrayList;

public class adlsimple_Component  {

    private String name;





    private List<adlsimple_Provided> adlsimple_provideds;




    private List<adlsimple_Required> adlsimple_requireds;


    public adlsimple_Component(
        String name    ) {
        this.name = name;
        this.adlsimple_provideds = new ArrayList<>();
        this.adlsimple_requireds = new ArrayList<>();
    }

    public adlsimple_Component(
        String name        ArrayList<adlsimple_Provided> adlsimple_provideds,        ArrayList<adlsimple_Required> adlsimple_requireds    ) {
        this.name = name;
        this.adlsimple_provideds = adlsimple_provideds;
        this.adlsimple_requireds = adlsimple_requireds;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<adlsimple_Provided> getAdlsimple_provideds() {
        return adlsimple_provideds;
    }

    public void addAdlsimple_provided(Adlsimple_provided adlsimple_provided) {
        this.adlsimple_provideds.add(adlsimple_provided);
    }
    public List<adlsimple_Required> getAdlsimple_requireds() {
        return adlsimple_requireds;
    }

    public void addAdlsimple_required(Adlsimple_required adlsimple_required) {
        this.adlsimple_requireds.add(adlsimple_required);
    }

}