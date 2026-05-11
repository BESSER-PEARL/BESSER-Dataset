





import java.util.List;
import java.util.ArrayList;

public class sADL_ElementInList extends Expression {

    private boolean before;
    private boolean after;





    private sADL_Expression sadl_expression;


    public sADL_ElementInList(
        boolean before,        boolean after    ) {
        super(
        );
        this.before = before;
        this.after = after;
    }


    public boolean getBefore() {
        return before;
    }

    public void setBefore(boolean before) {
        this.before = before;
    }
    public boolean getAfter() {
        return after;
    }

    public void setAfter(boolean after) {
        this.after = after;
    }

    public sADL_Expression getSadl_expression() {
        return sadl_expression;
    }

    public void setSadl_expression(sADL_Expression sadl_expression) {
        this.sadl_expression = sadl_expression;
    }

}