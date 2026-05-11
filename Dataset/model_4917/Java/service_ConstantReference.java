





import java.util.List;
import java.util.ArrayList;

public class service_ConstantReference extends Variable {

    private String name;





    private service_Constant service_constant;


    public service_ConstantReference(
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

    public service_Constant getService_constant() {
        return service_constant;
    }

    public void setService_constant(service_Constant service_constant) {
        this.service_constant = service_constant;
    }

}