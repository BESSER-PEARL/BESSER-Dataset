





import java.util.List;
import java.util.ArrayList;

public class services_services_Operation extends BaseElement {

    private String name;





    private services_services_EObject services_services_eobject;


    public services_services_Operation(
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

    public services_services_EObject getServices_services_eobject() {
        return services_services_eobject;
    }

    public void setServices_services_eobject(services_services_EObject services_services_eobject) {
        this.services_services_eobject = services_services_eobject;
    }

}