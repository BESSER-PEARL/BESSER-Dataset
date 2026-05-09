





import java.util.List;
import java.util.ArrayList;

public class eol_FOLMethodCallExpression extends FeatureCallExpression {






    private List<eol_Expression> eol_expressions;




    private eol_NameExpression eol_nameexpression;




    private eol_FormalParameterExpression eol_formalparameterexpression;


    public eol_FOLMethodCallExpression(
    ) {
        super(
        );
        this.eol_expressions = new ArrayList<>();
    }

    public eol_FOLMethodCallExpression(
        ArrayList<eol_Expression> eol_expressions    ) {
        this.eol_expressions = eol_expressions;
    }


    public List<eol_Expression> getEol_expressions() {
        return eol_expressions;
    }

    public void addEol_expression(Eol_expression eol_expression) {
        this.eol_expressions.add(eol_expression);
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public eol_FormalParameterExpression getEol_formalparameterexpression() {
        return eol_formalparameterexpression;
    }

    public void setEol_formalparameterexpression(eol_FormalParameterExpression eol_formalparameterexpression) {
        this.eol_formalparameterexpression = eol_formalparameterexpression;
    }

}