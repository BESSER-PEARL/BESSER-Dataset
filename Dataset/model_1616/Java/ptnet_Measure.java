





import java.util.List;
import java.util.ArrayList;

public class ptnet_Measure  {

    private String name;





    private ptnet_EvaluationList ptnet_evaluationlist;




    private ptnet_ArithmeticExpression ptnet_arithmeticexpression;


    public ptnet_Measure(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ptnet_EvaluationList getPtnet_evaluationlist() {
        return ptnet_evaluationlist;
    }

    public void setPtnet_evaluationlist(ptnet_EvaluationList ptnet_evaluationlist) {
        this.ptnet_evaluationlist = ptnet_evaluationlist;
    }
    public ptnet_ArithmeticExpression getPtnet_arithmeticexpression() {
        return ptnet_arithmeticexpression;
    }

    public void setPtnet_arithmeticexpression(ptnet_ArithmeticExpression ptnet_arithmeticexpression) {
        this.ptnet_arithmeticexpression = ptnet_arithmeticexpression;
    }

}