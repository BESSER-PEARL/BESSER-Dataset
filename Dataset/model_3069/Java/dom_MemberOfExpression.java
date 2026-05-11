





import java.util.List;
import java.util.ArrayList;

public class dom_MemberOfExpression extends Expression {

    private boolean not_;
    private String memberOf;
    private String operator;





    private dom_Expression dom_expression;


    public dom_MemberOfExpression(
        boolean not_,        String memberOf,        String operator    ) {
        super(
        );
        this.not_ = not_;
        this.memberOf = memberOf;
        this.operator = operator;
    }


    public boolean getNot_() {
        return not_;
    }

    public void setNot_(boolean not_) {
        this.not_ = not_;
    }
    public String getMemberof() {
        return memberOf;
    }

    public void setMemberof(String memberOf) {
        this.memberOf = memberOf;
    }
    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}