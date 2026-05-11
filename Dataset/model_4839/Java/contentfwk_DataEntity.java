





import java.util.List;
import java.util.ArrayList;

public class contentfwk_DataEntity extends Element {

    private String privacyClassification;
    private String retentionClassification;
    private String dataEntityCategory;





    private contentfwk_Service contentfwk_service;




    private contentfwk_DataEntity contentfwk_dataentity;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent;




    private contentfwk_DataEntity contentfwk_dataentity;




    private List<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents;




    private contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent;




    private contentfwk_Service contentfwk_service;




    private List<contentfwk_Service> contentfwk_services;




    private contentfwk_DataArchitecture contentfwk_dataarchitecture;




    private List<contentfwk_Service> contentfwk_services;




    private List<contentfwk_Actor> contentfwk_actors;


    public contentfwk_DataEntity(
        String privacyClassification,        String retentionClassification,        String dataEntityCategory    ) {
        super(
        );
        this.privacyClassification = privacyClassification;
        this.retentionClassification = retentionClassification;
        this.dataEntityCategory = dataEntityCategory;
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_logicalapplicationcomponents = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_services = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
    }

    public contentfwk_DataEntity(
        String privacyClassification,        String retentionClassification,        String dataEntityCategory        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents,        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Service> contentfwk_services,        ArrayList<contentfwk_Actor> contentfwk_actors    ) {
        this.privacyClassification = privacyClassification;
        this.retentionClassification = retentionClassification;
        this.dataEntityCategory = dataEntityCategory;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_logicalapplicationcomponents = contentfwk_logicalapplicationcomponents;
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_services = contentfwk_services;
        this.contentfwk_actors = contentfwk_actors;
    }

    public String getPrivacyclassification() {
        return privacyClassification;
    }

    public void setPrivacyclassification(String privacyClassification) {
        this.privacyClassification = privacyClassification;
    }
    public String getRetentionclassification() {
        return retentionClassification;
    }

    public void setRetentionclassification(String retentionClassification) {
        this.retentionClassification = retentionClassification;
    }
    public String getDataentitycategory() {
        return dataEntityCategory;
    }

    public void setDataentitycategory(String dataEntityCategory) {
        this.dataEntityCategory = dataEntityCategory;
    }

    public contentfwk_Service getContentfwk_service() {
        return contentfwk_service;
    }

    public void setContentfwk_service(contentfwk_Service contentfwk_service) {
        this.contentfwk_service = contentfwk_service;
    }
    public contentfwk_DataEntity getContentfwk_dataentity() {
        return contentfwk_dataentity;
    }

    public void setContentfwk_dataentity(contentfwk_DataEntity contentfwk_dataentity) {
        this.contentfwk_dataentity = contentfwk_dataentity;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public contentfwk_LogicalDataComponent getContentfwk_logicaldatacomponent() {
        return contentfwk_logicaldatacomponent;
    }

    public void setContentfwk_logicaldatacomponent(contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent) {
        this.contentfwk_logicaldatacomponent = contentfwk_logicaldatacomponent;
    }
    public contentfwk_DataEntity getContentfwk_dataentity() {
        return contentfwk_dataentity;
    }

    public void setContentfwk_dataentity(contentfwk_DataEntity contentfwk_dataentity) {
        this.contentfwk_dataentity = contentfwk_dataentity;
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
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public contentfwk_LogicalDataComponent getContentfwk_logicaldatacomponent() {
        return contentfwk_logicaldatacomponent;
    }

    public void setContentfwk_logicaldatacomponent(contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent) {
        this.contentfwk_logicaldatacomponent = contentfwk_logicaldatacomponent;
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
    public contentfwk_DataArchitecture getContentfwk_dataarchitecture() {
        return contentfwk_dataarchitecture;
    }

    public void setContentfwk_dataarchitecture(contentfwk_DataArchitecture contentfwk_dataarchitecture) {
        this.contentfwk_dataarchitecture = contentfwk_dataarchitecture;
    }
    public List<contentfwk_Service> getContentfwk_services() {
        return contentfwk_services;
    }

    public void addContentfwk_service(Contentfwk_service contentfwk_service) {
        this.contentfwk_services.add(contentfwk_service);
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }

}