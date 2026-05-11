





import java.util.List;
import java.util.ArrayList;

public class services_Service  {

    private String serviceSupport1;
    private String mostTopService;
    private String serviceCategory;
    private String serviceKind;
    private String serviceCharacterCommon;
    private String serviceClass;
    private String ssDomain;





    private services_Service services_service;




    private services_CIID services_ciid;




    private services_ServiceIncidentMgt services_serviceincidentmgt;


    public services_Service(
        String serviceSupport1,        String mostTopService,        String serviceCategory,        String serviceKind,        String serviceCharacterCommon,        String serviceClass,        String ssDomain    ) {
        this.serviceSupport1 = serviceSupport1;
        this.mostTopService = mostTopService;
        this.serviceCategory = serviceCategory;
        this.serviceKind = serviceKind;
        this.serviceCharacterCommon = serviceCharacterCommon;
        this.serviceClass = serviceClass;
        this.ssDomain = ssDomain;
    }


    public String getServicesupport1() {
        return serviceSupport1;
    }

    public void setServicesupport1(String serviceSupport1) {
        this.serviceSupport1 = serviceSupport1;
    }
    public String getMosttopservice() {
        return mostTopService;
    }

    public void setMosttopservice(String mostTopService) {
        this.mostTopService = mostTopService;
    }
    public String getServicecategory() {
        return serviceCategory;
    }

    public void setServicecategory(String serviceCategory) {
        this.serviceCategory = serviceCategory;
    }
    public String getServicekind() {
        return serviceKind;
    }

    public void setServicekind(String serviceKind) {
        this.serviceKind = serviceKind;
    }
    public String getServicecharactercommon() {
        return serviceCharacterCommon;
    }

    public void setServicecharactercommon(String serviceCharacterCommon) {
        this.serviceCharacterCommon = serviceCharacterCommon;
    }
    public String getServiceclass() {
        return serviceClass;
    }

    public void setServiceclass(String serviceClass) {
        this.serviceClass = serviceClass;
    }
    public String getSsdomain() {
        return ssDomain;
    }

    public void setSsdomain(String ssDomain) {
        this.ssDomain = ssDomain;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }
    public services_CIID getServices_ciid() {
        return services_ciid;
    }

    public void setServices_ciid(services_CIID services_ciid) {
        this.services_ciid = services_ciid;
    }
    public services_ServiceIncidentMgt getServices_serviceincidentmgt() {
        return services_serviceincidentmgt;
    }

    public void setServices_serviceincidentmgt(services_ServiceIncidentMgt services_serviceincidentmgt) {
        this.services_serviceincidentmgt = services_serviceincidentmgt;
    }

}