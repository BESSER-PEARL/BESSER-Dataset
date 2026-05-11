





import java.util.List;
import java.util.ArrayList;

public class services_ServiceInterrest  {

    private String contactUnit;
    private String interrestKind;





    private services_Service services_service;


    public services_ServiceInterrest(
        String contactUnit,        String interrestKind    ) {
        this.contactUnit = contactUnit;
        this.interrestKind = interrestKind;
    }


    public String getContactunit() {
        return contactUnit;
    }

    public void setContactunit(String contactUnit) {
        this.contactUnit = contactUnit;
    }
    public String getInterrestkind() {
        return interrestKind;
    }

    public void setInterrestkind(String interrestKind) {
        this.interrestKind = interrestKind;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}