





import java.util.List;
import java.util.ArrayList;

public class FPath_PathExp extends Expression {






    private List<FPath_Step> fpath_steps;




    private FPath_Expression fpath_expression;


    public FPath_PathExp(
    ) {
        super(
        );
        this.fpath_steps = new ArrayList<>();
    }

    public FPath_PathExp(
        ArrayList<FPath_Step> fpath_steps    ) {
        this.fpath_steps = fpath_steps;
    }


    public List<FPath_Step> getFpath_steps() {
        return fpath_steps;
    }

    public void addFpath_step(Fpath_step fpath_step) {
        this.fpath_steps.add(fpath_step);
    }
    public FPath_Expression getFpath_expression() {
        return fpath_expression;
    }

    public void setFpath_expression(FPath_Expression fpath_expression) {
        this.fpath_expression = fpath_expression;
    }

}