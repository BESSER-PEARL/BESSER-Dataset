





import java.util.List;
import java.util.ArrayList;

public class ilp_ObjectiveFunctionExpression  {

    private String goal;





    private ilp_IntegerLinearProgram ilp_integerlinearprogram;


    public ilp_ObjectiveFunctionExpression(
        String goal    ) {
        this.goal = goal;
    }


    public String getGoal() {
        return goal;
    }

    public void setGoal(String goal) {
        this.goal = goal;
    }

    public ilp_IntegerLinearProgram getIlp_integerlinearprogram() {
        return ilp_integerlinearprogram;
    }

    public void setIlp_integerlinearprogram(ilp_IntegerLinearProgram ilp_integerlinearprogram) {
        this.ilp_integerlinearprogram = ilp_integerlinearprogram;
    }

}