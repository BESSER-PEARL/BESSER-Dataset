





import java.util.List;
import java.util.ArrayList;

public class cjsidl_guard  {

    private String equiv;
    private String comment;
    private String logicalOperator;





    private cjsidl_transition cjsidl_transition;


    public cjsidl_guard(
        String equiv,        String comment,        String logicalOperator    ) {
        this.equiv = equiv;
        this.comment = comment;
        this.logicalOperator = logicalOperator;
    }


    public String getEquiv() {
        return equiv;
    }

    public void setEquiv(String equiv) {
        this.equiv = equiv;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getLogicaloperator() {
        return logicalOperator;
    }

    public void setLogicaloperator(String logicalOperator) {
        this.logicalOperator = logicalOperator;
    }

    public cjsidl_transition getCjsidl_transition() {
        return cjsidl_transition;
    }

    public void setCjsidl_transition(cjsidl_transition cjsidl_transition) {
        this.cjsidl_transition = cjsidl_transition;
    }

}