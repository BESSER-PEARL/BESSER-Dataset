





import java.util.List;
import java.util.ArrayList;

public class nabla_Interval extends IterationBlock {

    private int from_;





    private nabla_SimpleVar nabla_simplevar;




    private nabla_Expression nabla_expression;


    public nabla_Interval(
        int from_    ) {
        super(
        );
        this.from_ = from_;
    }


    public int getFrom_() {
        return from_;
    }

    public void setFrom_(int from_) {
        this.from_ = from_;
    }

    public nabla_SimpleVar getNabla_simplevar() {
        return nabla_simplevar;
    }

    public void setNabla_simplevar(nabla_SimpleVar nabla_simplevar) {
        this.nabla_simplevar = nabla_simplevar;
    }
    public nabla_Expression getNabla_expression() {
        return nabla_expression;
    }

    public void setNabla_expression(nabla_Expression nabla_expression) {
        this.nabla_expression = nabla_expression;
    }

}