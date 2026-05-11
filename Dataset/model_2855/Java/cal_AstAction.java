





import java.util.List;
import java.util.ArrayList;

public class cal_AstAction  {






    private List<cal_AstAnnotation> cal_astannotations;




    private cal_AstActor cal_astactor;




    private List<cal_Variable> cal_variables;




    private cal_AstActor cal_astactor;


    public cal_AstAction(
    ) {
        this.cal_astannotations = new ArrayList<>();
        this.cal_variables = new ArrayList<>();
    }

    public cal_AstAction(
        ArrayList<cal_AstAnnotation> cal_astannotations,        ArrayList<cal_Variable> cal_variables    ) {
        this.cal_astannotations = cal_astannotations;
        this.cal_variables = cal_variables;
    }


    public List<cal_AstAnnotation> getCal_astannotations() {
        return cal_astannotations;
    }

    public void addCal_astannotation(Cal_astannotation cal_astannotation) {
        this.cal_astannotations.add(cal_astannotation);
    }
    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }
    public List<cal_Variable> getCal_variables() {
        return cal_variables;
    }

    public void addCal_variable(Cal_variable cal_variable) {
        this.cal_variables.add(cal_variable);
    }
    public cal_AstActor getCal_astactor() {
        return cal_astactor;
    }

    public void setCal_astactor(cal_AstActor cal_astactor) {
        this.cal_astactor = cal_astactor;
    }

}