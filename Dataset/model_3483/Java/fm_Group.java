





import java.util.List;
import java.util.ArrayList;

public class fm_Group  {

    private int lower;
    private boolean or_;
    private boolean xor;
    private String description;
    private String comment;
    private int upper;



    public fm_Group(
        int lower,        boolean or_,        boolean xor,        String description,        String comment,        int upper    ) {
        this.lower = lower;
        this.or_ = or_;
        this.xor = xor;
        this.description = description;
        this.comment = comment;
        this.upper = upper;
    }


    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }
    public boolean getOr_() {
        return or_;
    }

    public void setOr_(boolean or_) {
        this.or_ = or_;
    }
    public boolean getXor() {
        return xor;
    }

    public void setXor(boolean xor) {
        this.xor = xor;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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


}