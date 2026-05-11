





import java.util.List;
import java.util.ArrayList;

public class adl199_Component extends AbstractComponent {






    private List<adl199_AbstractComponent> adl199_abstractcomponents;


    public adl199_Component(
    ) {
        super(
        );
        this.adl199_abstractcomponents = new ArrayList<>();
    }

    public adl199_Component(
        ArrayList<adl199_AbstractComponent> adl199_abstractcomponents    ) {
        this.adl199_abstractcomponents = adl199_abstractcomponents;
    }


    public List<adl199_AbstractComponent> getAdl199_abstractcomponents() {
        return adl199_abstractcomponents;
    }

    public void addAdl199_abstractcomponent(Adl199_abstractcomponent adl199_abstractcomponent) {
        this.adl199_abstractcomponents.add(adl199_abstractcomponent);
    }

}