





import java.util.List;
import java.util.ArrayList;

public class services_ServiceDescription  {

    private String serviceDescriptionNational;
    private String serviceDescriptionCommon;





    private services_Service services_service;


    public services_ServiceDescription(
        String serviceDescriptionNational,        String serviceDescriptionCommon    ) {
        this.serviceDescriptionNational = serviceDescriptionNational;
        this.serviceDescriptionCommon = serviceDescriptionCommon;
    }


    public String getServicedescriptionnational() {
        return serviceDescriptionNational;
    }

    public void setServicedescriptionnational(String serviceDescriptionNational) {
        this.serviceDescriptionNational = serviceDescriptionNational;
    }
    public String getServicedescriptioncommon() {
        return serviceDescriptionCommon;
    }

    public void setServicedescriptioncommon(String serviceDescriptionCommon) {
        this.serviceDescriptionCommon = serviceDescriptionCommon;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}