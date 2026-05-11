





import java.util.List;
import java.util.ArrayList;

public class aDSL_Init extends Expression {






    private aDSL_VariableType adsl_variabletype;




    private aDSL_Expression adsl_expression;


    public aDSL_Init(
    ) {
        super(
        );
    }



    public aDSL_VariableType getAdsl_variabletype() {
        return adsl_variabletype;
    }

    public void setAdsl_variabletype(aDSL_VariableType adsl_variabletype) {
        this.adsl_variabletype = adsl_variabletype;
    }
    public aDSL_Expression getAdsl_expression() {
        return adsl_expression;
    }

    public void setAdsl_expression(aDSL_Expression adsl_expression) {
        this.adsl_expression = adsl_expression;
    }

}