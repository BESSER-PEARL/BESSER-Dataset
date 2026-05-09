





import java.util.List;
import java.util.ArrayList;

public class eol_MethodCallExpression extends FeatureCallExpression {






    private eol_NameExpression eol_nameexpression;




    private List<eol_Expression> eol_expressions;




    private eol_OperationDefinition eol_operationdefinition;


    public eol_MethodCallExpression(
    ) {
        super(
        );
        this.eol_expressions = new ArrayList<>();
    }

    public eol_MethodCallExpression(
        ArrayList<eol_Expression> eol_expressions    ) {
        this.eol_expressions = eol_expressions;
    }


    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public List<eol_Expression> getEol_expressions() {
        return eol_expressions;
    }

    public void addEol_expression(Eol_expression eol_expression) {
        this.eol_expressions.add(eol_expression);
    }
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
    }

}