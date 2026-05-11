





import java.util.List;
import java.util.ArrayList;

public class contentfwk_LogicalApplicationComponent extends ApplicationComponent, Element {






    private contentfwk_DataEntity contentfwk_dataentity;




    private List<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents;




    private List<contentfwk_Service> contentfwk_services;




    private contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent;




    private contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent;




    private List<contentfwk_DataEntity> contentfwk_dataentitys;




    private List<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents;




    private contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture;




    private contentfwk_Service contentfwk_service;


    public contentfwk_LogicalApplicationComponent(
    ) {
        super(
        );
        this.contentfwk_physicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_dataentitys = new ArrayList<>();
        this.contentfwk_logicalapplicationcomponents = new ArrayList<>();
    }

    public contentfwk_LogicalApplicationComponent(
        ArrayList<contentfwk_PhysicalApplicationComponent> contentfwk_physicalapplicationcomponents,        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_DataEntity> contentfwk_dataentitys,        ArrayList<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents    ) {
        this.contentfwk_physicalapplicationcomponents = contentfwk_physicalapplicationcomponents;
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_dataentitys = contentfwk_dataentitys;
        this.contentfwk_logicalapplicationcomponents = contentfwk_logicalapplicationcomponents;
    }


    public contentfwk_DataEntity getContentfwk_dataentity() {
        return contentfwk_dataentity;
    }

    public void setContentfwk_dataentity(contentfwk_DataEntity contentfwk_dataentity) {
        this.contentfwk_dataentity = contentfwk_dataentity;
    }
    public List<contentfwk_PhysicalApplicationComponent> getContentfwk_physicalapplicationcomponents() {
        return contentfwk_physicalapplicationcomponents;
    }

    public void addContentfwk_physicalapplicationcomponent(Contentfwk_physicalapplicationcomponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponents.add(contentfwk_physicalapplicationcomponent);
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public contentfwk_PhysicalApplicationComponent getContentfwk_physicalapplicationcomponent() {
        return contentfwk_physicalapplicationcomponent;
    }

    public void setContentfwk_physicalapplicationcomponent(contentfwk_PhysicalApplicationComponent contentfwk_physicalapplicationcomponent) {
        this.contentfwk_physicalapplicationcomponent = contentfwk_physicalapplicationcomponent;
    }
    public contentfwk_LogicalApplicationComponent getContentfwk_logicalapplicationcomponent() {
        return contentfwk_logicalapplicationcomponent;
    }

    public void setContentfwk_logicalapplicationcomponent(contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponent = contentfwk_logicalapplicationcomponent;
    }
    public List<contentfwk_DataEntity> getContentfwk_dataentitys() {
        return contentfwk_dataentitys;
    }

    public void addContentfwk_dataentity(Contentfwk_dataentity contentfwk_dataentity) {
        this.contentfwk_dataentitys.add(contentfwk_dataentity);
    }
    public List<contentfwk_LogicalApplicationComponent> getContentfwk_logicalapplicationcomponents() {
        return contentfwk_logicalapplicationcomponents;
    }

    public void addContentfwk_logicalapplicationcomponent(Contentfwk_logicalapplicationcomponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponents.add(contentfwk_logicalapplicationcomponent);
    }
    public contentfwk_ApplicationArchitecture getContentfwk_applicationarchitecture() {
        return contentfwk_applicationarchitecture;
    }

    public void setContentfwk_applicationarchitecture(contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture) {
        this.contentfwk_applicationarchitecture = contentfwk_applicationarchitecture;
    }
    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }

}