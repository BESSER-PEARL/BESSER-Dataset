





import java.util.List;
import java.util.ArrayList;

public class delphi_callStmnt extends simpleStatement {






    private delphi_designator delphi_designator;




    private delphi_exprList delphi_exprlist;


    public delphi_callStmnt(
    ) {
        super(
        );
    }



    public delphi_designator getDelphi_designator() {
        return delphi_designator;
    }

    public void setDelphi_designator(delphi_designator delphi_designator) {
        this.delphi_designator = delphi_designator;
    }
    public delphi_exprList getDelphi_exprlist() {
        return delphi_exprlist;
    }

    public void setDelphi_exprlist(delphi_exprList delphi_exprlist) {
        this.delphi_exprlist = delphi_exprlist;
    }

}