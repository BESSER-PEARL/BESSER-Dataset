





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_BindingInput extends wsdl_IBindingInput, wsdl_ExtensibleElement {

    private String name;



    public model_wsdl_BindingInput(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}