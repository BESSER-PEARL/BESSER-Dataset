





import java.util.List;
import java.util.ArrayList;

public class website_BusinessOperation extends NamedElement {

    private String resultType;
    private String resultMimeType;





    private List<website_Service> website_services;




    private website_Service website_service;


    public website_BusinessOperation(
        String resultType,        String resultMimeType    ) {
        super(
        );
        this.resultType = resultType;
        this.resultMimeType = resultMimeType;
        this.website_services = new ArrayList<>();
    }

    public website_BusinessOperation(
        String resultType,        String resultMimeType        ArrayList<website_Service> website_services    ) {
        this.resultType = resultType;
        this.resultMimeType = resultMimeType;
        this.website_services = website_services;
    }

    public String getResulttype() {
        return resultType;
    }

    public void setResulttype(String resultType) {
        this.resultType = resultType;
    }
    public String getResultmimetype() {
        return resultMimeType;
    }

    public void setResultmimetype(String resultMimeType) {
        this.resultMimeType = resultMimeType;
    }

    public List<website_Service> getWebsite_services() {
        return website_services;
    }

    public void addWebsite_service(Website_service website_service) {
        this.website_services.add(website_service);
    }
    public website_Service getWebsite_service() {
        return website_service;
    }

    public void setWebsite_service(website_Service website_service) {
        this.website_service = website_service;
    }

}