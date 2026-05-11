





import java.util.List;
import java.util.ArrayList;

public class adlold_Component extends AbstractComponent {






    private List<adlold_Component> adlold_components;


    public adlold_Component(
    ) {
        super(
        );
        this.adlold_components = new ArrayList<>();
    }

    public adlold_Component(
        ArrayList<adlold_Component> adlold_components    ) {
        this.adlold_components = adlold_components;
    }


    public List<adlold_Component> getAdlold_components() {
        return adlold_components;
    }

    public void addAdlold_component(Adlold_component adlold_component) {
        this.adlold_components.add(adlold_component);
    }

}