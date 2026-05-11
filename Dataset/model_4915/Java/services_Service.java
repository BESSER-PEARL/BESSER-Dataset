





import java.util.List;
import java.util.ArrayList;

public class services_Service  {

    private String ssDomain;
    private String serviceKind;
    private String serviceSupport1;
    private String serviceCharacterCommon;
    private String serviceCategory;
    private String mostTopService;
    private String serviceClass;





    private services_ServiceInterrest services_serviceinterrest;




    private services_ServiceIncidentMgt services_serviceincidentmgt;




    private services_ServiceSecurityMgt services_servicesecuritymgt;




    private List<services_ServiceContract> services_servicecontracts;




    private services_CIID services_ciid;




    private List<services_Service> services_services;


    public services_Service(
        String ssDomain,        String serviceKind,        String serviceSupport1,        String serviceCharacterCommon,        String serviceCategory,        String mostTopService,        String serviceClass    ) {
        this.ssDomain = ssDomain;
        this.serviceKind = serviceKind;
        this.serviceSupport1 = serviceSupport1;
        this.serviceCharacterCommon = serviceCharacterCommon;
        this.serviceCategory = serviceCategory;
        this.mostTopService = mostTopService;
        this.serviceClass = serviceClass;
        this.services_servicecontracts = new ArrayList<>();
        this.services_services = new ArrayList<>();
    }

    public services_Service(
        String ssDomain,        String serviceKind,        String serviceSupport1,        String serviceCharacterCommon,        String serviceCategory,        String mostTopService,        String serviceClass        ArrayList<services_ServiceContract> services_servicecontracts,        ArrayList<services_Service> services_services    ) {
        this.ssDomain = ssDomain;
        this.serviceKind = serviceKind;
        this.serviceSupport1 = serviceSupport1;
        this.serviceCharacterCommon = serviceCharacterCommon;
        this.serviceCategory = serviceCategory;
        this.mostTopService = mostTopService;
        this.serviceClass = serviceClass;
        this.services_servicecontracts = services_servicecontracts;
        this.services_services = services_services;
    }

    public String getSsdomain() {
        return ssDomain;
    }

    public void setSsdomain(String ssDomain) {
        this.ssDomain = ssDomain;
    }
    public String getServicekind() {
        return serviceKind;
    }

    public void setServicekind(String serviceKind) {
        this.serviceKind = serviceKind;
    }
    public String getServicesupport1() {
        return serviceSupport1;
    }

    public void setServicesupport1(String serviceSupport1) {
        this.serviceSupport1 = serviceSupport1;
    }
    public String getServicecharactercommon() {
        return serviceCharacterCommon;
    }

    public void setServicecharactercommon(String serviceCharacterCommon) {
        this.serviceCharacterCommon = serviceCharacterCommon;
    }
    public String getServicecategory() {
        return serviceCategory;
    }

    public void setServicecategory(String serviceCategory) {
        this.serviceCategory = serviceCategory;
    }
    public String getMosttopservice() {
        return mostTopService;
    }

    public void setMosttopservice(String mostTopService) {
        this.mostTopService = mostTopService;
    }
    public String getServiceclass() {
        return serviceClass;
    }

    public void setServiceclass(String serviceClass) {
        this.serviceClass = serviceClass;
    }

    public services_ServiceInterrest getServices_serviceinterrest() {
        return services_serviceinterrest;
    }

    public void setServices_serviceinterrest(services_ServiceInterrest services_serviceinterrest) {
        this.services_serviceinterrest = services_serviceinterrest;
    }
    public services_ServiceIncidentMgt getServices_serviceincidentmgt() {
        return services_serviceincidentmgt;
    }

    public void setServices_serviceincidentmgt(services_ServiceIncidentMgt services_serviceincidentmgt) {
        this.services_serviceincidentmgt = services_serviceincidentmgt;
    }
    public services_ServiceSecurityMgt getServices_servicesecuritymgt() {
        return services_servicesecuritymgt;
    }

    public void setServices_servicesecuritymgt(services_ServiceSecurityMgt services_servicesecuritymgt) {
        this.services_servicesecuritymgt = services_servicesecuritymgt;
    }
    public List<services_ServiceContract> getServices_servicecontracts() {
        return services_servicecontracts;
    }

    public void addServices_servicecontract(Services_servicecontract services_servicecontract) {
        this.services_servicecontracts.add(services_servicecontract);
    }
    public services_CIID getServices_ciid() {
        return services_ciid;
    }

    public void setServices_ciid(services_CIID services_ciid) {
        this.services_ciid = services_ciid;
    }
    public List<services_Service> getServices_services() {
        return services_services;
    }

    public void addServices_service(Services_service services_service) {
        this.services_services.add(services_service);
    }

}