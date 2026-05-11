





import java.util.List;
import java.util.ArrayList;

public class roverDSL_AssignExpression extends Expression {






    private roverDSL_Global roverdsl_global;




    private roverDSL_ValueExpression roverdsl_valueexpression;


    public roverDSL_AssignExpression(
    ) {
        super(
        );
    }



    public roverDSL_Global getRoverdsl_global() {
        return roverdsl_global;
    }

    public void setRoverdsl_global(roverDSL_Global roverdsl_global) {
        this.roverdsl_global = roverdsl_global;
    }
    public roverDSL_ValueExpression getRoverdsl_valueexpression() {
        return roverdsl_valueexpression;
    }

    public void setRoverdsl_valueexpression(roverDSL_ValueExpression roverdsl_valueexpression) {
        this.roverdsl_valueexpression = roverdsl_valueexpression;
    }

}