





import java.util.List;
import java.util.ArrayList;

public class cal_AstOutputPattern  {






    private cal_AstAction cal_astaction;




    private List<cal_AstExpression> cal_astexpressions;




    private cal_AstExpression cal_astexpression;




    private cal_AstPort cal_astport;


    public cal_AstOutputPattern(
    ) {
        this.cal_astexpressions = new ArrayList<>();
    }

    public cal_AstOutputPattern(
        ArrayList<cal_AstExpression> cal_astexpressions    ) {
        this.cal_astexpressions = cal_astexpressions;
    }


    public cal_AstAction getCal_astaction() {
        return cal_astaction;
    }

    public void setCal_astaction(cal_AstAction cal_astaction) {
        this.cal_astaction = cal_astaction;
    }
    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
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

}