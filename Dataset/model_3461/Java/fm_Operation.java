





import java.util.List;
import java.util.ArrayList;

public class fm_Operation  {

    private int value;





    private fm_Feature fm_feature;




    private fm_CardExConstraint fm_cardexconstraint;




    private fm_CardExConstraint fm_cardexconstraint;


    public fm_Operation(
        int value    ) {
        this.value = value;
    }


    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public fm_Feature getFm_feature() {
        return fm_feature;
    }

    public void setFm_feature(fm_Feature fm_feature) {
        this.fm_feature = fm_feature;
    }
    public fm_CardExConstraint getFm_cardexconstraint() {
        return fm_cardexconstraint;
    }

    public void setFm_cardexconstraint(fm_CardExConstraint fm_cardexconstraint) {
        this.fm_cardexconstraint = fm_cardexconstraint;
    }
    public fm_CardExConstraint getFm_cardexconstraint() {
        return fm_cardexconstraint;
    }

    public void setFm_cardexconstraint(fm_CardExConstraint fm_cardexconstraint) {
        this.fm_cardexconstraint = fm_cardexconstraint;
    }

}