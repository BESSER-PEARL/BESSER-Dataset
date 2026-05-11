





import java.util.List;
import java.util.ArrayList;

public class contentfwk_LogicalApplicationComponent extends ApplicationComponent, Element {






    private List<contentfwk_DataEntity> contentfwk_dataentitys;




    private List<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents;




    private contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent;




    private contentfwk_EObject contentfwk_eobject;




    private contentfwk_DataEntity contentfwk_dataentity;




    private contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture;


    public contentfwk_LogicalApplicationComponent(
    ) {
        super(
        );
        this.contentfwk_dataentitys = new ArrayList<>();
        this.contentfwk_logicalapplicationcomponents = new ArrayList<>();
    }

    public contentfwk_LogicalApplicationComponent(
        ArrayList<contentfwk_DataEntity> contentfwk_dataentitys,        ArrayList<contentfwk_LogicalApplicationComponent> contentfwk_logicalapplicationcomponents    ) {
        this.contentfwk_dataentitys = contentfwk_dataentitys;
        this.contentfwk_logicalapplicationcomponents = contentfwk_logicalapplicationcomponents;
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
    public contentfwk_LogicalApplicationComponent getContentfwk_logicalapplicationcomponent() {
        return contentfwk_logicalapplicationcomponent;
    }

    public void setContentfwk_logicalapplicationcomponent(contentfwk_LogicalApplicationComponent contentfwk_logicalapplicationcomponent) {
        this.contentfwk_logicalapplicationcomponent = contentfwk_logicalapplicationcomponent;
    }
    public contentfwk_EObject getContentfwk_eobject() {
        return contentfwk_eobject;
    }

    public void setContentfwk_eobject(contentfwk_EObject contentfwk_eobject) {
        this.contentfwk_eobject = contentfwk_eobject;
    }
    public contentfwk_DataEntity getContentfwk_dataentity() {
        return contentfwk_dataentity;
    }

    public void setContentfwk_dataentity(contentfwk_DataEntity contentfwk_dataentity) {
        this.contentfwk_dataentity = contentfwk_dataentity;
    }
    public contentfwk_ApplicationArchitecture getContentfwk_applicationarchitecture() {
        return contentfwk_applicationarchitecture;
    }

    public void setContentfwk_applicationarchitecture(contentfwk_ApplicationArchitecture contentfwk_applicationarchitecture) {
        this.contentfwk_applicationarchitecture = contentfwk_applicationarchitecture;
    }

}