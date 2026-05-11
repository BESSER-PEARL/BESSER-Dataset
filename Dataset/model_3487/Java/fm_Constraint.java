





import java.util.List;
import java.util.ArrayList;

public class fm_Constraint  {

    private String comment;
    private String description;
    private String value;
    private String language;





    private fm_FeatureModel fm_featuremodel;




    private fm_FeatureModel fm_featuremodel;


    public fm_Constraint(
        String comment,        String description,        String value,        String language    ) {
        this.comment = comment;
        this.description = description;
        this.value = value;
        this.language = language;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public fm_FeatureModel getFm_featuremodel() {
        return fm_featuremodel;
    }

    public void setFm_featuremodel(fm_FeatureModel fm_featuremodel) {
        this.fm_featuremodel = fm_featuremodel;
    }
    public fm_FeatureModel getFm_featuremodel() {
        return fm_featuremodel;
    }

    public void setFm_featuremodel(fm_FeatureModel fm_featuremodel) {
        this.fm_featuremodel = fm_featuremodel;
    }

}