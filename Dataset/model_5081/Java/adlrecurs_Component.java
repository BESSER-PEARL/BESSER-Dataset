





import java.util.List;
import java.util.ArrayList;

public class adlrecurs_Component extends AbstractComponent, NamedElement {






    private List<adlrecurs_Component> adlrecurs_components;


    public adlrecurs_Component(
    ) {
        super(
        );
        this.adlrecurs_components = new ArrayList<>();
    }

    public adlrecurs_Component(
        ArrayList<adlrecurs_Component> adlrecurs_components    ) {
        this.adlrecurs_components = adlrecurs_components;
    }


    public List<adlrecurs_Component> getAdlrecurs_components() {
        return adlrecurs_components;
    }

    public void addAdlrecurs_component(Adlrecurs_component adlrecurs_component) {
        this.adlrecurs_components.add(adlrecurs_component);
    }

}