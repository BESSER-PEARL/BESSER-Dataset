





import java.util.List;
import java.util.ArrayList;

public class cal_AstActor extends AstAbstractActor {






    private List<cal_AstVariable> cal_astvariables;




    private List<cal_AstFunction> cal_astfunctions;


    public cal_AstActor(
    ) {
        super(
        );
        this.cal_astvariables = new ArrayList<>();
        this.cal_astfunctions = new ArrayList<>();
    }

    public cal_AstActor(
        ArrayList<cal_AstVariable> cal_astvariables,        ArrayList<cal_AstFunction> cal_astfunctions    ) {
        this.cal_astvariables = cal_astvariables;
        this.cal_astfunctions = cal_astfunctions;
    }


    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }
    public List<cal_AstFunction> getCal_astfunctions() {
        return cal_astfunctions;
    }

    public void addCal_astfunction(Cal_astfunction cal_astfunction) {
        this.cal_astfunctions.add(cal_astfunction);
    }

}