





import java.util.List;
import java.util.ArrayList;

public class DOT_DirectedArc extends Arc {

    private float head_lp;
    private float tail_lp;





    private DOT_Label dot_label;




    private DOT_Label dot_label;


    public DOT_DirectedArc(
        float head_lp,        float tail_lp    ) {
        super(
        );
        this.head_lp = head_lp;
        this.tail_lp = tail_lp;
    }


    public float getHead_lp() {
        return head_lp;
    }

    public void setHead_lp(float head_lp) {
        this.head_lp = head_lp;
    }
    public float getTail_lp() {
        return tail_lp;
    }

    public void setTail_lp(float tail_lp) {
        this.tail_lp = tail_lp;
    }

    public DOT_Label getDot_label() {
        return dot_label;
    }

    public void setDot_label(DOT_Label dot_label) {
        this.dot_label = dot_label;
    }
    public DOT_Label getDot_label() {
        return dot_label;
    }

    public void setDot_label(DOT_Label dot_label) {
        this.dot_label = dot_label;
    }

}