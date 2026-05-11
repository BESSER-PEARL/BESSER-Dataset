





import java.util.List;
import java.util.ArrayList;

public class services_ServiceProfile  {

    private String name;





    private services_RFSService services_rfsservice;


    public services_ServiceProfile(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public services_RFSService getServices_rfsservice() {
        return services_rfsservice;
    }

    public void setServices_rfsservice(services_RFSService services_rfsservice) {
        this.services_rfsservice = services_rfsservice;
    }

}