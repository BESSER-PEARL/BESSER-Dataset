





import java.util.List;
import java.util.ArrayList;

public class contentfwk_DataEntity extends Element {

    private String retentionClassification;
    private String privacyClassification;
    private String dataEntityCategory;





    private contentfwk_DataArchitecture contentfwk_dataarchitecture;




    private contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent;




    private contentfwk_DataEntity contentfwk_dataentity;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_DataEntity contentfwk_dataentity;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_EObject contentfwk_eobject;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_LogicalDataComponent contentfwk_logicaldatacomponent;


    public contentfwk_DataEntity(
        String retentionClassification,        String privacyClassification,        String dataEntityCategory    ) {
        super(
        );
        this.retentionClassification = retentionClassification;
        this.privacyClassification = privacyClassification;
        this.dataEntityCategory = dataEntityCategory;
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
    }

    public contentfwk_DataEntity(
        String retentionClassification,        String privacyClassification,        String dataEntityCategory        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_Actor> contentfwk_actors    ) {
        this.retentionClassification = retentionClassification;
        this.privacyClassification = privacyClassification;
        this.dataEntityCategory = dataEntityCategory;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_actors = contentfwk_actors;
    }

    public String getRetentionclassification() {
        return retentionClassification;
    }

    public void setRetentionclassification(String retentionClassification) {
        this.retentionClassification = retentionClassification;
    }
    public String getPrivacyclassification() {
        return privacyClassification;
    }

    public void setPrivacyclassification(String privacyClassification) {
        this.privacyClassification = privacyClassification;
    }
    public String getDataentitycategory() {
        return dataEntityCategory;
    }

    public void setDataentitycategory(String dataEntityCategory) {
        this.dataEntityCategory = dataEntityCategory;
    }

    public contentfwk_DataArchitecture getContentfwk_dataarchitecture() {
        return contentfwk_dataarchitecture;
    }

    public void setContentfwk_dataarchitecture(contentfwk_DataArchitecture contentfwk_dataarchitecture) {
        this.contentfwk_dataarchitecture = contentfwk_dataarchitecture;
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
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
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
    public contentfwk_EObject getContentfwk_eobject() {
        return contentfwk_eobject;
    }

    public void setContentfwk_eobject(contentfwk_EObject contentfwk_eobject) {
        this.contentfwk_eobject = contentfwk_eobject;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
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

}