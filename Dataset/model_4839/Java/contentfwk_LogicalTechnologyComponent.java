





import java.util.List;
import java.util.ArrayList;

public class contentfwk_LogicalTechnologyComponent extends Element, TechnologyComponent {

    private String categoryTRM;





    private List<contentfwk_LogicalTechnologyComponent> contentfwk_logicaltechnologycomponents;




    private List<contentfwk_PlatformService> contentfwk_platformservices;




    private contentfwk_PlatformService contentfwk_platformservice;




    private contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent;




    private contentfwk_Service contentfwk_service;




    private List<contentfwk_Service> contentfwk_services;


    public contentfwk_LogicalTechnologyComponent(
        String categoryTRM    ) {
        super(
        );
        this.categoryTRM = categoryTRM;
        this.contentfwk_logicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_platformservices = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
    }

    public contentfwk_LogicalTechnologyComponent(
        String categoryTRM        ArrayList<contentfwk_LogicalTechnologyComponent> contentfwk_logicaltechnologycomponents,        ArrayList<contentfwk_PlatformService> contentfwk_platformservices,        ArrayList<contentfwk_Service> contentfwk_services    ) {
        this.categoryTRM = categoryTRM;
        this.contentfwk_logicaltechnologycomponents = contentfwk_logicaltechnologycomponents;
        this.contentfwk_platformservices = contentfwk_platformservices;
        this.contentfwk_services = contentfwk_services;
    }

    public String getCategorytrm() {
        return categoryTRM;
    }

    public void setCategorytrm(String categoryTRM) {
        this.categoryTRM = categoryTRM;
    }

    public List<contentfwk_LogicalTechnologyComponent> getContentfwk_logicaltechnologycomponents() {
        return contentfwk_logicaltechnologycomponents;
    }

    public void addContentfwk_logicaltechnologycomponent(Contentfwk_logicaltechnologycomponent contentfwk_logicaltechnologycomponent) {
        this.contentfwk_logicaltechnologycomponents.add(contentfwk_logicaltechnologycomponent);
    }
    public List<contentfwk_PlatformService> getContentfwk_platformservices() {
        return contentfwk_platformservices;
    }

    public void addContentfwk_platformservice(Contentfwk_platformservice contentfwk_platformservice) {
        this.contentfwk_platformservices.add(contentfwk_platformservice);
    }
    public contentfwk_PlatformService getContentfwk_platformservice() {
        return contentfwk_platformservice;
    }

    public void setContentfwk_platformservice(contentfwk_PlatformService contentfwk_platformservice) {
        this.contentfwk_platformservice = contentfwk_platformservice;
    }
    public contentfwk_LogicalTechnologyComponent getContentfwk_logicaltechnologycomponent() {
        return contentfwk_logicaltechnologycomponent;
    }

    public void setContentfwk_logicaltechnologycomponent(contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent) {
        this.contentfwk_logicaltechnologycomponent = contentfwk_logicaltechnologycomponent;
    }
    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }

}