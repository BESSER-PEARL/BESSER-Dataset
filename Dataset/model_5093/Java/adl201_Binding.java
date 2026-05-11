





import java.util.List;
import java.util.ArrayList;

public class adl201_Binding  {

    private String name;





    private adl201_Required adl201_required;




    private adl201_Component adl201_component;




    private adl201_Provided adl201_provided;




    private adl201_Provided adl201_provided;




    private List<adl201_BindingAttributes> adl201_bindingattributess;


    public adl201_Binding(
        String name    ) {
        this.name = name;
        this.adl201_bindingattributess = new ArrayList<>();
    }

    public adl201_Binding(
        String name        ArrayList<adl201_BindingAttributes> adl201_bindingattributess    ) {
        this.name = name;
        this.adl201_bindingattributess = adl201_bindingattributess;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adl201_Required getAdl201_required() {
        return adl201_required;
    }

    public void setAdl201_required(adl201_Required adl201_required) {
        this.adl201_required = adl201_required;
    }
    public adl201_Component getAdl201_component() {
        return adl201_component;
    }

    public void setAdl201_component(adl201_Component adl201_component) {
        this.adl201_component = adl201_component;
    }
    public adl201_Provided getAdl201_provided() {
        return adl201_provided;
    }

    public void setAdl201_provided(adl201_Provided adl201_provided) {
        this.adl201_provided = adl201_provided;
    }
    public adl201_Provided getAdl201_provided() {
        return adl201_provided;
    }

    public void setAdl201_provided(adl201_Provided adl201_provided) {
        this.adl201_provided = adl201_provided;
    }
    public List<adl201_BindingAttributes> getAdl201_bindingattributess() {
        return adl201_bindingattributess;
    }

    public void addAdl201_bindingattributes(Adl201_bindingattributes adl201_bindingattributes) {
        this.adl201_bindingattributess.add(adl201_bindingattributes);
    }

}