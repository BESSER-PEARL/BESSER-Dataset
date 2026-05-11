





import java.util.List;
import java.util.ArrayList;

public class nabla_ReductionCall extends Iterable, Expression {






    private nabla_Expression nabla_expression;




    private nabla_Reduction nabla_reduction;


    public nabla_ReductionCall(
    ) {
        super(
        );
    }



    public nabla_Expression getNabla_expression() {
        return nabla_expression;
    }

    public void setNabla_expression(nabla_Expression nabla_expression) {
        this.nabla_expression = nabla_expression;
    }
    public nabla_Reduction getNabla_reduction() {
        return nabla_reduction;
    }

    public void setNabla_reduction(nabla_Reduction nabla_reduction) {
        this.nabla_reduction = nabla_reduction;
    }

}