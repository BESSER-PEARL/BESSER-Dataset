





import java.util.List;
import java.util.ArrayList;

public class dbl_Expression extends TypedElement, ExtensibleElement {






    private dbl_Variable dbl_variable;




    private dbl_ExpandExpr dbl_expandexpr;


    public dbl_Expression(
    ) {
        super(
        );
    }



    public dbl_Variable getDbl_variable() {
        return dbl_variable;
    }

    public void setDbl_variable(dbl_Variable dbl_variable) {
        this.dbl_variable = dbl_variable;
    }
    public dbl_ExpandExpr getDbl_expandexpr() {
        return dbl_expandexpr;
    }

    public void setDbl_expandexpr(dbl_ExpandExpr dbl_expandexpr) {
        this.dbl_expandexpr = dbl_expandexpr;
    }

}