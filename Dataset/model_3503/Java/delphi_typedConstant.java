





import java.util.List;
import java.util.ArrayList;

public class delphi_typedConstant extends CSTrace {






    private delphi_constantDecl delphi_constantdecl;




    private delphi_constExpr delphi_constexpr;


    public delphi_typedConstant(
    ) {
        super(
        );
    }



    public delphi_constantDecl getDelphi_constantdecl() {
        return delphi_constantdecl;
    }

    public void setDelphi_constantdecl(delphi_constantDecl delphi_constantdecl) {
        this.delphi_constantdecl = delphi_constantdecl;
    }
    public delphi_constExpr getDelphi_constexpr() {
        return delphi_constexpr;
    }

    public void setDelphi_constexpr(delphi_constExpr delphi_constexpr) {
        this.delphi_constexpr = delphi_constexpr;
    }

}