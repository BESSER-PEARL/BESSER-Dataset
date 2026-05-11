





import java.util.List;
import java.util.ArrayList;

public class dbl_Expression extends ExtensibleElement, TypedElement {






    private dbl_ExpandExpr dbl_expandexpr;




    private dbl_IdExpr dbl_idexpr;




    private dbl_ArrayDimension dbl_arraydimension;




    private dbl_Variable dbl_variable;


    public dbl_Expression(
    ) {
        super(
        );
    }



    public dbl_ExpandExpr getDbl_expandexpr() {
        return dbl_expandexpr;
    }

    public void setDbl_expandexpr(dbl_ExpandExpr dbl_expandexpr) {
        this.dbl_expandexpr = dbl_expandexpr;
    }
    public dbl_IdExpr getDbl_idexpr() {
        return dbl_idexpr;
    }

    public void setDbl_idexpr(dbl_IdExpr dbl_idexpr) {
        this.dbl_idexpr = dbl_idexpr;
    }
    public dbl_ArrayDimension getDbl_arraydimension() {
        return dbl_arraydimension;
    }

    public void setDbl_arraydimension(dbl_ArrayDimension dbl_arraydimension) {
        this.dbl_arraydimension = dbl_arraydimension;
    }
    public dbl_Variable getDbl_variable() {
        return dbl_variable;
    }

    public void setDbl_variable(dbl_Variable dbl_variable) {
        this.dbl_variable = dbl_variable;
    }

}