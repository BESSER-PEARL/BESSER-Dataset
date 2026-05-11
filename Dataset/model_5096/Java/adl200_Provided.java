





import java.util.List;
import java.util.ArrayList;

public class adl200_Provided extends Interface {






    private List<adl200_Required> adl200_requireds;




    private adl200_Component adl200_component;


    public adl200_Provided(
    ) {
        super(
        );
        this.adl200_requireds = new ArrayList<>();
    }

    public adl200_Provided(
        ArrayList<adl200_Required> adl200_requireds    ) {
        this.adl200_requireds = adl200_requireds;
    }


    public List<adl200_Required> getAdl200_requireds() {
        return adl200_requireds;
    }

    public void addAdl200_required(Adl200_required adl200_required) {
        this.adl200_requireds.add(adl200_required);
    }
    public adl200_Component getAdl200_component() {
        return adl200_component;
    }

    public void setAdl200_component(adl200_Component adl200_component) {
        this.adl200_component = adl200_component;
    }

}