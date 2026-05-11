





import java.util.List;
import java.util.ArrayList;

public class service_BusinessOperation extends NamedElement {

    private String resultMimeType;
    private String resultType;





    private List<service_Service> service_services;




    private service_Service service_service;


    public service_BusinessOperation(
        String resultMimeType,        String resultType    ) {
        super(
        );
        this.resultMimeType = resultMimeType;
        this.resultType = resultType;
        this.service_services = new ArrayList<>();
    }

    public service_BusinessOperation(
        String resultMimeType,        String resultType        ArrayList<service_Service> service_services    ) {
        this.resultMimeType = resultMimeType;
        this.resultType = resultType;
        this.service_services = service_services;
    }

    public String getResultmimetype() {
        return resultMimeType;
    }

    public void setResultmimetype(String resultMimeType) {
        this.resultMimeType = resultMimeType;
    }
    public String getResulttype() {
        return resultType;
    }

    public void setResulttype(String resultType) {
        this.resultType = resultType;
    }

    public List<service_Service> getService_services() {
        return service_services;
    }

    public void addService_service(Service_service service_service) {
        this.service_services.add(service_service);
    }
    public service_Service getService_service() {
        return service_service;
    }

    public void setService_service(service_Service service_service) {
        this.service_service = service_service;
    }

}