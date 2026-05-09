





import java.util.List;
import java.util.ArrayList;

public class eol_FOLMethodCallExpression extends FeatureCallExpression {






    private eol_FormalParameterExpression eol_formalparameterexpression;




    private eol_OperationDefinition eol_operationdefinition;




    private eol_NameExpression eol_nameexpression;




    private eol_Expression eol_expression;


    public eol_FOLMethodCallExpression(
    ) {
        super(
        );
    }



    public eol_FormalParameterExpression getEol_formalparameterexpression() {
        return eol_formalparameterexpression;
    }

    public void setEol_formalparameterexpression(eol_FormalParameterExpression eol_formalparameterexpression) {
        this.eol_formalparameterexpression = eol_formalparameterexpression;
    }
    public eol_OperationDefinition getEol_operationdefinition() {
        return eol_operationdefinition;
    }

    public void setEol_operationdefinition(eol_OperationDefinition eol_operationdefinition) {
        this.eol_operationdefinition = eol_operationdefinition;
    }
    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public eol_Expression getEol_expression() {
        return eol_expression;
    }

    public void setEol_expression(eol_Expression eol_expression) {
        this.eol_expression = eol_expression;
    }

}