





import java.util.List;
import java.util.ArrayList;

public class ric_Form extends IdentifiableComponent, EventComponent, ClassifiableComponent {

    private String method;
    private String name;





    private ric_Div ric_div;




    private List<ric_Fieldset> ric_fieldsets;


    public ric_Form(
        String method,        String name    ) {
        super(
        );
        this.method = method;
        this.name = name;
        this.ric_fieldsets = new ArrayList<>();
    }

    public ric_Form(
        String method,        String name        ArrayList<ric_Fieldset> ric_fieldsets    ) {
        this.method = method;
        this.name = name;
        this.ric_fieldsets = ric_fieldsets;
    }

    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ric_Div getRic_div() {
        return ric_div;
    }

    public void setRic_div(ric_Div ric_div) {
        this.ric_div = ric_div;
    }
    public List<ric_Fieldset> getRic_fieldsets() {
        return ric_fieldsets;
    }

    public void addRic_fieldset(Ric_fieldset ric_fieldset) {
        this.ric_fieldsets.add(ric_fieldset);
    }

}