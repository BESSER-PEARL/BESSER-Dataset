





import java.util.List;
import java.util.ArrayList;

public class adl202_Provided extends Interface {






    private adl202_Component adl202_component;




    private List<adl202_Required> adl202_requireds;


    public adl202_Provided(
    ) {
        super(
        );
        this.adl202_requireds = new ArrayList<>();
    }

    public adl202_Provided(
        ArrayList<adl202_Required> adl202_requireds    ) {
        this.adl202_requireds = adl202_requireds;
    }


    public adl202_Component getAdl202_component() {
        return adl202_component;
    }

    public void setAdl202_component(adl202_Component adl202_component) {
        this.adl202_component = adl202_component;
    }
    public List<adl202_Required> getAdl202_requireds() {
        return adl202_requireds;
    }

    public void addAdl202_required(Adl202_required adl202_required) {
        this.adl202_requireds.add(adl202_required);
    }

}