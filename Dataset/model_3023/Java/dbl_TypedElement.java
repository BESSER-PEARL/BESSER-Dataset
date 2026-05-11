





import java.util.List;
import java.util.ArrayList;

public class dbl_TypedElement  {

    private boolean isList;





    private dbl_PrimitiveType dbl_primitivetype;




    private dbl_IdExpr dbl_idexpr;


    public dbl_TypedElement(
        boolean isList    ) {
        this.isList = isList;
    }


    public boolean getIslist() {
        return isList;
    }

    public void setIslist(boolean isList) {
        this.isList = isList;
    }

    public dbl_PrimitiveType getDbl_primitivetype() {
        return dbl_primitivetype;
    }

    public void setDbl_primitivetype(dbl_PrimitiveType dbl_primitivetype) {
        this.dbl_primitivetype = dbl_primitivetype;
    }
    public dbl_IdExpr getDbl_idexpr() {
        return dbl_idexpr;
    }

    public void setDbl_idexpr(dbl_IdExpr dbl_idexpr) {
        this.dbl_idexpr = dbl_idexpr;
    }

}