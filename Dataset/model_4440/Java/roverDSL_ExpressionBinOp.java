





import java.util.List;
import java.util.ArrayList;

public class roverDSL_ExpressionBinOp extends ValueExpression {

    private String bop;





    private roverDSL_ValueExpression roverdsl_valueexpression;




    private roverDSL_ValueExpression roverdsl_valueexpression;


    public roverDSL_ExpressionBinOp(
        String bop    ) {
        super(
        );
        this.bop = bop;
    }


    public String getBop() {
        return bop;
    }

    public void setBop(String bop) {
        this.bop = bop;
    }

    public roverDSL_ValueExpression getRoverdsl_valueexpression() {
        return roverdsl_valueexpression;
    }

    public void setRoverdsl_valueexpression(roverDSL_ValueExpression roverdsl_valueexpression) {
        this.roverdsl_valueexpression = roverdsl_valueexpression;
    }
    public roverDSL_ValueExpression getRoverdsl_valueexpression() {
        return roverdsl_valueexpression;
    }

    public void setRoverdsl_valueexpression(roverDSL_ValueExpression roverdsl_valueexpression) {
        this.roverdsl_valueexpression = roverdsl_valueexpression;
    }

}