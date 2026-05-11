





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_Port extends wsdl_IPort, wsdl_ExtensibleElement {

    private String name;



    public model_wsdl_Port(
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