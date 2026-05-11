





import java.util.List;
import java.util.ArrayList;

public class delphi_recVariant extends CSTrace {






    private delphi_variantSection delphi_variantsection;




    private delphi_fieldList delphi_fieldlist;




    private List<delphi_constExpr> delphi_constexprs;


    public delphi_recVariant(
    ) {
        super(
        );
        this.delphi_constexprs = new ArrayList<>();
    }

    public delphi_recVariant(
        ArrayList<delphi_constExpr> delphi_constexprs    ) {
        this.delphi_constexprs = delphi_constexprs;
    }


    public delphi_variantSection getDelphi_variantsection() {
        return delphi_variantsection;
    }

    public void setDelphi_variantsection(delphi_variantSection delphi_variantsection) {
        this.delphi_variantsection = delphi_variantsection;
    }
    public delphi_fieldList getDelphi_fieldlist() {
        return delphi_fieldlist;
    }

    public void setDelphi_fieldlist(delphi_fieldList delphi_fieldlist) {
        this.delphi_fieldlist = delphi_fieldlist;
    }
    public List<delphi_constExpr> getDelphi_constexprs() {
        return delphi_constexprs;
    }

    public void addDelphi_constexpr(Delphi_constexpr delphi_constexpr) {
        this.delphi_constexprs.add(delphi_constexpr);
    }

}