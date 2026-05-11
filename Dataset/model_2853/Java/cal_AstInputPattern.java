





import java.util.List;
import java.util.ArrayList;

public class cal_AstInputPattern  {






    private cal_AstExpression cal_astexpression;




    private cal_AstPort cal_astport;




    private cal_AstAction cal_astaction;




    private List<cal_AstVariable> cal_astvariables;


    public cal_AstInputPattern(
    ) {
        this.cal_astvariables = new ArrayList<>();
    }

    public cal_AstInputPattern(
        ArrayList<cal_AstVariable> cal_astvariables    ) {
        this.cal_astvariables = cal_astvariables;
    }


    public cal_AstExpression getCal_astexpression() {
        return cal_astexpression;
    }

    public void setCal_astexpression(cal_AstExpression cal_astexpression) {
        this.cal_astexpression = cal_astexpression;
    }
    public cal_AstPort getCal_astport() {
        return cal_astport;
    }

    public void setCal_astport(cal_AstPort cal_astport) {
        this.cal_astport = cal_astport;
    }
    public cal_AstAction getCal_astaction() {
        return cal_astaction;
    }

    public void setCal_astaction(cal_AstAction cal_astaction) {
        this.cal_astaction = cal_astaction;
    }
    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }

}