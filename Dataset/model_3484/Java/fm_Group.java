





import java.util.List;
import java.util.ArrayList;

public class fm_Group  {

    private int lower;
    private String description;
    private boolean or_;
    private String comment;
    private boolean xor;
    private int upper;





    private List<fm_Feature> fm_features;




    private fm_Feature fm_feature;




    private fm_Feature fm_feature;




    private fm_Feature fm_feature;


    public fm_Group(
        int lower,        String description,        boolean or_,        String comment,        boolean xor,        int upper    ) {
        this.lower = lower;
        this.description = description;
        this.or_ = or_;
        this.comment = comment;
        this.xor = xor;
        this.upper = upper;
        this.fm_features = new ArrayList<>();
    }

    public fm_Group(
        int lower,        String description,        boolean or_,        String comment,        boolean xor,        int upper        ArrayList<fm_Feature> fm_features    ) {
        this.lower = lower;
        this.description = description;
        this.or_ = or_;
        this.comment = comment;
        this.xor = xor;
        this.upper = upper;
        this.fm_features = fm_features;
    }

    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getOr_() {
        return or_;
    }

    public void setOr_(boolean or_) {
        this.or_ = or_;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public boolean getXor() {
        return xor;
    }

    public void setXor(boolean xor) {
        this.xor = xor;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
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

}