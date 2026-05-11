





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Service extends Standard {






    private contentfwk_Service contentfwk_service;




    private List<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents;




    private contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent;




    private List<contentfwk_Service> contentfwk_services;


    public contentfwk_Service(
    ) {
        super(
        );
        this.contentfwk_logicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
    }

    public contentfwk_Service(
        ArrayList<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents,        ArrayList<contentfwk_Service> contentfwk_services    ) {
        this.contentfwk_logicalapplicationcomponents = contentfwk_logicalapplicationcomponents;
        this.contentfwk_services = contentfwk_services;
    }


    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public List<contentfwk_LogicalApplicationComponent> getContentfwk_logicalapplicationcomponents() {
        return contentfwk_logicalapplicationcomponents;
    }

    public void addContentfwk_logicalapplicationcomponent(Contentfwk_logicalapplicationcomponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponents.add(contentfwk_logicalapplicationcomponent);
    }
    public contentfwk_LogicalApplicationComponent getContentfwk_logicalapplicationcomponent() {
        return contentfwk_logicalapplicationcomponent;
    }

    public void setContentfwk_logicalapplicationcomponent(contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponent = contentfwk_logicalapplicationcomponent;
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }

}