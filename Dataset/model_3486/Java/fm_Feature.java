





import java.util.List;
import java.util.ArrayList;

public class fm_Feature  {

    private boolean optional;
    private String name;
    private boolean cloneable;
    private String description;
    private int lower;
    private boolean mandatory;
    private int upper;
    private String id;
    private boolean root;
    private String comment;
    private boolean orphan;





    private fm_Group fm_group;




    private fm_FeatureModel fm_featuremodel;




    private fm_Feature fm_feature;




    private fm_FeatureModel fm_featuremodel;




    private fm_FeatureModel fm_featuremodel;




    private List<fm_Group> fm_groups;




    private fm_Group fm_group;




    private fm_Group fm_group;




    private fm_Feature fm_feature;


    public fm_Feature(
        boolean optional,        String name,        boolean cloneable,        String description,        int lower,        boolean mandatory,        int upper,        String id,        boolean root,        String comment,        boolean orphan    ) {
        this.optional = optional;
        this.name = name;
        this.cloneable = cloneable;
        this.description = description;
        this.lower = lower;
        this.mandatory = mandatory;
        this.upper = upper;
        this.id = id;
        this.root = root;
        this.comment = comment;
        this.orphan = orphan;
        this.fm_groups = new ArrayList<>();
    }

    public fm_Feature(
        boolean optional,        String name,        boolean cloneable,        String description,        int lower,        boolean mandatory,        int upper,        String id,        boolean root,        String comment,        boolean orphan        ArrayList<fm_Group> fm_groups    ) {
        this.optional = optional;
        this.name = name;
        this.cloneable = cloneable;
        this.description = description;
        this.lower = lower;
        this.mandatory = mandatory;
        this.upper = upper;
        this.id = id;
        this.root = root;
        this.comment = comment;
        this.orphan = orphan;
        this.fm_groups = fm_groups;
    }

    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getCloneable() {
        return cloneable;
    }

    public void setCloneable(boolean cloneable) {
        this.cloneable = cloneable;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getRoot() {
        return root;
    }

    public void setRoot(boolean root) {
        this.root = root;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public boolean getOrphan() {
        return orphan;
    }

    public void setOrphan(boolean orphan) {
        this.orphan = orphan;
    }

    public fm_Group getFm_group() {
        return fm_group;
    }

    public void setFm_group(fm_Group fm_group) {
        this.fm_group = fm_group;
    }
    public fm_FeatureModel getFm_featuremodel() {
        return fm_featuremodel;
    }

    public void setFm_featuremodel(fm_FeatureModel fm_featuremodel) {
        this.fm_featuremodel = fm_featuremodel;
    }
    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
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
    public List<fm_Group> getFm_groups() {
        return fm_groups;
    }

    public void addFm_group(Fm_group fm_group) {
        this.fm_groups.add(fm_group);
    }
    public fm_Group getFm_group() {
        return fm_group;
    }

    public void setFm_group(fm_Group fm_group) {
        this.fm_group = fm_group;
    }
    public fm_Group getFm_group() {
        return fm_group;
    }

    public void setFm_group(fm_Group fm_group) {
        this.fm_group = fm_group;
    }
    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }

}