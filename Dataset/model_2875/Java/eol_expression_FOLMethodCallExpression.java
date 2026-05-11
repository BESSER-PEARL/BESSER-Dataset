





import java.util.List;
import java.util.ArrayList;

public class eol_expression_FOLMethodCallExpression extends FeatureCallExpression {






    private eol_expression_FormalParameterExpression eol_expression_formalparameterexpression;




    private List<eol_expression_Expression> eol_expression_expressions;




    private eol_expression_NameExpression eol_expression_nameexpression;


    public eol_expression_FOLMethodCallExpression(
    ) {
        super(
        );
        this.eol_expression_expressions = new ArrayList<>();
    }

    public eol_expression_FOLMethodCallExpression(
        ArrayList<eol_expression_Expression> eol_expression_expressions    ) {
        this.eol_expression_expressions = eol_expression_expressions;
    }


    public eol_expression_FormalParameterExpression getEol_expression_formalparameterexpression() {
        return eol_expression_formalparameterexpression;
    }

    public void setEol_expression_formalparameterexpression(eol_expression_FormalParameterExpression eol_expression_formalparameterexpression) {
        this.eol_expression_formalparameterexpression = eol_expression_formalparameterexpression;
    }
    public List<eol_expression_Expression> getEol_expression_expressions() {
        return eol_expression_expressions;
    }

    public void addEol_expression_expression(Eol_expression_expression eol_expression_expression) {
        this.eol_expression_expressions.add(eol_expression_expression);
    }
    public eol_expression_NameExpression getEol_expression_nameexpression() {
        return eol_expression_nameexpression;
    }

    public void setEol_expression_nameexpression(eol_expression_NameExpression eol_expression_nameexpression) {
        this.eol_expression_nameexpression = eol_expression_nameexpression;
    }

}