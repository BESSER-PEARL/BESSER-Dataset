





import java.util.List;
import java.util.ArrayList;

public class drn_Expression  {

    private String repeatCST;





    private drn_Parametre drn_parametre;




    private drn_Expression drn_expression;


    public drn_Expression(
        String repeatCST    ) {
        this.repeatCST = repeatCST;
    }


    public String getRepeatcst() {
        return repeatCST;
    }

    public void setRepeatcst(String repeatCST) {
        this.repeatCST = repeatCST;
    }

    public drn_Parametre getDrn_parametre() {
        return drn_parametre;
    }

    public void setDrn_parametre(drn_Parametre drn_parametre) {
        this.drn_parametre = drn_parametre;
    }
    public drn_Expression getDrn_expression() {
        return drn_expression;
    }

    public void setDrn_expression(drn_Expression drn_expression) {
        this.drn_expression = drn_expression;
    }

}