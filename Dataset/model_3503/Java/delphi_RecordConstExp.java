





import java.util.List;
import java.util.ArrayList;

public class delphi_RecordConstExp extends constExpr {






    private List<delphi_recordConstExpr> delphi_recordconstexprs;


    public delphi_RecordConstExp(
    ) {
        super(
        );
        this.delphi_recordconstexprs = new ArrayList<>();
    }

    public delphi_RecordConstExp(
        ArrayList<delphi_recordConstExpr> delphi_recordconstexprs    ) {
        this.delphi_recordconstexprs = delphi_recordconstexprs;
    }


    public List<delphi_recordConstExpr> getDelphi_recordconstexprs() {
        return delphi_recordconstexprs;
    }

    public void addDelphi_recordconstexpr(Delphi_recordconstexpr delphi_recordconstexpr) {
        this.delphi_recordconstexprs.add(delphi_recordconstexpr);
    }

}