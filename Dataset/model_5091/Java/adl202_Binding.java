





import java.util.List;
import java.util.ArrayList;

public class adl202_Binding  {

    private String name;





    private adl202_Component adl202_component;




    private adl202_Required adl202_required;




    private adl202_Provided adl202_provided;




    private adl202_Provided adl202_provided;




    private List<adl202_BindingAttributes> adl202_bindingattributess;


    public adl202_Binding(
        String name    ) {
        this.name = name;
        this.adl202_bindingattributess = new ArrayList<>();
    }

    public adl202_Binding(
        String name        ArrayList<adl202_BindingAttributes> adl202_bindingattributess    ) {
        this.name = name;
        this.adl202_bindingattributess = adl202_bindingattributess;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adl202_Component getAdl202_component() {
        return adl202_component;
    }

    public void setAdl202_component(adl202_Component adl202_component) {
        this.adl202_component = adl202_component;
    }
    public adl202_Required getAdl202_required() {
        return adl202_required;
    }

    public void setAdl202_required(adl202_Required adl202_required) {
        this.adl202_required = adl202_required;
    }
    public adl202_Provided getAdl202_provided() {
        return adl202_provided;
    }

    public void setAdl202_provided(adl202_Provided adl202_provided) {
        this.adl202_provided = adl202_provided;
    }
    public adl202_Provided getAdl202_provided() {
        return adl202_provided;
    }

    public void setAdl202_provided(adl202_Provided adl202_provided) {
        this.adl202_provided = adl202_provided;
    }
    public List<adl202_BindingAttributes> getAdl202_bindingattributess() {
        return adl202_bindingattributess;
    }

    public void addAdl202_bindingattributes(Adl202_bindingattributes adl202_bindingattributes) {
        this.adl202_bindingattributess.add(adl202_bindingattributes);
    }

}