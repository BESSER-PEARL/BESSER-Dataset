





import java.util.List;
import java.util.ArrayList;

public class cal_AstAction  {






    private cal_AstActor cal_astactor;




    private List<cal_AstAnnotation> cal_astannotations;




    private List<cal_AstExpression> cal_astexpressions;




    private cal_AstActor cal_astactor;




    private List<cal_AstVariable> cal_astvariables;


    public cal_AstAction(
    ) {
        this.cal_astannotations = new ArrayList<>();
        this.cal_astexpressions = new ArrayList<>();
        this.cal_astvariables = new ArrayList<>();
    }

    public cal_AstAction(
        ArrayList<cal_AstAnnotation> cal_astannotations,        ArrayList<cal_AstExpression> cal_astexpressions,        ArrayList<cal_AstVariable> cal_astvariables    ) {
        this.cal_astannotations = cal_astannotations;
        this.cal_astexpressions = cal_astexpressions;
        this.cal_astvariables = cal_astvariables;
    }


    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }
    public List<cal_AstAnnotation> getCal_astannotations() {
        return cal_astannotations;
    }

    public void addCal_astannotation(Cal_astannotation cal_astannotation) {
        this.cal_astannotations.add(cal_astannotation);
    }
    public List<cal_AstExpression> getCal_astexpressions() {
        return cal_astexpressions;
    }

    public void addCal_astexpression(Cal_astexpression cal_astexpression) {
        this.cal_astexpressions.add(cal_astexpression);
    }
    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }
    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }

}