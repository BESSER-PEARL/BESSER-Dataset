





import java.util.List;
import java.util.ArrayList;

public class adl203_Provided extends Interface {






    private List<adl203_Required> adl203_requireds;




    private adl203_Component adl203_component;


    public adl203_Provided(
    ) {
        super(
        );
        this.adl203_requireds = new ArrayList<>();
    }

    public adl203_Provided(
        ArrayList<adl203_Required> adl203_requireds    ) {
        this.adl203_requireds = adl203_requireds;
    }


    public List<adl203_Required> getAdl203_requireds() {
        return adl203_requireds;
    }

    public void addAdl203_required(Adl203_required adl203_required) {
        this.adl203_requireds.add(adl203_required);
    }
    public adl203_Component getAdl203_component() {
        return adl203_component;
    }

    public void setAdl203_component(adl203_Component adl203_component) {
        this.adl203_component = adl203_component;
    }

}