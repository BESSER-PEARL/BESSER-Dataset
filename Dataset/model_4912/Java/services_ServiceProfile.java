





import java.util.List;
import java.util.ArrayList;

public class services_ServiceProfile extends Base {

    private String name;





    private services_ServiceUser services_serviceuser;


    public services_ServiceProfile(
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

    public services_ServiceUser getServices_serviceuser() {
        return services_serviceuser;
    }

    public void setServices_serviceuser(services_ServiceUser services_serviceuser) {
        this.services_serviceuser = services_serviceuser;
    }

}