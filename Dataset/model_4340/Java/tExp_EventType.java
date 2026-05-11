





import java.util.List;
import java.util.ArrayList;

public class tExp_EventType  {

    private String name;





    private tExp_TraceExpression texp_traceexpression;




    private List<tExp_PrologExpression> texp_prologexpressions;




    private tExp_PrologExpression texp_prologexpression;


    public tExp_EventType(
        String name    ) {
        this.name = name;
        this.texp_prologexpressions = new ArrayList<>();
    }

    public tExp_EventType(
        String name        ArrayList<tExp_PrologExpression> texp_prologexpressions    ) {
        this.name = name;
        this.texp_prologexpressions = texp_prologexpressions;
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
    public List<tExp_PrologExpression> getTexp_prologexpressions() {
        return texp_prologexpressions;
    }

    public void addTexp_prologexpression(Texp_prologexpression texp_prologexpression) {
        this.texp_prologexpressions.add(texp_prologexpression);
    }
    public tExp_PrologExpression getTexp_prologexpression() {
        return texp_prologexpression;
    }

    public void setTexp_prologexpression(tExp_PrologExpression texp_prologexpression) {
        this.texp_prologexpression = texp_prologexpression;
    }

}