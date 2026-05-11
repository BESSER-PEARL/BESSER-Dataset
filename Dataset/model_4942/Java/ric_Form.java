





import java.util.List;
import java.util.ArrayList;

public class ric_Form extends ClassifiableComponent, IdentifiableComponent, EventComponent {

    private String name;
    private String method;





    private ric_Div ric_div;


    public ric_Form(
        String name,        String method    ) {
        super(
        );
        this.name = name;
        this.method = method;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }

    public ric_Div getRic_div() {
        return ric_div;
    }

    public void setRic_div(ric_Div ric_div) {
        this.ric_div = ric_div;
    }

}