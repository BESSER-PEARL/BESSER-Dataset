





import java.util.List;
import java.util.ArrayList;

public class gastm_SwitchStatement extends Statement {






    private gastm_SwitchCase gastm_switchcase;




    private gastm_Expression gastm_expression;


    public gastm_SwitchStatement(
    ) {
        super(
        );
    }



    public gastm_SwitchCase getGastm_switchcase() {
        return gastm_switchcase;
    }

    public void setGastm_switchcase(gastm_SwitchCase gastm_switchcase) {
        this.gastm_switchcase = gastm_switchcase;
    }
    public gastm_Expression getGastm_expression() {
        return gastm_expression;
    }

    public void setGastm_expression(gastm_Expression gastm_expression) {
        this.gastm_expression = gastm_expression;
    }

}