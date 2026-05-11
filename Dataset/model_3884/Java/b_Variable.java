





import java.util.List;
import java.util.ArrayList;

public class b_Variable  {

    private String name;





    private b_ConcreteConstants b_concreteconstants;




    private b_ConcreteVariables b_concretevariables;




    private b_ValueExpr b_valueexpr;


    public b_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public b_ConcreteConstants getB_concreteconstants() {
        return b_concreteconstants;
    }

    public void setB_concreteconstants(b_ConcreteConstants b_concreteconstants) {
        this.b_concreteconstants = b_concreteconstants;
    }
    public b_ConcreteVariables getB_concretevariables() {
        return b_concretevariables;
    }

    public void setB_concretevariables(b_ConcreteVariables b_concretevariables) {
        this.b_concretevariables = b_concretevariables;
    }
    public b_ValueExpr getB_valueexpr() {
        return b_valueexpr;
    }

    public void setB_valueexpr(b_ValueExpr b_valueexpr) {
        this.b_valueexpr = b_valueexpr;
    }

}