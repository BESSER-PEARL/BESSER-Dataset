





import java.util.List;
import java.util.ArrayList;

public class cal_InputPattern  {






    private cal_AstAction cal_astaction;




    private cal_AstExpression cal_astexpression;




    private cal_AstPort cal_astport;




    private List<cal_Variable> cal_variables;


    public cal_InputPattern(
    ) {
        this.cal_variables = new ArrayList<>();
    }

    public cal_InputPattern(
        ArrayList<cal_Variable> cal_variables    ) {
        this.cal_variables = cal_variables;
    }


    public cal_AstAction getCal_astaction() {
        return cal_astaction;
    }

    public void setCal_astaction(cal_AstAction cal_astaction) {
        this.cal_astaction = cal_astaction;
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
    public List<cal_Variable> getCal_variables() {
        return cal_variables;
    }

    public void addCal_variable(Cal_variable cal_variable) {
        this.cal_variables.add(cal_variable);
    }

}