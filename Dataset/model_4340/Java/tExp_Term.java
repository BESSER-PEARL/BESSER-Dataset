





import java.util.List;
import java.util.ArrayList;

public class tExp_Term  {

    private String name;





    private tExp_TraceExpression texp_traceexpression;


    public tExp_Term(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tExp_TraceExpression getTexp_traceexpression() {
        return texp_traceexpression;
    }

    public void setTexp_traceexpression(tExp_TraceExpression texp_traceexpression) {
        this.texp_traceexpression = texp_traceexpression;
    }

}