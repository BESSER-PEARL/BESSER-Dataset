





import java.util.List;
import java.util.ArrayList;

public class aDSL_WhileStat extends Statement {






    private aDSL_Expression adsl_expression;




    private aDSL_Body adsl_body;


    public aDSL_WhileStat(
    ) {
        super(
        );
    }



    public aDSL_Expression getAdsl_expression() {
        return adsl_expression;
    }

    public void setAdsl_expression(aDSL_Expression adsl_expression) {
        this.adsl_expression = adsl_expression;
    }
    public aDSL_Body getAdsl_body() {
        return adsl_body;
    }

    public void setAdsl_body(aDSL_Body adsl_body) {
        this.adsl_body = adsl_body;
    }

}