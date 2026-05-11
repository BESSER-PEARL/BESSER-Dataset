





import java.util.List;
import java.util.ArrayList;

public class myDsl_argument_expression_listR  {






    private List<myDsl_argument_expression_listR> mydsl_argument_expression_listrs;




    private myDsl_assignment_expression mydsl_assignment_expression;


    public myDsl_argument_expression_listR(
    ) {
        this.mydsl_argument_expression_listrs = new ArrayList<>();
    }

    public myDsl_argument_expression_listR(
        ArrayList<myDsl_argument_expression_listR> mydsl_argument_expression_listrs    ) {
        this.mydsl_argument_expression_listrs = mydsl_argument_expression_listrs;
    }


    public List<myDsl_argument_expression_listR> getMydsl_argument_expression_listrs() {
        return mydsl_argument_expression_listrs;
    }

    public void addMydsl_argument_expression_listr(Mydsl_argument_expression_listr mydsl_argument_expression_listr) {
        this.mydsl_argument_expression_listrs.add(mydsl_argument_expression_listr);
    }
    public myDsl_assignment_expression getMydsl_assignment_expression() {
        return mydsl_assignment_expression;
    }

    public void setMydsl_assignment_expression(myDsl_assignment_expression mydsl_assignment_expression) {
        this.mydsl_assignment_expression = mydsl_assignment_expression;
    }

}