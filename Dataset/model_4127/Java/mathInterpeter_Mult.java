





import java.util.List;
import java.util.ArrayList;

public class mathInterpeter_Mult extends Exp {






    private mathInterpeter_Exp mathinterpeter_exp;




    private mathInterpeter_Primary mathinterpeter_primary;


    public mathInterpeter_Mult(
    ) {
        super(
        );
    }



    public mathInterpeter_Exp getMathinterpeter_exp() {
        return mathinterpeter_exp;
    }

    public void setMathinterpeter_exp(mathInterpeter_Exp mathinterpeter_exp) {
        this.mathinterpeter_exp = mathinterpeter_exp;
    }
    public mathInterpeter_Primary getMathinterpeter_primary() {
        return mathinterpeter_primary;
    }

    public void setMathinterpeter_primary(mathInterpeter_Primary mathinterpeter_primary) {
        this.mathinterpeter_primary = mathinterpeter_primary;
    }

}