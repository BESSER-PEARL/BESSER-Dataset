





import java.util.List;
import java.util.ArrayList;

public class coCoMM_Config  {

    private String type;
    private boolean selected;





    private List<coCoMM_Feature> cocomm_features;




    private coCoMM_Project cocomm_project;




    private coCoMM_Stakeholder cocomm_stakeholder;


    public coCoMM_Config(
        String type,        boolean selected    ) {
        this.type = type;
        this.selected = selected;
        this.cocomm_features = new ArrayList<>();
    }

    public coCoMM_Config(
        String type,        boolean selected        ArrayList<coCoMM_Feature> cocomm_features    ) {
        this.type = type;
        this.selected = selected;
        this.cocomm_features = cocomm_features;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getSelected() {
        return selected;
    }

    public void setSelected(boolean selected) {
        this.selected = selected;
    }

    public List<coCoMM_Feature> getCocomm_features() {
        return cocomm_features;
    }

    public void addCocomm_feature(Cocomm_feature cocomm_feature) {
        this.cocomm_features.add(cocomm_feature);
    }
    public coCoMM_Project getCocomm_project() {
        return cocomm_project;
    }

    public void setCocomm_project(coCoMM_Project cocomm_project) {
        this.cocomm_project = cocomm_project;
    }
    public coCoMM_Stakeholder getCocomm_stakeholder() {
        return cocomm_stakeholder;
    }

    public void setCocomm_stakeholder(coCoMM_Stakeholder cocomm_stakeholder) {
        this.cocomm_stakeholder = cocomm_stakeholder;
    }

}