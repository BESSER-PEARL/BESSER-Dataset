





import java.util.List;
import java.util.ArrayList;

public class ilp_ConstraintExpression extends BinaryExpression {






    private ilp_IntegerLinearProgram ilp_integerlinearprogram;


    public ilp_ConstraintExpression(
    ) {
        super(
        );
    }



    public ilp_IntegerLinearProgram getIlp_integerlinearprogram() {
        return ilp_integerlinearprogram;
    }

    public void setIlp_integerlinearprogram(ilp_IntegerLinearProgram ilp_integerlinearprogram) {
        this.ilp_integerlinearprogram = ilp_integerlinearprogram;
    }

}