





import java.util.List;
import java.util.ArrayList;

public class alf_SuffixExpression  {






    private alf_ParenthesizedExpression alf_parenthesizedexpression;




    private alf_NameExpression alf_nameexpression;




    private alf_InstanceCreationExpression alf_instancecreationexpression;




    private alf_LITERAL alf_literal;




    private alf_ThisExpression alf_thisexpression;


    public alf_SuffixExpression(
    ) {
    }



    public alf_ParenthesizedExpression getAlf_parenthesizedexpression() {
        return alf_parenthesizedexpression;
    }

    public void setAlf_parenthesizedexpression(alf_ParenthesizedExpression alf_parenthesizedexpression) {
        this.alf_parenthesizedexpression = alf_parenthesizedexpression;
    }
    public alf_NameExpression getAlf_nameexpression() {
        return alf_nameexpression;
    }

    public void setAlf_nameexpression(alf_NameExpression alf_nameexpression) {
        this.alf_nameexpression = alf_nameexpression;
    }
    public alf_InstanceCreationExpression getAlf_instancecreationexpression() {
        return alf_instancecreationexpression;
    }

    public void setAlf_instancecreationexpression(alf_InstanceCreationExpression alf_instancecreationexpression) {
        this.alf_instancecreationexpression = alf_instancecreationexpression;
    }
    public alf_LITERAL getAlf_literal() {
        return alf_literal;
    }

    public void setAlf_literal(alf_LITERAL alf_literal) {
        this.alf_literal = alf_literal;
    }
    public alf_ThisExpression getAlf_thisexpression() {
        return alf_thisexpression;
    }

    public void setAlf_thisexpression(alf_ThisExpression alf_thisexpression) {
        this.alf_thisexpression = alf_thisexpression;
    }

}