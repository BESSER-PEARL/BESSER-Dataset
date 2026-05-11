





import java.util.List;
import java.util.ArrayList;

public class fm_Feature  {

    private int lower;
    private boolean orphan;
    private String id;
    private boolean cloneable;
    private int upper;
    private boolean mandatory;
    private String name;
    private boolean root;
    private String comment;
    private String description;
    private boolean optional;





    private fm_FeatureModel fm_featuremodel;




    private fm_Group fm_group;




    private fm_Group fm_group;




    private fm_Feature fm_feature;




    private fm_Feature fm_feature;




    private fm_Attribute fm_attribute;




    private fm_EObject fm_eobject;




    private List<fm_Group> fm_groups;




    private fm_Group fm_group;




    private List<fm_Attribute> fm_attributes;




    private fm_FeatureModel fm_featuremodel;




    private fm_FeatureModel fm_featuremodel;


    public fm_Feature(
        int lower,        boolean orphan,        String id,        boolean cloneable,        int upper,        boolean mandatory,        String name,        boolean root,        String comment,        String description,        boolean optional    ) {
        this.lower = lower;
        this.orphan = orphan;
        this.id = id;
        this.cloneable = cloneable;
        this.upper = upper;
        this.mandatory = mandatory;
        this.name = name;
        this.root = root;
        this.comment = comment;
        this.description = description;
        this.optional = optional;
        this.fm_groups = new ArrayList<>();
        this.fm_attributes = new ArrayList<>();
    }

    public fm_Feature(
        int lower,        boolean orphan,        String id,        boolean cloneable,        int upper,        boolean mandatory,        String name,        boolean root,        String comment,        String description,        boolean optional        ArrayList<fm_Group> fm_groups,        ArrayList<fm_Attribute> fm_attributes    ) {
        this.lower = lower;
        this.orphan = orphan;
        this.id = id;
        this.cloneable = cloneable;
        this.upper = upper;
        this.mandatory = mandatory;
        this.name = name;
        this.root = root;
        this.comment = comment;
        this.description = description;
        this.optional = optional;
        this.fm_groups = fm_groups;
        this.fm_attributes = fm_attributes;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getCloneable() {
        return cloneable;
    }

    public void setCloneable(boolean cloneable) {
        this.cloneable = cloneable;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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

    public fm_FeatureModel getFm_featuremodel() {
        return fm_featuremodel;
    }

    public void setFm_featuremodel(fm_FeatureModel fm_featuremodel) {
        this.fm_featuremodel = fm_featuremodel;
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
    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }
    public fm_Attribute getFm_attribute() {
        return fm_attribute;
    }

    public void setFm_attribute(fm_Attribute fm_attribute) {
        this.fm_attribute = fm_attribute;
    }
    public fm_EObject getFm_eobject() {
        return fm_eobject;
    }

    public void setFm_eobject(fm_EObject fm_eobject) {
        this.fm_eobject = fm_eobject;
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

}