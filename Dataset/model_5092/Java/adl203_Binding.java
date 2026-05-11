





import java.util.List;
import java.util.ArrayList;

public class adl203_Binding  {

    private String name;





    private adl203_Component adl203_component;




    private adl203_Required adl203_required;




    private adl203_Provided adl203_provided;




    private adl203_Provided adl203_provided;


    public adl203_Binding(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adl203_Component getAdl203_component() {
        return adl203_component;
    }

    public void setAdl203_component(adl203_Component adl203_component) {
        this.adl203_component = adl203_component;
    }
    public adl203_Required getAdl203_required() {
        return adl203_required;
    }

    public void setAdl203_required(adl203_Required adl203_required) {
        this.adl203_required = adl203_required;
    }
    public adl203_Provided getAdl203_provided() {
        return adl203_provided;
    }

    public void setAdl203_provided(adl203_Provided adl203_provided) {
        this.adl203_provided = adl203_provided;
    }
    public adl203_Provided getAdl203_provided() {
        return adl203_provided;
    }

    public void setAdl203_provided(adl203_Provided adl203_provided) {
        this.adl203_provided = adl203_provided;
    }

}