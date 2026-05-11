





import java.util.List;
import java.util.ArrayList;

public class ClockRDL_literals_QueueLiteral extends Literal {






    private List<kernel_Expression> kernel_expressions;


    public ClockRDL_literals_QueueLiteral(
    ) {
        super(
        );
        this.kernel_expressions = new ArrayList<>();
    }

    public ClockRDL_literals_QueueLiteral(
        ArrayList<kernel_Expression> kernel_expressions    ) {
        this.kernel_expressions = kernel_expressions;
    }


    public List<kernel_Expression> getKernel_expressions() {
        return kernel_expressions;
    }

    public void addKernel_expression(Kernel_expression kernel_expression) {
        this.kernel_expressions.add(kernel_expression);
    }

}