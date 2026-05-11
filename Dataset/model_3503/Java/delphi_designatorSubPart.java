





import java.util.List;
import java.util.ArrayList;

public class delphi_designatorSubPart extends CSTrace {






    private List<delphi_exprList> delphi_exprlists;




    private delphi_designator delphi_designator;


    public delphi_designatorSubPart(
    ) {
        super(
        );
        this.delphi_exprlists = new ArrayList<>();
    }

    public delphi_designatorSubPart(
        ArrayList<delphi_exprList> delphi_exprlists    ) {
        this.delphi_exprlists = delphi_exprlists;
    }


    public List<delphi_exprList> getDelphi_exprlists() {
        return delphi_exprlists;
    }

    public void addDelphi_exprlist(Delphi_exprlist delphi_exprlist) {
        this.delphi_exprlists.add(delphi_exprlist);
    }
    public delphi_designator getDelphi_designator() {
        return delphi_designator;
    }

    public void setDelphi_designator(delphi_designator delphi_designator) {
        this.delphi_designator = delphi_designator;
    }

}