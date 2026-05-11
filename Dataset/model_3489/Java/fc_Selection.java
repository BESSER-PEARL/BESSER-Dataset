





import java.util.List;
import java.util.ArrayList;

public class fc_Selection  {

    private String name;
    private String description;
    private boolean root;
    private String id;
    private String comment;
    private boolean enabled;
    private boolean present;





    private fc_Selection fc_selection;




    private fc_FeatureConfiguration fc_featureconfiguration;




    private fc_Selection fc_selection;




    private fc_FeatureConfiguration fc_featureconfiguration;


    public fc_Selection(
        String name,        String description,        boolean root,        String id,        String comment,        boolean enabled,        boolean present    ) {
        this.name = name;
        this.description = description;
        this.root = root;
        this.id = id;
        this.comment = comment;
        this.enabled = enabled;
        this.present = present;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getRoot() {
        return root;
    }

    public void setRoot(boolean root) {
        this.root = root;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public boolean getPresent() {
        return present;
    }

    public void setPresent(boolean present) {
        this.present = present;
    }

    public fc_Selection getFc_selection() {
        return fc_selection;
    }

    public void setFc_selection(fc_Selection fc_selection) {
        this.fc_selection = fc_selection;
    }
    public fc_FeatureConfiguration getFc_featureconfiguration() {
        return fc_featureconfiguration;
    }

    public void setFc_featureconfiguration(fc_FeatureConfiguration fc_featureconfiguration) {
        this.fc_featureconfiguration = fc_featureconfiguration;
    }
    public fc_Selection getFc_selection() {
        return fc_selection;
    }

    public void setFc_selection(fc_Selection fc_selection) {
        this.fc_selection = fc_selection;
    }
    public fc_FeatureConfiguration getFc_featureconfiguration() {
        return fc_featureconfiguration;
    }

    public void setFc_featureconfiguration(fc_FeatureConfiguration fc_featureconfiguration) {
        this.fc_featureconfiguration = fc_featureconfiguration;
    }

}