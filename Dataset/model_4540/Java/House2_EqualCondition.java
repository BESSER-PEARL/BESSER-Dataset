





import java.util.List;
import java.util.ArrayList;

public class House2_EqualCondition extends Condition {

    private float valuecond;
    private boolean boolcond;



    public House2_EqualCondition(
        float valuecond,        boolean boolcond    ) {
        super(
        );
        this.valuecond = valuecond;
        this.boolcond = boolcond;
    }


    public float getValuecond() {
        return valuecond;
    }

    public void setValuecond(float valuecond) {
        this.valuecond = valuecond;
    }
    public boolean getBoolcond() {
        return boolcond;
    }

    public void setBoolcond(boolean boolcond) {
        this.boolcond = boolcond;
    }


}