





import java.util.List;
import java.util.ArrayList;

public class adl203_BindingAttributes  {

    private String name;
    private String value;





    private adl203_Binding adl203_binding;


    public adl203_BindingAttributes(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public adl203_Binding getAdl203_binding() {
        return adl203_binding;
    }

    public void setAdl203_binding(adl203_Binding adl203_binding) {
        this.adl203_binding = adl203_binding;
    }

}