





import java.util.List;
import java.util.ArrayList;

public class cal_AstStatementForeach extends AstStatement {






    private List<cal_AstStatement> cal_aststatements;




    private List<cal_AstVariable> cal_astvariables;


    public cal_AstStatementForeach(
    ) {
        super(
        );
        this.cal_aststatements = new ArrayList<>();
        this.cal_astvariables = new ArrayList<>();
    }

    public cal_AstStatementForeach(
        ArrayList<cal_AstStatement> cal_aststatements,        ArrayList<cal_AstVariable> cal_astvariables    ) {
        this.cal_aststatements = cal_aststatements;
        this.cal_astvariables = cal_astvariables;
    }


    public List<cal_AstStatement> getCal_aststatements() {
        return cal_aststatements;
    }

    public void addCal_aststatement(Cal_aststatement cal_aststatement) {
        this.cal_aststatements.add(cal_aststatement);
    }
    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }

}