





import java.util.List;
import java.util.ArrayList;

public class contentfwk_LogicalTechnologyComponent extends Element, TechnologyComponent {






    private contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent;




    private contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture;




    private contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent;




    private List<contentfwk_Service> contentfwk_services;




    private contentfwk_PlatformService contentfwk_platformservice;




    private List<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents;




    private contentfwk_Service contentfwk_service;




    private List<contentfwk_PlatformService> contentfwk_platformservices;




    private contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent;


    public contentfwk_LogicalTechnologyComponent(
    ) {
        super(
        );
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_physicaltechnologycomponents = new ArrayList<>();
        this.contentfwk_platformservices = new ArrayList<>();
    }

    public contentfwk_LogicalTechnologyComponent(
        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_PhysicalTechnologyComponent> contentfwk_physicaltechnologycomponents,        ArrayList<contentfwk_PlatformService> contentfwk_platformservices    ) {
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_physicaltechnologycomponents = contentfwk_physicaltechnologycomponents;
        this.contentfwk_platformservices = contentfwk_platformservices;
    }


    public contentfwk_LogicalTechnologyComponent getContentfwk_logicaltechnologycomponent() {
        return contentfwk_logicaltechnologycomponent;
    }

    public void setContentfwk_logicaltechnologycomponent(contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent) {
        this.contentfwk_logicaltechnologycomponent = contentfwk_logicaltechnologycomponent;
    }
    public contentfwk_TechnologyArchitecture getContentfwk_technologyarchitecture() {
        return contentfwk_technologyarchitecture;
    }

    public void setContentfwk_technologyarchitecture(contentfwk_TechnologyArchitecture contentfwk_technologyarchitecture) {
        this.contentfwk_technologyarchitecture = contentfwk_technologyarchitecture;
    }
    public contentfwk_PhysicalTechnologyComponent getContentfwk_physicaltechnologycomponent() {
        return contentfwk_physicaltechnologycomponent;
    }

    public void setContentfwk_physicaltechnologycomponent(contentfwk_PhysicalTechnologyComponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponent = contentfwk_physicaltechnologycomponent;
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public contentfwk_PlatformService getContentfwk_platformservice() {
        return contentfwk_platformservice;
    }

    public void setContentfwk_platformservice(contentfwk_PlatformService contentfwk_platformservice) {
        this.contentfwk_platformservice = contentfwk_platformservice;
    }
    public List<contentfwk_PhysicalTechnologyComponent> getContentfwk_physicaltechnologycomponents() {
        return contentfwk_physicaltechnologycomponents;
    }

    public void addContentfwk_physicaltechnologycomponent(Contentfwk_physicaltechnologycomponent contentfwk_physicaltechnologycomponent) {
        this.contentfwk_physicaltechnologycomponents.add(contentfwk_physicaltechnologycomponent);
    }
    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public List<contentfwk_PlatformService> getContentfwk_platformservices() {
        return contentfwk_platformservices;
    }

    public void addContentfwk_platformservice(Contentfwk_platformservice contentfwk_platformservice) {
        this.contentfwk_platformservices.add(contentfwk_platformservice);
    }
    public contentfwk_LogicalTechnologyComponent getContentfwk_logicaltechnologycomponent() {
        return contentfwk_logicaltechnologycomponent;
    }

    public void setContentfwk_logicaltechnologycomponent(contentfwk_LogicalTechnologyComponent contentfwk_logicaltechnologycomponent) {
        this.contentfwk_logicaltechnologycomponent = contentfwk_logicaltechnologycomponent;
    }

}