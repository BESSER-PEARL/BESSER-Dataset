





import java.util.List;
import java.util.ArrayList;

public class ktest301_Component extends AbstractComponent, NamedElement {






    private List<ktest301_Component> ktest301_components;


    public ktest301_Component(
    ) {
        super(
        );
        this.ktest301_components = new ArrayList<>();
    }

    public ktest301_Component(
        ArrayList<ktest301_Component> ktest301_components    ) {
        this.ktest301_components = ktest301_components;
    }


    public List<ktest301_Component> getKtest301_components() {
        return ktest301_components;
    }

    public void addKtest301_component(Ktest301_component ktest301_component) {
        this.ktest301_components.add(ktest301_component);
    }

}