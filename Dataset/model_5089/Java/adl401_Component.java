





import java.util.List;
import java.util.ArrayList;

public class adl401_Component  {

    private String name;





    private adl401_Content adl401_content;




    private adl401_Content adl401_content;




    private List<adl401_Component> adl401_components;


    public adl401_Component(
        String name    ) {
        this.name = name;
        this.adl401_components = new ArrayList<>();
    }

    public adl401_Component(
        String name        ArrayList<adl401_Component> adl401_components    ) {
        this.name = name;
        this.adl401_components = adl401_components;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adl401_Content getAdl401_content() {
        return adl401_content;
    }

    public void setAdl401_content(adl401_Content adl401_content) {
        this.adl401_content = adl401_content;
    }
    public adl401_Content getAdl401_content() {
        return adl401_content;
    }

    public void setAdl401_content(adl401_Content adl401_content) {
        this.adl401_content = adl401_content;
    }
    public List<adl401_Component> getAdl401_components() {
        return adl401_components;
    }

    public void addAdl401_component(Adl401_component adl401_component) {
        this.adl401_components.add(adl401_component);
    }

}