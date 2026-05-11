





import java.util.List;
import java.util.ArrayList;

public class cal_AstNetwork extends AstAbstractActor {






    private List<cal_AstVariable> cal_astvariables;




    private List<cal_AstActorVariable> cal_astactorvariables;


    public cal_AstNetwork(
    ) {
        super(
        );
        this.cal_astvariables = new ArrayList<>();
        this.cal_astactorvariables = new ArrayList<>();
    }

    public cal_AstNetwork(
        ArrayList<cal_AstVariable> cal_astvariables,        ArrayList<cal_AstActorVariable> cal_astactorvariables    ) {
        this.cal_astvariables = cal_astvariables;
        this.cal_astactorvariables = cal_astactorvariables;
    }


    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }
    public List<cal_AstActorVariable> getCal_astactorvariables() {
        return cal_astactorvariables;
    }

    public void addCal_astactorvariable(Cal_astactorvariable cal_astactorvariable) {
        this.cal_astactorvariables.add(cal_astactorvariable);
    }

}