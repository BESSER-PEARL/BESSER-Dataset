





import java.util.List;
import java.util.ArrayList;

public class delphi_MultipleConstExp extends constExpr {






    private List<delphi_constExpr> delphi_constexprs;


    public delphi_MultipleConstExp(
    ) {
        super(
        );
        this.delphi_constexprs = new ArrayList<>();
    }

    public delphi_MultipleConstExp(
        ArrayList<delphi_constExpr> delphi_constexprs    ) {
        this.delphi_constexprs = delphi_constexprs;
    }


    public List<delphi_constExpr> getDelphi_constexprs() {
        return delphi_constexprs;
    }

    public void addDelphi_constexpr(Delphi_constexpr delphi_constexpr) {
        this.delphi_constexprs.add(delphi_constexpr);
    }

}