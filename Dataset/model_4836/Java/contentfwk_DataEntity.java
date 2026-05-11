





import java.util.List;
import java.util.ArrayList;

public class contentfwk_DataEntity extends Element {

    private String dataEntityCategory;
    private String privacyClassification;
    private String retentionClassification;





    private contentfwk_DataEntity contentfwk_dataentity;




    private contentfwk_Actor contentfwk_actor;




    private contentfwk_DataArchitecture contentfwk_dataarchitecture;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_EObject contentfwk_eobject;




    private contentfwk_Actor contentfwk_actor;




    private List<contentfwk_Actor> contentfwk_actors;




    private contentfwk_DataEntity contentfwk_dataentity;


    public contentfwk_DataEntity(
        String dataEntityCategory,        String privacyClassification,        String retentionClassification    ) {
        super(
        );
        this.dataEntityCategory = dataEntityCategory;
        this.privacyClassification = privacyClassification;
        this.retentionClassification = retentionClassification;
        this.contentfwk_actors = new ArrayList<>();
        this.contentfwk_actors = new ArrayList<>();
    }

    public contentfwk_DataEntity(
        String dataEntityCategory,        String privacyClassification,        String retentionClassification        ArrayList<contentfwk_Actor> contentfwk_actors,        ArrayList<contentfwk_Actor> contentfwk_actors    ) {
        this.dataEntityCategory = dataEntityCategory;
        this.privacyClassification = privacyClassification;
        this.retentionClassification = retentionClassification;
        this.contentfwk_actors = contentfwk_actors;
        this.contentfwk_actors = contentfwk_actors;
    }

    public String getDataentitycategory() {
        return dataEntityCategory;
    }

    public void setDataentitycategory(String dataEntityCategory) {
        this.dataEntityCategory = dataEntityCategory;
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
    public contentfwk_DataArchitecture getContentfwk_dataarchitecture() {
        return contentfwk_dataarchitecture;
    }

    public void setContentfwk_dataarchitecture(contentfwk_DataArchitecture contentfwk_dataarchitecture) {
        this.contentfwk_dataarchitecture = contentfwk_dataarchitecture;
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
    public contentfwk_Actor getContentfwk_actor() {
        return contentfwk_actor;
    }

    public void setContentfwk_actor(contentfwk_Actor contentfwk_actor) {
        this.contentfwk_actor = contentfwk_actor;
    }
    public List<contentfwk_Actor> getContentfwk_actors() {
        return contentfwk_actors;
    }

    public void addContentfwk_actor(Contentfwk_actor contentfwk_actor) {
        this.contentfwk_actors.add(contentfwk_actor);
    }
    public contentfwk_DataEntity getContentfwk_dataentity() {
        return contentfwk_dataentity;
    }

    public void setContentfwk_dataentity(contentfwk_DataEntity contentfwk_dataentity) {
        this.contentfwk_dataentity = contentfwk_dataentity;
    }

}