





import java.util.List;
import java.util.ArrayList;

public class alf_PropertyCallExpression extends SuffixExpression {

    private String propertyName;





    private alf_SuffixExpression alf_suffixexpression;




    private alf_Expression alf_expression;


    public alf_PropertyCallExpression(
        String propertyName    ) {
        super(
        );
        this.propertyName = propertyName;
    }


    public String getPropertyname() {
        return propertyName;
    }

    public void setPropertyname(String propertyName) {
        this.propertyName = propertyName;
    }

    public alf_SuffixExpression getAlf_suffixexpression() {
        return alf_suffixexpression;
    }

    public void setAlf_suffixexpression(alf_SuffixExpression alf_suffixexpression) {
        this.alf_suffixexpression = alf_suffixexpression;
    }
    public alf_Expression getAlf_expression() {
        return alf_expression;
    }

    public void setAlf_expression(alf_Expression alf_expression) {
        this.alf_expression = alf_expression;
    }

}