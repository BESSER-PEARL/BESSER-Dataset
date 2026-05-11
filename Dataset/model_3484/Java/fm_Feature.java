





import java.util.List;
import java.util.ArrayList;

public class fm_Feature  {

    private int lower;
    private boolean mandatory;
    private String description;
    private String name;
    private boolean root;
    private String id;
    private int upper;
    private boolean optional;
    private boolean orphan;
    private boolean cloneable;
    private String comment;





    private List<fm_Feature> fm_features;




    private fm_Feature fm_feature;


    public fm_Feature(
        int lower,        boolean mandatory,        String description,        String name,        boolean root,        String id,        int upper,        boolean optional,        boolean orphan,        boolean cloneable,        String comment    ) {
        this.lower = lower;
        this.mandatory = mandatory;
        this.description = description;
        this.name = name;
        this.root = root;
        this.id = id;
        this.upper = upper;
        this.optional = optional;
        this.orphan = orphan;
        this.cloneable = cloneable;
        this.comment = comment;
        this.fm_features = new ArrayList<>();
    }

    public fm_Feature(
        int lower,        boolean mandatory,        String description,        String name,        boolean root,        String id,        int upper,        boolean optional,        boolean orphan,        boolean cloneable,        String comment        ArrayList<fm_Feature> fm_features    ) {
        this.lower = lower;
        this.mandatory = mandatory;
        this.description = description;
        this.name = name;
        this.root = root;
        this.id = id;
        this.upper = upper;
        this.optional = optional;
        this.orphan = orphan;
        this.cloneable = cloneable;
        this.comment = comment;
        this.fm_features = fm_features;
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
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public boolean getOptional() {
        return optional;
    }

    public void setOptional(boolean optional) {
        this.optional = optional;
    }
    public boolean getOrphan() {
        return orphan;
    }

    public void setOrphan(boolean orphan) {
        this.orphan = orphan;
    }
    public boolean getCloneable() {
        return cloneable;
    }

    public void setCloneable(boolean cloneable) {
        this.cloneable = cloneable;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }

    public List<fm_Feature> getFm_features() {
        return fm_features;
    }

    public void addFm_feature(Fm_feature fm_feature) {
        this.fm_features.add(fm_feature);
    }
    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }

}