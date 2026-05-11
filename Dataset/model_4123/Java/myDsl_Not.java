





import java.util.List;
import java.util.ArrayList;

public class myDsl_Not extends Condition {

    private String not_;





    private myDsl_Expression mydsl_expression;


    public myDsl_Not(
        String not_    ) {
        super(
        );
        this.not_ = not_;
    }


    public String getNot_() {
        return not_;
    }

    public void setNot_(String not_) {
        this.not_ = not_;
    }

    public myDsl_Expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_Expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }

}