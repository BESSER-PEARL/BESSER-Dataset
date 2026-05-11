





import java.util.List;
import java.util.ArrayList;

public class cal_Guard  {






    private cal_AstAction cal_astaction;




    private List<cal_AstExpression> cal_astexpressions;


    public cal_Guard(
    ) {
        this.cal_astexpressions = new ArrayList<>();
    }

    public cal_Guard(
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

}