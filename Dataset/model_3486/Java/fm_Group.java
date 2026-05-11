





import java.util.List;
import java.util.ArrayList;

public class fm_Group  {

    private String comment;
    private int upper;
    private boolean xor;
    private int lower;
    private String description;
    private boolean or_;



    public fm_Group(
        String comment,        int upper,        boolean xor,        int lower,        String description,        boolean or_    ) {
        this.comment = comment;
        this.upper = upper;
        this.xor = xor;
        this.lower = lower;
        this.description = description;
        this.or_ = or_;
    }


    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }
    public boolean getXor() {
        return xor;
    }

    public void setXor(boolean xor) {
        this.xor = xor;
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


}