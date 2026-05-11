





import java.util.List;
import java.util.ArrayList;

public class adl_Component extends AbstractComponent, NamedElement {






    private List<adl_Component> adl_components;


    public adl_Component(
    ) {
        super(
        );
        this.adl_components = new ArrayList<>();
    }

    public adl_Component(
        ArrayList<adl_Component> adl_components    ) {
        this.adl_components = adl_components;
    }


    public List<adl_Component> getAdl_components() {
        return adl_components;
    }

    public void addAdl_component(Adl_component adl_component) {
        this.adl_components.add(adl_component);
    }

}