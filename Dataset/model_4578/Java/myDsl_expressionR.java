





import java.util.List;
import java.util.ArrayList;

public class myDsl_expressionR  {






    private myDsl_expression mydsl_expression;




    private List<myDsl_expressionR> mydsl_expressionrs;




    private myDsl_assignment_expression mydsl_assignment_expression;


    public myDsl_expressionR(
    ) {
        this.mydsl_expressionrs = new ArrayList<>();
    }

    public myDsl_expressionR(
        ArrayList<myDsl_expressionR> mydsl_expressionrs    ) {
        this.mydsl_expressionrs = mydsl_expressionrs;
    }


    public myDsl_expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }
    public List<myDsl_expressionR> getMydsl_expressionrs() {
        return mydsl_expressionrs;
    }

    public void addMydsl_expressionr(Mydsl_expressionr mydsl_expressionr) {
        this.mydsl_expressionrs.add(mydsl_expressionr);
    }
    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }

}