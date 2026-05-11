





import java.util.List;
import java.util.ArrayList;

public class services_CIID extends Base {

    private String localCIID;
    private String commonCIID;





    private services_Service services_service;


    public services_CIID(
        String localCIID,        String commonCIID    ) {
        super(
        );
        this.localCIID = localCIID;
        this.commonCIID = commonCIID;
    }


    public String getLocalciid() {
        return localCIID;
    }

    public void setLocalciid(String localCIID) {
        this.localCIID = localCIID;
    }
    public String getCommonciid() {
        return commonCIID;
    }

    public void setCommonciid(String commonCIID) {
        this.commonCIID = commonCIID;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}