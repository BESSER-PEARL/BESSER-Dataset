





import java.util.List;
import java.util.ArrayList;

public class dbl_TypedElement  {

    private boolean isList;





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

    public dbl_IdExpr getDbl_idexpr() {
        return dbl_idexpr;
    }

    public void setDbl_idexpr(dbl_IdExpr dbl_idexpr) {
        this.dbl_idexpr = dbl_idexpr;
    }

}