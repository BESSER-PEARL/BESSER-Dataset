





import java.util.List;
import java.util.ArrayList;

public class fm_Feature  {

    private String description;
    private boolean optional;
    private boolean mandatory;
    private String comment;
    private String id;
    private int upper;
    private boolean cloneable;
    private boolean root;
    private String name;
    private int lower;
    private boolean orphan;





    private fm_Feature fm_feature;




    private List<fm_Attribute> fm_attributes;




    private fm_FeatureModel fm_featuremodel;




    private fm_FeatureModel fm_featuremodel;




    private List<fm_Group> fm_groups;




    private fm_Group fm_group;




    private fm_Attribute fm_attribute;




    private fm_Group fm_group;




    private fm_Group fm_group;




    private fm_FeatureModel fm_featuremodel;




    private fm_Feature fm_feature;


    public fm_Feature(
        String description,        boolean optional,        boolean mandatory,        String comment,        String id,        int upper,        boolean cloneable,        boolean root,        String name,        int lower,        boolean orphan    ) {
        this.description = description;
        this.optional = optional;
        this.mandatory = mandatory;
        this.comment = comment;
        this.id = id;
        this.upper = upper;
        this.cloneable = cloneable;
        this.root = root;
        this.name = name;
        this.lower = lower;
        this.orphan = orphan;
        this.fm_attributes = new ArrayList<>();
        this.fm_groups = new ArrayList<>();
    }

    public fm_Feature(
        String description,        boolean optional,        boolean mandatory,        String comment,        String id,        int upper,        boolean cloneable,        boolean root,        String name,        int lower,        boolean orphan        ArrayList<fm_Attribute> fm_attributes,        ArrayList<fm_Group> fm_groups    ) {
        this.description = description;
        this.optional = optional;
        this.mandatory = mandatory;
        this.comment = comment;
        this.id = id;
        this.upper = upper;
        this.cloneable = cloneable;
        this.root = root;
        this.name = name;
        this.lower = lower;
        this.orphan = orphan;
        this.fm_attributes = fm_attributes;
        this.fm_groups = fm_groups;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public boolean getCloneable() {
        return cloneable;
    }

    public void setCloneable(boolean cloneable) {
        this.cloneable = cloneable;
    }
    public boolean getRoot() {
        return root;
    }

    public void setRoot(boolean root) {
        this.root = root;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public boolean getOrphan() {
        return orphan;
    }

    public void setOrphan(boolean orphan) {
        this.orphan = orphan;
    }

    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }
    public List<fm_Attribute> getFm_attributes() {
        return fm_attributes;
    }

    public void addFm_attribute(Fm_attribute fm_attribute) {
        this.fm_attributes.add(fm_attribute);
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
    public fm_Attribute getFm_attribute() {
        return fm_attribute;
    }

    public void setFm_attribute(fm_Attribute fm_attribute) {
        this.fm_attribute = fm_attribute;
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

}