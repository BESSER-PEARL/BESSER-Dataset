





import java.util.List;
import java.util.ArrayList;

public class cal_AstNetwork extends AstAbstractActor {






    private List<cal_AstVariable> cal_astvariables;


    public cal_AstNetwork(
    ) {
        super(
        );
        this.cal_astvariables = new ArrayList<>();
    }

    public cal_AstNetwork(
        ArrayList<cal_AstVariable> cal_astvariables    ) {
        this.cal_astvariables = cal_astvariables;
    }


    public List<cal_AstVariable> getCal_astvariables() {
        return cal_astvariables;
    }

    public void addCal_astvariable(Cal_astvariable cal_astvariable) {
        this.cal_astvariables.add(cal_astvariable);
    }

}