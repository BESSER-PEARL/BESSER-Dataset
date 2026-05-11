





import java.util.List;
import java.util.ArrayList;

public class adl201_Provided extends Interface {






    private adl201_Component adl201_component;




    private List<adl201_Required> adl201_requireds;


    public adl201_Provided(
    ) {
        super(
        );
        this.adl201_requireds = new ArrayList<>();
    }

    public adl201_Provided(
        ArrayList<adl201_Required> adl201_requireds    ) {
        this.adl201_requireds = adl201_requireds;
    }


    public adl201_Component getAdl201_component() {
        return adl201_component;
    }

    public void setAdl201_component(adl201_Component adl201_component) {
        this.adl201_component = adl201_component;
    }
    public List<adl201_Required> getAdl201_requireds() {
        return adl201_requireds;
    }

    public void addAdl201_required(Adl201_required adl201_required) {
        this.adl201_requireds.add(adl201_required);
    }

}