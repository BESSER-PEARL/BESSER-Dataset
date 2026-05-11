





import java.util.List;
import java.util.ArrayList;

public class adl203_Component  {

    private String name;





    private List<adl203_Component> adl203_components;


    public adl203_Component(
        String name    ) {
        this.name = name;
        this.adl203_components = new ArrayList<>();
    }

    public adl203_Component(
        String name        ArrayList<adl203_Component> adl203_components    ) {
        this.name = name;
        this.adl203_components = adl203_components;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<adl203_Component> getAdl203_components() {
        return adl203_components;
    }

    public void addAdl203_component(Adl203_component adl203_component) {
        this.adl203_components.add(adl203_component);
    }

}