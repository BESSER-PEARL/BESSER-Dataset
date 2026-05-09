





import java.util.List;
import java.util.ArrayList;

public class ocl_exp_ELoopExp extends ECallExp {






    private EOclExpression eoclexpression;




    private List<EVariable> evariables;


    public ocl_exp_ELoopExp(
    ) {
        super(
        );
        this.evariables = new ArrayList<>();
    }

    public ocl_exp_ELoopExp(
        ArrayList<EVariable> evariables    ) {
        this.evariables = evariables;
    }


    public EOclExpression getEoclexpression() {
        return eoclexpression;
    }

    public void setEoclexpression(EOclExpression eoclexpression) {
        this.eoclexpression = eoclexpression;
    }
    public List<EVariable> getEvariables() {
        return evariables;
    }

    public void addEvariable(Evariable evariable) {
        this.evariables.add(evariable);
    }

}